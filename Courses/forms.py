from django import forms
from django.db import models
from .models import *


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('trainer', 'date', 'timeslot', 'customer',)
    

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'info', 'teach', 'days', 'pic', ]
