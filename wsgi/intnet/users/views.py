from django.template import RequestContext
from django.shortcuts import render
from users.forms import LoginForm, SignUpForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from users.models import DirrUser


def login_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('main:main'))
    else:
        if 'next' in request.GET:
            next_url = request.GET['next']
        else:
            next_url = '/'
        form = LoginForm(next_url=next_url)
        dictionary = {'form': form}

    return render(request, 'users/login.html', dictionary)


def authenticate_view(request):
    user_username = request.POST['username']
    user_password = request.POST['password']
    user = authenticate(username=user_username, password=user_password)
    if user is not None:
        login(request, user)
        print 'logging in...'
        return HttpResponseRedirect(request.POST['next_url'])
    else:
        print 'not logging in...'
        return HttpResponseRedirect(reverse('users:login'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:main'))


def sign_up_view(request):
    if request.method != 'POST':
        form = SignUpForm()
        dictionary = {'form': form}
        return render(request, 'users/sign_up.html', dictionary)
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] != form.cleaned_data['password2']:
                dictionary = {'form': form, 'pw': 'Passwords did not match'}
                return render(request, 'users/sign_up.html', dictionary)
            else:
                user = DirrUser.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], email=form.cleaned_data['email'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], phone_nr=form.cleaned_data['phone_nr'], address=form.cleaned_data['address'], p_code=form.cleaned_data['p_code'], city=form.cleaned_data['city'])
                user.is_active = True
                user.is_staff = False
                user.is_superuser = False
                user.save()
                user.authenticate(form.cleaned_data['username'], form.cleaned_data['password1'])
                login(request, user)
        else:
            dictionary = {'form': form, 'pw': 'Some fields were left blank'}
            return render(request, 'users/sign_up.html', dictionary)
        return HttpResponseRedirect(reverse('main:main'))

