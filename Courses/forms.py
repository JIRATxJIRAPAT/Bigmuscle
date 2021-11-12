from django import forms
from django.db import models
from .models import Appointment
from datetime import date
class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('trainer', 'date', 'timeslot', 'customer',)
    
