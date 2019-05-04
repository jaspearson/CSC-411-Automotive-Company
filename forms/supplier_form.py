from django import forms
from auto.models import State

class SupplierForm(forms.Form):
	name = forms.CharField(max_length=100)
	address1 = forms.CharField(max_length=100)
	address2 = forms.CharField(max_length=100, required=False)
	city = forms.CharField(max_length=50)
	state =forms.ModelChoiceField(label='State', queryset=State.objects.values_list('abbreviation', flat=True), empty_label='-- None --')
	zip = forms.CharField(max_length=5, min_length=5)
	phone = forms.CharField(max_length=15)