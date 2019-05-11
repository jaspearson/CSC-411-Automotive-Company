from django import forms

# Custom form class child of forms.Forms from which all of my forms will inherit functionality.
class CustomForm(forms.Form):

	# Returns the cleaned data in the form of list.
	def get_data_list(self):
		data_list = []

		for key in self.cleaned_data:

			if hasattr(self.cleaned_data[key], 'pk'):
				print("Key: %s, value: %s, PK: %s" % (key, self.cleaned_data[key], self.cleaned_data[key].pk))
				data_list.append(self.cleaned_data[key].pk)

			else:
				print("Key: %s, Value: %s" %(key, self.cleaned_data[key]))
				data_list.append(self.cleaned_data[key])

		print(data_list)
		return data_list