from .custom_form import *
from auto.models import State


class DealerForm(CustomForm):

	name = forms.CharField(label='Name', max_length=100)
	address1 = forms.CharField(label='Address 1', max_length=100)
	address2 = forms.CharField(label='Address 2', max_length=100, required=False)
	city = forms.CharField(label='City', max_length=50)
	state = forms.ModelChoiceField(label='State', queryset=State.objects.values_list('abbreviation', flat=True), empty_label='-- None --')
	zip = forms.CharField(label='Zip code', max_length=5)
	phone = forms.CharField(label='Phone', max_length=15, required=False)