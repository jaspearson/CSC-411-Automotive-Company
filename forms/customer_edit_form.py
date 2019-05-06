from django import forms
from auto.models import *
from auto.models import Customer
import datetime

# Used to specify the range of years that appears in the Date of birth field.
YEARS = [x for x in range(1919, 2020)]
#forms.ModelForm
class CustomerEditForm(forms.Form):


	first_name = forms.CharField(label='First name', max_length=100)
	last_name = forms.CharField(label='Last name', max_length=100)

	# Make DOB Required, use a date picker control, and default to today's date.
	DOB = forms.DateField(label='Date of birth', required=True, widget=forms.SelectDateWidget(years=YEARS), initial=datetime.date.today())

	address1 = forms.CharField(label='Address 1', max_length=100)
	address2 = forms.CharField(label='Address 2', max_length=100, required=False)
	city = forms.CharField(label='City', max_length=50)
	state = forms.ModelChoiceField(label='State', queryset=State.objects.values_list('abbreviation', flat=True), empty_label='-- None --')
	zip = forms.CharField(label='Zip code', max_length=5)
	email = forms.CharField(label='Email address', max_length=100, widget=forms.EmailInput())
	phone = forms.CharField(label='Phone', max_length=15)
	gender = forms.CharField(label='Gender', max_length=1)
	annual_income = forms.ModelChoiceField(label='Annual income', to_field_name="id", queryset=cust_income_range.objects.all(), empty_label='-- None --')

	# Returns the cleaned data in the form of list.
	def get_data_list(self):
		data_list = []

		for key in self.cleaned_data:

			if hasattr(self.cleaned_data[key], 'pk'):
				data_list.append(self.cleaned_data[key].pk)

			else:
				data_list.append(self.cleaned_data[key])

		return data_list