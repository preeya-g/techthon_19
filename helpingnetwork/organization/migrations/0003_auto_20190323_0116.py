# Generated by Django 2.1.7 on 2019-03-22 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_organizationimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='organizer',
        ),
        migrations.RemoveField(
            model_name='event',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='event',
            name='volunteers',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='event',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='volunteer',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
    ]
