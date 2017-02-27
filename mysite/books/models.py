from __future__ import unicode_literals

from django.db import models

# Create your models here.

#book table
# python.exe .\manage.py makemigrations books
# python.exe .\manage.py sqlmigrate books 0001
# python.exe .\manage.py migrate
# for shell access python.exe .\manage.py migrate
class Book(models.Model):
    
    def __str__(self):
        return self.name + '-' + self.author
    
    #field definitions
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    
