from django.urls import path

from myapp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('counter/',views.counter, name='counter'),
    path('register/',views.register, name='register'),
]