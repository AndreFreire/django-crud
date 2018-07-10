from django import forms

from .models import Person

class PersonForms(forms.ModelForm):

	class Meta:
		model = Person
		fields = ('name', 'last_name', 'nick_name')