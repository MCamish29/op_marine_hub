# Generated by Django 4.2.17 on 2025-01-15 22:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0010_alter_wanted_pirate_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wanted',
            name='bounty',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
