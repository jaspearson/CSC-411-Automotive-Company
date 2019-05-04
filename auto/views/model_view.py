from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import redirect
from auto.models import *
from forms.model_form import cModelForm
from .views import error
from django.db import connection


# Used to display the list of models.
def model_list(requests):
	query_string = "SELECT * FROM auto_model"

	try:
		result_list = cModel.objects.raw(query_string)
		paginator = Paginator(result_list, 27)

		page = requests.GET.get('page')
		results = paginator.get_page(page)

		print(result_list)

		if len(result_list) > 0:

			return render(requests, 'model_list.html', {'cmodels': results, 'cmodel': 'active'})
		else:
			return error(requests, 'No models found.')

	except cModel.DoesNotExist:
		return render(requests, 'error.html','Oops...Something went wrong with your search.')


def model_search(requests):

	if requests.method == 'GET':
		search_id = requests.GET.get('model_search')
		print('Search_ID = %s' % search_id)

		# Remove dashes from the search_id
		search_id = search_id.replace('-', '')

		# Remove trailing spaces.
		search_id = search_id.strip(' ')

		try:
			query_string = 'SELECT * FROM auto_model WHERE name LIKE "%" %s "%" OR base_price LIKE "%" %s "%"' \
						   'OR est_miles_per_gallon LIKE "%" %s "%" OR body_style LIKE "%" %s "%"' \
						   'OR year LIKE "%" %s "%" OR color LIKE "%" %s "%" OR engine LIKE "%" %s "%" ' \
						   'OR transmission LIKE "%" %s "%" OR brand LIKE "%" %s "%"'
			results_list = cModel.objects.raw(query_string, [search_id, search_id, search_id, search_id, search_id, search_id, search_id, search_id, search_id])

			paginator = Paginator(results_list, 27)

			page = requests.GET.get('page')
			results = paginator.get_page(page)

			#print(results)
			if len(results_list) > 0:
				return render(requests, 'model_list.html', {'cmodels': results, 'cmodel': 'active'})
			else:
				error(requests, 'No models found')
		except cModel.DoesNotExist:
			return error(requests, 'Oops...Something went wrong with your search.')


def model_new(requests):
	insert_query_string = 'INSERT INTO auto_model (name, base_price, est_miles_per_gallon, body_style, year, ' \
						  'color, engine, transmission, brand) ' \
						  'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) '

	try:
		if requests.method == 'POST':
			form = cModelForm(requests.POST)
			print("Model_new: I got this far ... creating a new model")

			if form.is_valid():

				# Get the user altered data from the form.
				name = form.cleaned_data['name']
				base_price = form.cleaned_data['base_price']
				est_miles_per_gallon = form.cleaned_data['est_miles_per_gallon']
				body_style = form.cleaned_data['body_style']
				year = form.cleaned_data['year']
				color = form.cleaned_data['color']
				engine = form.cleaned_data['engine']
				transmission = form.cleaned_data['transmission']
				brand = form.cleaned_data['brand']

				# Execute the insert query
				with connection.cursor() as cursor:
					cursor.execute(insert_query_string, [name,
														 base_price,
														 est_miles_per_gallon,
														 body_style,
														 year,
														 color,
														 engine,
														 transmission,
														 brand])
				return redirect('/model_list/')
		else:
			form = cModelForm()
			return render(requests, 'model_edit.html', {'form': form, 'cmodel': 'active'})

	except cModel.DoesNotExist:
		return error(requests, 'Oops...something went wrong.')

	#return render(requests, 'model_list.html', {'cmodels': results, 'cmodel': 'active'})

def model_edit(requests, model_id):

	try:
		select_query_string = "SELECT * FROM auto_model WHERE id = %s"
		update_query_string = "UPDATE auto_model SET name = %s, base_price = %s, est_miles_per_gallon = %s, " \
							  "body_style = %s, year = %s, color = %s, engine = %s, transmission = %s,"  \
							  "brand = %s WHERE id = %s"

		if requests.method == 'POST':
			form = cModelForm(requests.POST)
			print("Models_edit: I got this far ... editing and existing model.")

			if form.is_valid():

				# Get the user altered data from the form.
				name = form.cleaned_data['name']
				base_price = form.cleaned_data['base_price']
				est_miles_per_gallon = form.cleaned_data['est_miles_per_gallon']
				body_style = form.cleaned_data['body_style']
				year = form.cleaned_data['year']
				color = form.cleaned_data['color']
				engine = form.cleaned_data['engine']
				transmission = form.cleaned_data['transmission']
				brand = form.cleaned_data['brand']

				# Execute the update query
				with connection.cursor() as cursor:
					cursor.execute(update_query_string, [name, base_price, est_miles_per_gallon, body_style, year, color, engine, transmission, brand, model_id])

				# Redirect the user to the models list.
				return redirect('/model_list')

		else:

			# Retrieve the models from the database using SQL.
			cmodel = cModel.objects.raw(select_query_string, [model_id])

			# Convert the raw query to a dictionary object.
			cmodel = [dict(m.__dict__) for m in cmodel]

			# For debugging purposes print out the model.
			print(cmodel[0])

			# Bind the form to the data.
			form = cModelForm(cmodel[0])

			# Render the data on the form.
			return render(requests, 'model_edit.html', {'form': form, 'cmodel': 'active'})

	except:
		return error(requests, 'Oops...Something went wrong...')

