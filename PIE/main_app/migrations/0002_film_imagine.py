# Generated by Django 2.0b1 on 2017-11-01 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='imagine',
            field=models.CharField(default='', max_length=255),
        ),
    ]