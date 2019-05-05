from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import redirect
from auto.models import *
from forms.model_form import cModelForm
from .views import error
from django.db import connection

# Used to display the list of sales.
def sale_list(requests):
	query_string = "SELECT * FROM auto_sales_view order by sale_date desc "

	try:
		result_list = SaleView.objects.raw(query_string)

		paginator = Paginator(result_list, 27)

		page = requests.GET.get('page')
		results = paginator.get_page(page)

		print(result_list)

		if len(result_list) > 0:

			return render(requests, 'sale_list.html', {'sales': results, 'sale_tab': 'active'})
		else:
			return render(requests, 'sale_list.html', {'sales': results, 'sale_tab': 'active', 'error': "No sales found."})

	except SaleView.DoesNotExist:
		return render(requests, 'error.html', 'Oops...Something went wrong with your search.')

def sale_search(requests):

	if requests.method == 'GET':
		search_id = requests.GET.get('sale_search')
		print('Search_ID = %s' % search_id)

		# Remove dashes from the search_id
		search_id = search_id.replace('-', '')

		# Remove trailing spaces.
		search_id = search_id.strip(' ')

		try:
			query_string = 'SELECT * FROM auto_sales_view WHERE vin LIKE "%" %s "%" OR model_name LIKE "%" %s "%" OR ' \
						   'first_name LIKE "%" %s "%" OR last_name LIKE "%" %s "%"'
			results_list = SaleView.objects.raw(query_string, [search_id, search_id, search_id, search_id])

			paginator = Paginator(results_list, 15)

			page = requests.GET.get('page')
			results = paginator.get_page(page)

			print(results)
			if len(results_list) > 0:
				return render(requests, 'sale_list.html', {'sales': results, 'sale_tab': 'active'})
			else:
				return render(requests, 'sale_list.html', {'sale_tab': 'active', 'error': 'No sales found.'})
		except SaleView.DoesNotExist:
			return render(requests, 'sale_list.html', {'error': 'No sales found.'})

def sale_new(requests):
	insert_query_string = 'INSERT INTO auto_sale (name, address1, address2, city, state, zip, phone) ' \
						  'VALUES (%s, %s, %s, %s, %s, %s, %s)'
	try:
		if requests.method == 'POST':
			form = saleForm(requests.POST)
			print("sale_new: I got this far ... creating a new sale")

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
				return redirect('sale_list')
		else:
			form = saleForm()
			return render(requests, 'sale_edit.html', {'form': form, 'sale_tab': 'active'})

	except sale.DoesNotExist:
		return admin_error(requests, 'Oops...something went wrong.')