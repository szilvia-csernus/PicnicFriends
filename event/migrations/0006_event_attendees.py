# Generated by Django 3.2 on 2023-07-15 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_event_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.IntegerField(default=0),
        ),
    ]
