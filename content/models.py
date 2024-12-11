from django.db import models

# Create your models here.

class Publication(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='content/docs')
    date = models.DateField()
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    place = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="content/img/", null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.title

class Talk(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    place = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    link = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.title
class HomepageContent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.title