from django.contrib import admin

from .models import Customer, Chef

class CustomerAdmin(admin.ModelAdmin):
   model = Customer 

admin.site.register(Customer, CustomerAdmin)

class ChefAdmin(admin.ModelAdmin):
   model = Chef

admin.site.register(Chef, ChefAdmin)
