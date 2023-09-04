from django.contrib import admin
from .models.products import Products
from .models.category import Category
from .models.customer import  Customer
from .models.orders import  Order

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

class AdminCustomer(admin.ModelAdmin):
    list_display=['first_name','last_name','phone','email','password']
    
admin.site.register(Products, AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Order)
