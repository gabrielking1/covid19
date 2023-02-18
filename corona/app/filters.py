
import django_filters
from app.models import *
from django import forms


class CountryFilter(django_filters.FilterSet):
    # level = django_filters.MultipleChoiceFilter(choices=Student.LevelChoices.choices,
    # widget = forms.CheckboxSelectMultiple)
    class Meta:
        model = Country
        
        fields = {
            'country' : ['icontains'],
            #'year' : ['exact'],
            #'level' :['exact'],
            #'department' :['exact']
        }