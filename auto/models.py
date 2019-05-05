from django.db import models

# Create your models here.


# Customers Model
class Customer(models.Model):
	id = models.IntegerField(primary_key=True)
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
class cModel(models.Model):
	name = models.CharField(max_length=100)
	base_price = models.DecimalField(max_digits=10, decimal_places=2)
	est_miles_per_gallon = models.IntegerField()
	body_style = models.CharField(max_length=45)
	year = models.IntegerField()
	color = models.CharField(max_length=45)
	engine = models.CharField(max_length=45)
	transmission = models.CharField(max_length=45)
	brand = models.CharField(max_length=45)

# Supplier Model
class Supplier(models.Model):
	name = models.CharField(max_length=100)
	address1 = models.CharField(max_length=100)
	address2 = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=2)
	zip = models.CharField(max_length=5)
	phone = models.CharField(max_length=15)

# Manufacturer Model
class Manufacturer(models.Model):
	name = models.CharField(max_length=100)
	address1 = models.CharField(max_length=100)
	address2 = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=2)
	zip = models.CharField(max_length=5)
	phone = models.CharField(max_length=15)


# Sale Model
class SaleView(models.Model):
	vin = models.CharField(max_length=14, primary_key=True)
	model_name = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	sale_price = models.DecimalField(max_digits=10, decimal_places=2)
	sale_date = models.DateField()

	class Meta:
		managed = False
		db_table = "auto_sales_view"

# Reports Models
# Top Brands by Sales Counts
class TopBrandsByCount(models.Model):
	brand = models.CharField(max_length=45, primary_key=True)
	sales_count = models.IntegerField()

class TopBrandsByAmount(models.Model):
	brand = models.CharField(max_length=45, primary_key=True)
	sales_amount = models.IntegerField()

# States Model
class State(models.Model):

	name = models.CharField(max_length=45)
	abbreviation = models.CharField(max_length=2, primary_key=True)


