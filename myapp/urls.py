from django.urls import path

from myapp import views

urlpattern=[
    path('',views.index, name='index'),
]