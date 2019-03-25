from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse


# Handle the landing page requests.
def index(requests):
	return render(requests, 'index.html', {})


# Handle errors page.
def error(requests, error):
	return render(requests, 'error.html', {'error': error})

