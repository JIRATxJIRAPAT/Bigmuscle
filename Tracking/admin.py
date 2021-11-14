from django.contrib import admin
from .models import Exercise,Workout,Program,Tracks
# Register your models here.
class showdateProgramAdmin(admin.ModelAdmin):
    readonly_fields = ('start_date','end_date',)

class showdateTrackAdmin(admin.ModelAdmin):
    readonly_fields = ('start_date',)

admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(Program,showdateProgramAdmin)
admin.site.register(Tracks,showdateTrackAdmin)