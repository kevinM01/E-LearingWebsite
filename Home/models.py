from django.db import models


# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=300, unique=True)
    password = models.TextField(default='abc123')
    cpassword = models.TextField(default='abc123')
    email = models.TextField()
    firstname = models.TextField(default='asc')
    phone = models.TextField(default='123')

class Contact(models.Model):
    msgid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300,default='')
    email = models.CharField(max_length=300,default='')
    phone = models.CharField(max_length=300,default='')
    desc = models.CharField(max_length=300,default='')
