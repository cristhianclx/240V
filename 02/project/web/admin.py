from django.contrib import admin
from .models import Author, Book, Edition


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Edition)