# Generated by Django 4.0.2 on 2022-02-22 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockuser',
            name='username',
        ),
    ]
