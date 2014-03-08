# -*- coding: utf-8 -*
from crispy_forms.bootstrap import InlineField
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Fieldset, Div, HTML
from django.core.urlresolvers import reverse


class FeatureForm(forms.Form, ):
    def __init__(self, *args, **kwargs):
        features = kwargs.pop('features')
        super(FeatureForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'features'
        counter = 1
        for feature in features:
            options_list = [("", "Välj ett alternativ")]
            for option in feature.featureoption_set.all():
                options_list = options_list + [(option.option, option.option)]

            self.fields['feature' + str(counter)] = forms.ChoiceField(label=feature.feature, choices=options_list)
            counter += 1


class ActivityForm(FeatureForm):
    def __init__(self, *args, **kwargs):
        activity = kwargs.pop('activity')
        people_list = [('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')]
        super(ActivityForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.fields['date'] = forms.DateField(label="Datum")

        self.fields['adults'] = forms.ChoiceField(label="Vuxna", choices=people_list)
        self.fields['youths'] = forms.ChoiceField(label="Ungdomar", choices=people_list)
        self.fields['children'] = forms.ChoiceField(label="Barn", choices=people_list)
        self.fields['students'] = forms.ChoiceField(label="Studenter", choices=people_list)
        self.fields['seniors'] = forms.ChoiceField(label="Pensionärer", choices=people_list)

        self.helper.form_class = "form-inline"
        self.helper.label_class = "control-label"
        self.helper.form_method = "POST"
        self.helper.form_action = reverse('bookings:create_booking', args=(activity.pk,))
        self.helper.layout = Layout(
            Div(
                Div(
                    Field('feature1'),
                    css_class="col-xs-5 col-xs-offset-1",
                ),
                Div(
                    Field('feature2'),
                    css_class="col-xs-5",
                ),
                Div(
                    Field('feature3'),
                    css_class="col-xs-5 col-xs-offset-1",
                ),
                Div(
                    Field('feature4'),
                    css_class="col-xs-5",
                ),
                Div(
                    Field('feature5'),
                    css_class="col-xs-5 col-xs-offset-1",
                ),
                Div(
                    Field('feature6'),
                    css_class="col-xs-5",
                ),
                Div(
                    Field('feature7'),
                    css_class="col-xs-5 col-xs-offset-1",
                ),
                Div(
                    Field('feature8'),
                    css_class="col-xs-5",
                ),
                Div(
                    Field('feature9'),
                    css_class="col-xs-5 col-xs-offset-1",
                ),
                Div(
                    Field('feature10'),
                    css_class="col-xs-5",
                ),
                css_class="row",
            ),
            Div(
                Div(
                    Field('date'),
                    css_class="col-xs-5 col-xs-offset-1",
                ),
                css_class="row",
            ),
            Div(
                Div(
                    Field('adults'),
                    css_class="col-xs-2 col-xs-offset-1"
                ),
                Div(
                    Field('youths'),
                    css_class="col-xs-2"
                ),
                Div(
                    Field('children'),
                    css_class="col-xs-2"
                ),
                Div(
                    Field('students'),
                    css_class="col-xs-2"
                ),
                Div(
                    Field('seniors'),
                    css_class="col-xs-2"
                ),
                css_class="row",
            ),
            HTML("<br>"),
            Div(
                Div(
                    Submit('book', 'Boka', css_class="btn btn-default"),
                    css_class="col-xs-5 col-xs-offset-1",
                ),
                css_class="row",
            ),

        )



