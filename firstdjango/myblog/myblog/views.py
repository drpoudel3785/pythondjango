# filename: views.py (Django view functions)

from django.http import HttpResponse
from django.shortcuts import render
from .models import Team

def index(request):
    # Get an HttpRequest - the request parameter
    # perform operations using information from the request.
    # Return HttpResponse
    return HttpResponse('Hello from Django!')