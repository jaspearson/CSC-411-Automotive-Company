from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Handle the landing page requests.
def index(requests):
	return render(requests, 'index.html', {})


def auto_admin(requests):
	return render(requests, 'admin_index.html', {})

def customer_list(requests):

	try:

		result_list = Customer.objects.order_by('last_name')
		paginator = Paginator(result_list, 27)	# Show 27 customers per page.

		page = requests.GET.get('page')
		results = paginator.get_page(page)

		if result_list.exists():
			return render(requests, 'customer_list.html', {'customers': results, 'customer_list': "active"})
		else:
			return render(requests, 'error.html', 'No customers found')

	except Customer.DoesNotExist:

		return render(requests, 'error.html', 'Oops...Something went wrong with your search.')


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
				return error(requests, 'No customers found')

		except Customer.DoesNotExist:
			# print("i got to Customer.DoesNotExist")
			return error(requests, 'Oops...Something went wrong with your search.')


# Handle errors page.
def error(requests, error):
	return render(requests, 'error.html', {'error': error})

