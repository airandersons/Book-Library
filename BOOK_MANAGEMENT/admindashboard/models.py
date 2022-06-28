from django.db import models
from django.utils import timezone
import datetime

class Book(models.Model):
    title = models.CharField('Book title',max_length=50)
    author = models.CharField('Book Author',max_length=50)
    pub_date = models.DateField('Publication date',auto_now_add=True)
    category = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    avail_status = models.CharField('Availability status',max_length=13, default='Available')

    def __str__(self):
        return self.title

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Notifications(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.message

class BookRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    req_date = models.DateField('Date of book request', null=True, blank=True)
    #return_date = req_date + datetime.timedelta(days=8) 
    book_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.book_id

class Fines(models.Model):
    book_id = models.IntegerField()
    student_id = models.IntegerField()
    actual_return_date = models.DateField()
    extra_days = models.IntegerField()
    fine = models.IntegerField()
    
        
    
