from django import forms
from .models import csvimport


class DataForm(forms.ModelForm):

	class Meta:
		model = csvimport
		fields = ('description', 'file', )

class PlotForm(forms.Form):
	x_axis = forms.CharField(label='X Axis', max_length=100),
	hue = forms.CharField(label='hue',max_length=100),
	