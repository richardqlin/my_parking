from django import forms

from .models import Car, Parking

class CarForm(forms.ModelForm):
	class Meta:
		model=Car

		fields='__all__'


