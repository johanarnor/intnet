# -*- coding: utf-8 -*
from django import forms
from users.models import DirrUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Field
from django.core.urlresolvers import reverse


class LoginForm(forms.Form):

    username = forms.CharField(max_length=128, label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), max_length=128, label="Password")

    def __init__(self, *args, **kwargs):
        next_url = kwargs.pop('next_url')
        print next_url
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('users:authenticate')
        self.fields['next_url'] = forms.CharField(max_length=255)
        self.fields['next_url'].initial = next_url
        self.helper.add_input(Submit('login', 'Login', css_class='btn btn-default'))
        self.helper.layout = Layout(
            Fieldset("Login",
                'username',
                'password',
                Field('next_url', type="hidden")
            ),
        )


class SignUpForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    helper = FormHelper()
    helper.form_action = 'users:sign_up'
    helper.form_method = 'POST'
    helper.add_input(Submit('create_user', 'Sign Up', css_class='btn btn-success'))

    class Meta:
        model = DirrUser
        exclude = ['password', 'groups', 'is_superuser', 'is_staff', 'is_active', 'last_login', 'user_permissions', 'date_joined']

