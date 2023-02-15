from django.db import models

# Create your models here.
class Student(models.Model):
    GENDERCHOICE = (
        ('male', 'male'),
        ('female','female'),
    )
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    gender = models.CharField(max_length=10, choices=GENDERCHOICE)
    