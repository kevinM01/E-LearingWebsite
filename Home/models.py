from django.db import models
from django.db.models import When


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
    name = models.CharField(max_length=300, default='')
    email = models.CharField(max_length=300, default='')
    phone = models.CharField(max_length=300, default='')
    desc = models.CharField(max_length=300, default='')


class faculty(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


# class Post(models.Model):
#     user = models.ForeignKey(faculty, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     file_field = models.FileField(upload_to='static/')
#     desc = models.TextField()
#
#     def __str__(self):
#         return f'{self.user}=> {self.title}'

class Upload_Files(models.Model):
    topic_name = models.CharField(max_length=200)
    notes_file = models.FileField(upload_to="Material/")
    # When: object



    # if topic_name == "Python" or "python":
    #     video_file = models.FileField(upload_to="Material/Python")
    #     notes_file = models.FileField(upload_to="Material/Python")
    # else:
    #     print('tk')
    #
    # if topic_name == "Javascript" or "javascript":
    #     video_file = models.FileField(upload_to="Material/Javascript")
    #     notes_file = models.FileField(upload_to="Material/Javascript")
    # else:
    #     print('t')

    # if topic_name == "machine learning" or "ML":
    #     video_file = models.FileField(upload_to="Material/Machine Learning")
    #     notes_file = models.FileField(upload_to="Material/Machine Learning")
    # else:
    #     print('ka')
    #
    # if topic_name == "Java" or "java":
    #     video_file = models.FileField(upload_to="Material/Java")
    #     notes_file = models.FileField(upload_to="Material/java")
    # else:
    #     print('a')
    #
    # if topic_name == "Android" or "android":
    #     video_file = models.FileField(upload_to="Material/Android")
    #     notes_file = models.FileField(upload_to="Material/Android")
    # else:
    #     print('Dk')
    #
    # if topic_name == "web dev" or "Web Dev":
    #     video_file = models.FileField(upload_to="Material/Web Dev")
    #     notes_file = models.FileField(upload_to="Material/Web Dev")
    # else:
    #     print('r')
    # video_file = models.FileField(upload_to="Material/")
    # notes_file = models.FileField(upload_to="Material/")
