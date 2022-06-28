from django.urls import path

from . import views

app_name = 'admindashboard'
urlpatterns = [
    path('', views.home, name='home'),
    path('addbook/', views.addbook, name="addbook"),
]
