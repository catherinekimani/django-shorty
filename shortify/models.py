"""
This module defines the URL model for the URL shortener app.
"""
from django.db import models
# Create your models here.


class URL(models.Model):
    """
    Represents a URL and its shortened version.
    Attributes:
        original_url (str): The original URL that is being shortened.
        shortened_url (str): The shortened version of the URL.
    """
    original_url = models.CharField(max_length=200)
    shortened_url = models.CharField(max_length=20, unique=True)
    def __str__(self):

        return f'{self.original_url} to {self.shortened_url}'
