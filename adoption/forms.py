# adoption/forms.py
from django import forms
from .models import Animal

class AnimalAdoptionForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'species', 'age', 'description','image']
