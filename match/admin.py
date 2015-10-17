from django.contrib import admin

from .models import Customer, Chef

class CustomerAdmin(admin.ModelAdmin):
   model = Customer 

class ChefAdmin(admin.ModelAdmin):
   model = Chef
