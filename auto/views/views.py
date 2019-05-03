from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import redirect


# Handle the landing page requests.
def index(requests):
	return render(requests, 'index.html', {})


def auto_admin(requests):
	return render(requests, 'admin_index.html', {})


# Handle errors page.
def error(requests, error):
	return render(requests, 'error.html', {'error': error})

