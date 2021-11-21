from django import forms
from django.db import models
from .models import *


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('trainer', 'date', 'timeslot', 'customer',)
    

class CreateCourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'info', 'teach', 'days', 'pic', ]
class CourseForm(forms.ModelForm):
    name = forms.CharField(label='test',widget=forms.Textarea(attrs={
            'rows': '1',
            'placeholder': 'Say Something...'
            }))
    class Meta:
        model = Course
        fields = ['name', 'info', 'teach', 'days', 'pic', ]
