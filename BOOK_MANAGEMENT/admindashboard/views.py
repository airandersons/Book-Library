from django.shortcuts import render

def home(request):
    context = {1: 'hi'}
    return render(request, 'admindashboard/index.html', context)

def addbook(request):
    context = {2: 2}
    return render(request, 'admindashboard/addbook.html', context)