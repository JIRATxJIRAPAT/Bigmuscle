from django.contrib import admin

# Register your models here.

from .models import Customer,Trainer

admin.site.register(Customer)
admin.site.register(Trainer)
