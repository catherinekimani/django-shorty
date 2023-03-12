import string
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import URL

def index(request):
    """
    Render the index.html template for the shortener app.

    Args:
        request: HttpRequest object representing the current request.

    Returns:
        A rendered HTML response with the index.html template.
    """
    return render(request, 'shortener/index.html')


def create_short_url(request):
    """
    Create a new shortened URL and return it as a response.

    Args:
        request: HttpRequest object representing the current request.

    Returns:
        An HttpResponse object with the shortened URL.
    """
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        url = URL.objects.filter(original_url=original_url).first()
        if not url:
            # generate a random string of length 8
            chars = string.ascii_lowercase + string.digits
            shortened_url = ''.join(random.choice(chars) for _ in range(8))
            url = URL(original_url=original_url, shortened_url=shortened_url)
            url.save()
        shortened_url = "http://" + request.get_host() + "/" + url.shortened_url
        return render(request, 'shortener/index.html', {'shortened_url': shortened_url})
    return redirect('/')


def redirect_original(request, shortened_url):
    """
    Redirect to the original URL for a given shortened URL.

    Args:
        request: HttpRequest object representing the current request.
        shortened_url: The shortened URL to redirect to the original URL.

    Returns:
        A redirect response to the original URL for the given shortened URL.
    """
    url = URL.objects.get(shortened_url=shortened_url)
    return redirect(url.original_url)
