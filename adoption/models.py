# adoption/models.py
from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='animal_images/', blank=True, null=True)  # Add this field

   


    def __str__(self):
        return self.name

    class Meta:
        app_label = 'adoption'  # Specify the app_label for the model
