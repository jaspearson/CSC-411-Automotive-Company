from django.db import models

# Create your models here.


# Customers Model
class Customer(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	DOB = models.DateField(null=False)
	address1 = models.CharField(max_length=100)
	address2 = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=2)
	zip = models.CharField(max_length=5)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	gender = models.CharField(max_length=1)
	annual_income = models.IntegerField()
	#created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


# Dealer Model
class Dealer(models.Model):
	name = models.CharField(max_length=100)
	address1 = models.CharField(max_length=100)
	address2 = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=2)
	zip = models.CharField(max_length=5)
	phone = models.CharField(max_length=15)


# Model Model
class Model(models.Model):
	name = models.CharField(max_length=100)
