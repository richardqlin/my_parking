from django import forms

from .models import Car, Parking

class CarForm(forms.ModelForm):
	class Meta:
		model=Car

		fields='__all__'


class ParkingForm(forms.ModelForm):
	class Meta:
		model=Parking

		fields='__all__'