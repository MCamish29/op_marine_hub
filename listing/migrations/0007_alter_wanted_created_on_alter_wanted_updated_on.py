# Generated by Django 4.2.17 on 2025-01-13 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0006_alter_wanted_created_on_alter_wanted_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wanted',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='wanted',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
