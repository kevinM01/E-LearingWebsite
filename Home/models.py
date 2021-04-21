from django.db import models


# Create your models here.
# class Student(models.Model):
#     username = models.CharField(max_length=300, unique=True)
#     password = models.TextField(default='abc123')
#     cpassword = models.TextField(default='abc123')
#     email = models.TextField()
#     firstname = models.TextField(default='asc')
#     lastname = models.TextField(default='asc')

class Contact(models.Model):
    msgid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300,default='')
    email = models.CharField(max_length=300,default='')
    phone = models.CharField(max_length=300,default='')
    desc = models.CharField(max_length=300,default='')

class faculty(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Post(models.Model):
    user = models.ForeignKey(faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file_field = models.FileField(upload_to='uploads/')
    desc = models.TextField()

    def __str__(self):
        return f'{self.user}=> {self.title}'


