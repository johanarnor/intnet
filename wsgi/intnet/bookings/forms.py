from django import forms
from bookings.models import Booking, People
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


class PeopleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        booking = kwargs.pop('booking')
        super(PeopleForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = reverse('bookings:booking', args=(booking.pk, ))
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('edit_people', 'Spara', css_class='btn btn-success'))
        self.helper.layout = Layout(
            Field('label', type="hidden"),
            Field('booking', type="hidden"),
            'adult',
            'youth',
            'child',
            'student',
            'senior',
        )

    class Meta:
        model = People