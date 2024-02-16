from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Employees)

admin.site.register(Customer)

admin.site.register(Products)

admin.site.register(Category)

admin.site.register(Supplier)

admin.site.register(Stock)
