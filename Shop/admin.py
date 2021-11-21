
from django.contrib import admin
from .models import Shop

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)} 

class showdateAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
admin.site.register(Shop, showdateAdmin)