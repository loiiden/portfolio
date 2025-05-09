# Generated by Django 5.1.3 on 2024-11-20 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/content/img'),
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='talk',
            name='place',
            field=models.TextField(blank=True, null=True),
        ),
    ]
