from django.contrib import admin
from .models import Publication, Event, Talk, Course

admin.site.register(Publication)
admin.site.register(Event)
admin.site.register(Talk)
admin.site.register(Course)