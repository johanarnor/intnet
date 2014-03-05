from django import forms
from bookings.models import Booking
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Field
from django.core.urlresolvers import reverse


class BookingForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_action = 'bookings:booking'
    helper.form_method = 'POST'
    helper.add_input(Submit('edit_booking', 'Sign Up', css_class='btn btn-success'))

    class Meta:
        model = Booking
        exclude = ['user', 'activity', 'amount']