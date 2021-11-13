from django.contrib import admin

# Register your models here.

from .models import Customer,Report
class showdateAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


admin.site.register(Customer)
admin.site.register(Report,showdateAdmin)

