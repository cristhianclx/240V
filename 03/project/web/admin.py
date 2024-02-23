from django.contrib import admin
from .models import Document, DocumentMatch


admin.site.register(Document)
admin.site.register(DocumentMatch)