from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import redirect
from auto.models import *
from forms.supplier_form import SupplierForm
from .views import admin_error
from django.db import connection

# Used to display the list of suppliers.
def supplier_list(requests):
	query_string = "SELECT * FROM auto_supplier"

	try:
		result_list = Supplier.objects.raw(query_string)
		paginator = Paginator(result_list, 27)

		page = requests.GET.get('page')
		results = paginator.get_page(page)

		print(result_list)

		if len(result_list) > 0:

			return render(requests, 'supplier_list.html', {'suppliers': results, 'supplier_tab': 'active'})
		else:
			return render(requests, 'supplier_list.html', {'suppliers': results, 'supplier_tab': 'active', 'error': "No suppliers found."})

	except Supplier.DoesNotExist:
		return render(requests, 'error.html', 'Oops...Something went wrong with your search.')


def supplier_search(requests):

	if requests.method == 'GET':
		search_id = requests.GET.get('supplier_search')
		print('Search_ID = %s' % search_id)

		# Remove dashes from the search_id
		search_id = search_id.replace('-', '')

		# Remove trailing spaces.
		search_id = search_id.strip(' ')

		try:
			query_string = 'SELECT * FROM auto_supplier WHERE name LIKE "%" %s "%" OR city LIKE "%" %s "%" OR ' \
						   'state LIKE "%" %s "%" OR phone LIKE "%" %s "%"'
			results_list = Supplier.objects.raw(query_string, [search_id, search_id, search_id, search_id])

			paginator = Paginator(results_list, 15)

			page = requests.GET.get('page')
			results = paginator.get_page(page)

			print(results)
			if len(results_list) > 0:
				return render(requests, 'supplier_list.html', {'suppliers': results, 'supplier_tab': 'active'})
			else:
				return render(requests, 'supplier_list.html', {'supplier_tab': 'active', 'error': 'No suppliers found.'})
		except Supplier.DoesNotExist:
			return render(requests, 'supplier_list.html', {'error': 'No suppliers found.'})


def supplier_new(requests):
	insert_query_string = 'INSERT INTO auto_supplier (name, address1, address2, city, state, zip, phone) ' \
						  'VALUES (%s, %s, %s, %s, %s, %s, %s)'
	try:
		if requests.method == 'POST':
			form = SupplierForm(requests.POST)
			print("Supplier_new: I got this far ... creating a new supplier")

			if form.is_valid():

				# Get the user altered data from the form.
				name = form.cleaned_data['name']
				address1 = form.cleaned_data['address1']
				address2 = form.cleaned_data['address2']
				city = form.cleaned_data['city']
				state = form.cleaned_data['state']
				zip = form.cleaned_data['zip']
				phone = form.cleaned_data['phone']

				# Execute the insert query
				with connection.cursor() as cursor:
					cursor.execute(insert_query_string, [name,
														 address1,
														 address2,
														 city,
														 state,
														 zip,
														 phone])
				return redirect('supplier_list')
		else:
			form = SupplierForm()
			return render(requests, 'supplier_edit.html', {'form': form, 'supplier_tab': 'active'})

	except Supplier.DoesNotExist:
		return admin_error(requests, 'Oops...something went wrong.')


def supplier_edit(requests, supplier_id):

	try:
		select_query_string = "SELECT * FROM auto_supplier WHERE id = %s"
		update_query_string = "UPDATE auto_supplier SET name = %s, address1 = %s, address2 = %s, " \
							  			"city = %s, state = %s, zip = %s, phone = %s " \
							  "WHERE id = %s"

		if requests.method == 'POST':
			form = SupplierForm(requests.POST)
			print("Supplier_edit: I got this far ... editing and existing supplier.")

			if form.is_valid():

				# Get the user altered data from the form.
				name = form.cleaned_data['name']
				address1 = form.cleaned_data['address1']
				address2 = form.cleaned_data['address2']
				city = form.cleaned_data['city']
				state = form.cleaned_data['state']
				zip = form.cleaned_data['zip']
				phone = form.cleaned_data['phone']

				# Execute the update query
				with connection.cursor() as cursor:
					cursor.execute(update_query_string, [name,
														 address1,
														 address2,
														 city,
														 state,
														 zip,
														 phone,
														 supplier_id])

				# Redirect the user to the supplier list.
				return redirect('supplier_list')

		else:

			# Retrieve the suppliers from the database using SQL.
			suppliers = Supplier.objects.raw(select_query_string, [supplier_id])

			# Convert the raw query to a dictionary object.
			suppliers = [dict(s.__dict__) for s in suppliers]

			# For debugging purposes print out the supplier.
			print(suppliers[0])

			# Bind the form to the data.
			form = SupplierForm(suppliers[0])

			# Render the data on the form.
			return render(requests, 'supplier_edit.html', {'form': form, 'supplier_tab': 'active'})
	except:
		return admin_error(requests, 'Oops...Something went wrong...')