# -*- coding: utf-8 -*
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.urlresolvers import reverse


class LoginForm(forms.Form):

    username = forms.CharField(max_length=128, label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), max_length=128, label="Password")

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('users:authenticate')
        self.helper.add_input(Submit('login', 'Login', css_class='btn btn-default'))
