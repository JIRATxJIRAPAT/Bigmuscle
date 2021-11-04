from django.contrib import admin
from .models import Exercise,Workout,Program
# Register your models here.
admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(Program)