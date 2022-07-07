from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import get_user_mode

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    borrower_id = models.CharField(max_length=100,null=True,blank=True)
    Uploaded = models.DateTimeField(auto_now=True)
    Due_date = models.DateTimeField(auto_now=True)
    books= models.FileField(upload_to='BOOK_MANAGEMENT/books/')
    bookcover=models.ImageField(upload_to='BOOK_MANAGEMENT/books/covers')
    def __str__(self):
        return self.title 
     