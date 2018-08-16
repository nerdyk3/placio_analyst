from django.contrib import admin

# Register your models here.
from .models import csvimport,graph_axis

admin.site.register(csvimport)
admin.site.register(graph_axis)
