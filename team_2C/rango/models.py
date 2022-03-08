from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    username = models.ForeignKey(User)
    isbn = models.CharField(max_length=13, unique = True)
    bookPicture = models.ImageField()
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=1000)
    author = models.CharField(max_Length=50)
    publisher = models.CharField(max_Length=50)
    price = models.IntegerField(default=0)
    language = models.Charfield(max_Length=50)

class Review(models.Model):
    username = models.ForeignKey(User, on_delete=CASCADE)
    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(default= 0)
    comment = models.TextField(max_length=1000)
    publishDate = models.DateField()
    genre = models.CharField(max_length= 50)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)    

class User(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #not sure if we even need the username and password fields
    #cos the tango project doesit differently
    #username = models.CharField(max_length=30, unique = True)
    #password = models.CharField(max_length=30)
    userPicture = models.ImageField(blank = True)
    joinDate = models.DateField()

    def __str__(self):
        return self.user.username