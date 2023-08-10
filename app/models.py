from django.db import models
from django.urls import reverse

# Create your models here.

class School(models.Model):
    scname=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    slocation=models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.scname
    
    def get_absolute_url(self):
        return reverse('details',kwargs={'pk':self.pk})
    

    

class Student(models.Model):
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()
    scname=models.ForeignKey(School,on_delete=models.CASCADE, related_name= 'RAHUL')


    def __str__(self) -> str:
        return self.sname
    

    