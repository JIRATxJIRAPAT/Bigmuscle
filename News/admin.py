
from django.contrib import admin
from .models import News

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)} 


admin.site.register(News, PostAdmin)