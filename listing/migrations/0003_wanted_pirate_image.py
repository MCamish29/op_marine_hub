# Generated by Django 4.2.17 on 2025-01-08 21:12

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_wanted_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='wanted',
            name='pirate_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
