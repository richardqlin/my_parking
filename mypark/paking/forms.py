from django import forms

from .models import Spots, Paking

class SpotsForm(forms.ModelForm):
	class Meta:
		model=Spots

		fields='__all__'


