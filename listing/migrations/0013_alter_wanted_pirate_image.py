# Generated by Django 4.2.17 on 2025-01-16 19:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0012_alter_wanted_bounty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wanted',
            name='pirate_image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dunhhqljl/image/upload/v1736789635/marines_aculb0.png', max_length=255, verbose_name='image'),
        ),
    ]
