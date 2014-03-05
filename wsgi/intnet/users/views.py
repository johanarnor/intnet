from django.template import RequestContext
from django.shortcuts import render
from users.forms import LoginForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login


def login_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('main:main'))
    else:
        form = LoginForm()
        dictionary = {'form': form}

    return render(request, 'users/login.html', dictionary)


def authenticate_view(request):
    user_username = request.POST['username']
    user_password = request.POST['password']
    user = authenticate(username=user_username, password=user_password)
    if user is not None:
        login(request, user)
        print 'logging in...'
        return HttpResponseRedirect(reverse('main:main'))
    else:
        print 'not logging in...'
        return HttpResponseRedirect(reverse('users:login'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))