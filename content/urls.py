from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('publications/', views.publications, name='publications'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('talks/', views.talks, name='talks'),
    path('events/', views.events, name='events'),
]
