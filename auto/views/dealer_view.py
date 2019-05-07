from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import redirect
from auto.models import *
from forms.dealers_form import DealerForm
from .views import error
from django.db import connection


# Used to display the list of dealers
def dealer_list(requests):
	query_string = "SELECT * from auto_dealer"

	try:
		result_list = Dealer.objects.raw(query_string)
		paginator = Paginator(result_list, 27)

		page = requests.GET.get('page')
		results = paginator.get_page(page)

		if len(result_list) > 0:
			return render(requests,'dealer_list.html', {'dealers': results, 'dealer': 'active'})
		else:
			return render(requests, 'error.html', 'No dealers found')

	except Dealer.DoesNotExist:

		return render(requests, 'error.html', 'Oops...Something went wrong with your search.')


def dealer_search(requests):

	if requests.method == 'GET':
		search_id = requests.GET.get('dealer_search')
		print('Search_ID = %s' % search_id)

		# Remove dashes from the search_id
		search_id = search_id.replace('-', '')

		# Remove trailing spaces.
		search_id = search_id.strip(' ')

		try:
			query_string = "SELECT * FROM auto_dealer WHERE name LIKE  '%' %s '%' OR city LIKE '%' %s '%' OR state LIKE '%' %s '%'" \
						   "OR phone LIKE '%' %s '%'"
			result_list = Dealer.objects.raw(query_string, [search_id, search_id, search_id, search_id])

			paginator = Paginator(result_list, 27)

			page = requests.GET.get('page')
			results = paginator.get_page(page)

			if len(result_list) > 0:
				return render(requests, 'dealer_list.html', {'dealers': results, 'dealer': 'active'})
			else:
				return render(requests, 'dealer_list.html', {'error': 'No dealers found.', 'dealer': 'active'})
		except Dealer.DoesNotExist:
			return error(requests, 'Oops...Something went wrong with your search.')


def dealer_new(requests):
	insert_query_string = 'INSERT INTO auto_dealer (name, address1, address2, city, state, zip, phone) ' \
						  'VALUES (%s, %s, %s, %s, %s, %s, %s)'
	try:
		if requests.method == 'POST':
			form = DealerForm(requests.POST)
			print("Dealer_edit: I got this far ... creating a new dealer.")

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
					cursor.execute(insert_query_string, [name, address1, address2, city, state, zip, phone])

				return redirect('dealer_list')
		else:
			form = DealerForm()
			return render(requests, 'customer_edit.html', {'form': form, 'dealer': 'active'})
	except Dealer.DoesNotExist:
		return error(requests, 'Oops...something went wrong.')

def dealer_edit(requests, dealer_id):

	try:
		select_query_string = "SELECT * FROM auto_dealer WHERE id = %s"
		update_query_string = "UPDATE auto_dealer SET name = %s, address1 = %s, address2 = %s, city = %s, state = %s, zip = %s," \
							  "phone = %s " \
							  "WHERE id = %s"

		if requests.method == 'POST':
			form = DealerForm(requests.POST)
			print("Dealers_edit: I got this far... editing an existing dealer.")

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
					cursor.execute(update_query_string, [name, address1, address2, city, state, zip, phone, dealer_id])

				# Redirect the user to the dealers list.
				return redirect('dealer_list')

		else:

			# Retrieve dealer from the database using SQL
			dealer = Dealer.objects.raw(select_query_string, [dealer_id])

			# Convert the raw query set to a dictionary object
			dealer = [dict(d.__dict__) for d in dealer]

			# For debugging purposes print out the dealer
			print(dealer[0])

			# Bind the form to the data
			form = DealerForm(dealer[0])

			# Render the data on the form.
			return render(requests, 'dealer_edit.html', {'form': form, 'dealer': 'active'})

	except:
		return error(requests, 'Oops...Something went wrong ...')
