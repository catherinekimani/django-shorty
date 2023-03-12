"""
This module defines the URL view for the URL shortify app.
"""
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import URL


def index(request):
    """
    Render the index.html template for the shortify app.

    Args:
        request: HttpRequest object representing the current request.

    Returns:
        A rendered HTML response with the index.html template.
    """
    return render(request, 'shortener/index.html')