# Generated by Django 3.2 on 2023-07-13 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='Unspecified', max_length=100, null=True),
        ),
    ]