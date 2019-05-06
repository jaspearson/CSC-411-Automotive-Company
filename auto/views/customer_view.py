from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import redirect
from auto.models import *
from forms.customer_edit_form import CustomerEditForm
from .views import error
from django.db import connection




def customer_list(requests):

	try:

		result_list = Customer.objects.order_by('last_name')
		paginator = Paginator(result_list, 27)	# Show 27 customers per page.

		page = requests.GET.get('page')
		results = paginator.get_page(page)

		if result_list.exists():
			return render(requests, 'customer_list.html', {'customers': results, 'customer_list': "active"})
		else:
			return render(requests, 'customer_list.html', {'error':'No customers found'})

	except Customer.DoesNotExist:

		return render(requests, 'customer_list.html', {'error': 'Oops...Something went wrong with your search.', 'customer_list': 'active'})

# Customer_search function used to search for customers by name, email, or phone.
def customer_search(requests):

	if requests.method == 'GET':
		search_id = requests.GET.get('customer_search')
		print("Search_ID = %s" % (search_id))

		# Remove parenthisis and dashes from the search_id.
		search_id = search_id.replace('-', '')

		#Remove leading and trailing spaces.
		search_id = search_id.strip(' ')

		try:
			query_string = 'SELECT * FROM auto_customer WHERE first_name LIKE "%"%s"%" OR last_name LIKE "%"%s"%" OR email LIKE "%"%s"%" OR phone LIKE "%"%s"%"'

			# Determine if more than one word is being searched for.
			full_name_array = search_id.split(" ")
			if len(full_name_array) > 1:
				print ("Customer Search: Multiple words were searched for.")
				query_string = 'SELECT * FROM auto_customer WHERE first_name LIKE "%"%s"%" AND last_name LIKE "%"%s"%" OR email LIKE "%"%s"%" OR phone LIKE "%"%s"%"'
				first_name = full_name_array[0]
				last_name = full_name_array[1]
				result_list = Customer.objects.raw(query_string, [first_name, last_name, search_id, search_id])
			else:
				result_list = Customer.objects.raw(query_string, [search_id, search_id, search_id, search_id])

			paginator = Paginator(result_list, 27)

			page = requests.GET.get('page')
			results = paginator.get_page(page)

			if len(result_list) > 0:
				# print("i got to Customer search result_list > 0")
				return render(requests, 'customer_list.html', {'customers': results, 'customer_list': 'active'})
			else:
				# print("i got to Customer search else")
				return render(requests, 'customer_list.html', {'error': 'No customers found', 'customer_list': 'active'})

		except Customer.DoesNotExist:
			# print("i got to Customer.DoesNotExist")
			return render(requests, 'customer_list.html', {'error': 'Oops...Something went wrong with your search.', 'customer_list': 'active'})


# Used to edit existing customers.
# jaspearson
def customer_edit(requests, userid):
	select_query_string = "SELECT * from auto_customer WHERE id = %s"
	update_query_string = "Update auto_customer SET first_name = %s, last_name = %s, DOB = %s, address1 = %s, address2 =%s," \
						  " city = %s, state = %s, zip = %s, email = %s, phone = %s, gender = %s, annual_income = %s " \
						  "WHERE id = %s"

	if requests.method == 'POST':
		form = CustomerEditForm(requests.POST)
		print("customer_edit: I got this far...editing an existing customer")

		if form.is_valid():

			# Get the cleaned data from the form.
			data_list = form.get_data_list()

			# Append the userid to the data list.
			data_list.append(userid)

			# Execute the update Query.
			with connection.cursor() as cursor:
				cursor.execute(update_query_string, data_list)

			# Redirect the user to the customer list.
			return redirect('customer_list')

	else:

		# Retrieve from the database using SQL
		customer = Customer.objects.raw(select_query_string, [userid])

		# Retrieve from database using models.
		# customer = Customer.objects.filter(id=userid).defer("updated", "DOB").values()

		# Convert the raw query set to a dictionary object.
		customer = [dict(c.__dict__) for c in customer]

		# For Debugging purposes print out the customer
		print(customer[0])

		# Bind the form to the data
		form = CustomerEditForm(customer[0])

		# Render the data on the form.
		return render(requests, 'customer_edit.html', {'form': form})

# Used to edit create new customers.
# jaspearson
def customer_new(requests):
	insert_query_string = 'INSERT INTO auto_customer (first_name, last_name, DOB, address1, address2, city, state, zip,' \
						  ' email, phone, gender, annual_income) ' \
						  'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

	if requests.method == 'POST':
		form = CustomerEditForm(requests.POST)
		print("customer_edit: I got this far...creating a new customer.")

		if form.is_valid():

			# Get the cleaned data from the form.
			data_list = form.get_data_list()

			print(data_list)
			# Execute the update Query.
			with connection.cursor() as cursor:
				cursor.execute(insert_query_string, data_list)
			return redirect('customer_list')

	else:
		form = CustomerEditForm()
		return render(requests, 'customer_edit.html', {'form': form})
