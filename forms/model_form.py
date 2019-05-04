from django import forms

class cModelForm(forms.Form):
	name = forms.CharField(max_length=100)
	base_price = forms.DecimalField(max_digits=10, decimal_places=2)
	est_miles_per_gallon = forms.IntegerField()
	body_style = forms.CharField(max_length=45)
	year = forms.IntegerField()
	color = forms.CharField(max_length=45)
	engine = forms.CharField(max_length=45)
	transmission = forms.CharField(max_length=45)
	brand = forms.CharField(max_length=45)