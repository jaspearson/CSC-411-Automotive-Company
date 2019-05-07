from django import forms

# Custom form class child of forms.Forms from which all of my forms will inherit functionality.
class CustomForm(forms.Form):

	# Returns the cleaned data in the form of list.
	def get_data_list(self):
		data_list = []

		for key in self.cleaned_data:

			if hasattr(self.cleaned_data[key], 'pk'):
				data_list.append(self.cleaned_data[key].pk)

			else:
				data_list.append(self.cleaned_data[key])

		return data_list