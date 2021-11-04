from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(Day_Program)
admin.site.register(Tracks)
