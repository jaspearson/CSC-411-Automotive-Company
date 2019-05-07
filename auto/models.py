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
	image = models.ImageField(upload_to='customer_pic', blank=True)
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


# Top Brands by Amount
class TopBrandsByAmount(models.Model):
	brand = models.CharField(max_length=45, primary_key=True)
	sales_amount = models.IntegerField()


# Convertible Sales
class ConvertibleSaleMonth(models.Model):
	Month = models.DateField(primary_key=True)
	Count = models.IntegerField()

	class Meta:
		managed=False
		db_table = 'auto_sales_convertible_view'


# Dealer Aging
class DealerAging(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100)
	average_days = models.IntegerField()

	class Meta:
		managed = False
		db_table = 'auto_sales_dealer_aging_view'

# Sales Trend by year
class TrendYearView(models.Model):
	brand = models.CharField(max_length=100, primary_key=True)
	theyear = models.IntegerField()
	total = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		managed = False
		db_table = 'auto_trend_year_view'


# Sales Trend by month
class TrendMonthView(models.Model):
	brand = models.CharField(max_length=100, primary_key=True)
	month = models.IntegerField()
	total = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		managed = False
		db_table = 'auto_trend_month_view'


# Sales Trend by month
class TrendWeekView(models.Model):
	brand = models.CharField(max_length=100, primary_key=True)
	week = models.IntegerField()
	total = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		managed = False
		db_table = 'auto_trend_week_view'


# Sales Trend Gender Income
class TrendGenderIncomeView(models.Model):
	brand = models.CharField(max_length=100, primary_key=True)
	week = models.IntegerField()
	total = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		managed = False
		db_table = 'auto_trend_gender_income_view'


# States Model
class State(models.Model):

	name = models.CharField(max_length=45)
	abbreviation = models.CharField(max_length=2, primary_key=True)


# Annual Income Model
class cust_income_range(models.Model):
	id = models.IntegerField(primary_key=True)
	range = models.CharField(max_length=50)

	def __str__(self):
		return self.range






