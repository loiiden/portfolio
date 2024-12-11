from django.contrib import admin
from .models import Publication, Event, Talk, Course, HomepageContent

admin.site.register(Publication)
admin.site.register(Event)
admin.site.register(Talk)
admin.site.register(Course)
admin.site.register(HomepageContent)