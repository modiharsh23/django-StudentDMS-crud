from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    course = models.CharField(max_length=100)
    year = models.CharField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)