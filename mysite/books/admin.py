from django.contrib import admin

from models import Book
# Register your models here.

# I needed to add this line so Book table shows up on admin site
admin.site.register(Book)