from django.shortcuts import render

def home(request):
    context = {1: 'hi'}
    return render(request, 'admindashboard/index.html', context)