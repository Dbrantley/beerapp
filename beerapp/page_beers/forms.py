from django import forms
from beerapp.db_models.t_beers.models import BeerApp
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

#Will be used in the future to let users sign up
class PersonalDataForm(ModelForm):
   comments = forms.CharField(max_length=255)

   class Meta:
       model = BeerApp
       fields=('comments',)

   def __init__(self, *args, **kwargs):
       super(PersonalDataForm, self).__init__(*args, **kwargs)
       self.helper = FormHelper()
       self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
       self.helper.form_method = 'POST'

