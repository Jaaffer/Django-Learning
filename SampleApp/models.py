from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField()

class File(models.Model):
    file = models.FileField()
    
    def __str__(self):
        return str(self.file)