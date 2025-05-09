# Generated by Django 5.1.3 on 2024-12-18 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_homepagecontent_photo1_homepagecontent_photo2'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagecontent',
            name='text2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepagecontent',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='content/img/'),
        ),
        migrations.AlterField(
            model_name='homepagecontent',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='content/img'),
        ),
    ]
