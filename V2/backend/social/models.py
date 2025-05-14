from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    about = models.TextField()
    avatar = models.TextField(null=True, blank=True)
    privacy = models.CharField(max_length=10)

class Follow(models.Model):
    username = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    target = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    creator = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    content = models.TextField()
    creator = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

class Group(models.Model):
    individual = models.CharField(max_length=50)
    affiliation = models.CharField(max_length=50)

class Message(models.Model):
    speaker = models.CharField(max_length=50)
    content = models.TextField()
    listener = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
