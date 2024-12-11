from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Publication, Event, Talk, Course, HomepageContent


def home(request):
    content = HomepageContent.objects.first()
    return render(request, 'home.html', {'content': content})

def publications(request):
    publications = Publication.objects.all()
    return render(request, 'publications.html', {'publications': publications})

def contact(request):
    return render(request, 'contact.html')

def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def talks(request):
    talks = Talk.objects.all()
    return render(request, 'talks.html', {'talks': talks})

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})
