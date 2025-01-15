# Generated by Django 4.2.17 on 2025-01-15 21:21

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0008_alter_wanted_pirate_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wanted',
            name='pirate_image',
            field=cloudinary.models.CloudinaryField(default='images/marines.png', max_length=255, verbose_name='image'),
        ),
    ]
