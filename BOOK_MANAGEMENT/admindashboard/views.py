from django.shortcuts import render
from .models import Book
from . forms import BookForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def home(request):
    context = {1: 'hi'}
    return render(request, 'admindashboard/index.html', context)

def addbook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']

            book = Book(title=title, author=author, category=category, description=description)
            book.save()
            
            return HttpResponseRedirect('New book added to list')
    else:
        form = BookForm()
    return render(request, 'admindashboard/addbook.html', {'form': form})