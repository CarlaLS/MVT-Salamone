from django.db import models

# Create your models here.
class Person (models.Model):
    name= models.CharField(max_length=255)
    surname= models.CharField(max_length=255)
    age= models.IntegerField()
  

    def __str__(self):
        return f'{self.name} {self.surname}'