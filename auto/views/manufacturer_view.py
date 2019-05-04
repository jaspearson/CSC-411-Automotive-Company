from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import redirect
from auto.models import *
from forms.manufacturer_form import ManufacturerForm
from .views import admin_error
from django.db import connection

# Used to display the list of manufacturers.
def manufacturer_list(requests):
	query_string = "SELECT * FROM auto_manufacturer"

	try:
		result_list = Manufacturer.objects.raw(query_string)
		paginator = Paginator(result_list, 27)

		page = requests.GET.get('page')
		results = paginator.get_page(page)

		print(result_list)

		if len(result_list) > 0:

			return render(requests, 'manufacturer_list.html', {'manufacturers': results, 'manufacturer_tab': 'active'})
		else:
			return render(requests, 'manufacturer_list.html', {'manufacturers': results, 'manufacturer_tab': 'active', 'error': "No manufacturers found."})

	except Manufacturer.DoesNotExist:
		return render(requests, 'error.html', 'Oops...Something went wrong with your search.')


def manufacturer_search(requests):

	if requests.method == 'GET':
		search_id = requests.GET.get('manufacturer_search')
		print('Search_ID = %s' % search_id)

		# Remove dashes from the search_id
		search_id = search_id.replace('-', '')

		# Remove trailing spaces.
		search_id = search_id.strip(' ')

		try:
			query_string = 'SELECT * FROM auto_manufacturer WHERE name LIKE "%" %s "%" OR city LIKE "%" %s "%" OR ' \
						   'state LIKE "%" %s "%" OR phone LIKE "%" %s "%"'
			results_list = Manufacturer.objects.raw(query_string, [search_id, search_id, search_id, search_id])

			paginator = Paginator(results_list, 15)

			page = requests.GET.get('page')
			results = paginator.get_page(page)

			print(results)
			if len(results_list) > 0:
				return render(requests, 'manufacturer_list.html', {'manufacturers': results, 'manufacturer_tab': 'active'})
			else:
				return render(requests, 'manufacturer_list.html', {'manufacturer_tab': 'active', 'error': 'No manufacturers found.'})
		except Manufacturer.DoesNotExist:
			return render(requests, 'manufacturer_list.html', {'error': 'No manufacturers found.'})


def manufacturer_new(requests):
	insert_query_string = 'INSERT INTO auto_manufacturer (name, address1, address2, city, state, zip, phone) ' \
						  'VALUES (%s, %s, %s, %s, %s, %s, %s)'
	try:
		if requests.method == 'POST':
			form = ManufacturerForm(requests.POST)
			print("manufacturer_new: I got this far ... creating a new manufacturer")

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
				return redirect('manufacturer_list')
		else:
			form = ManufacturerForm()
			return render(requests, 'manufacturer_edit.html', {'form': form, 'manufacturer_tab': 'active'})

	except Manufacturer.DoesNotExist:
		return admin_error(requests, 'Oops...something went wrong.')


def manufacturer_edit(requests, manufacturer_id):

	try:
		select_query_string = "SELECT * FROM auto_manufacturer WHERE id = %s"
		update_query_string = "UPDATE auto_manufacturer SET name = %s, address1 = %s, address2 = %s, " \
							  			"city = %s, state = %s, zip = %s, phone = %s " \
							  "WHERE id = %s"

		if requests.method == 'POST':
			form = ManufacturerForm(requests.POST)
			print("manufacturer_edit: I got this far ... editing and existing manufacturer.")

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
														 manufacturer_id])

				# Redirect the user to the manufacturer list.
				return redirect('manufacturer_list')

		else:

			# Retrieve the manufacturers from the database using SQL.
			manufacturers = Manufacturer.objects.raw(select_query_string, [manufacturer_id])

			# Convert the raw query to a dictionary object.
			manufacturers = [dict(s.__dict__) for s in manufacturers]

			# For debugging purposes print out the manufacturer.
			print(manufacturers[0])

			# Bind the form to the data.
			form = ManufacturerForm(manufacturers[0])

			# Render the data on the form.
			return render(requests, 'manufacturer_edit.html', {'form': form, 'manufacturer_tab': 'active'})
	except:
		return admin_error(requests, 'Oops...Something went wrong...')