# Generated by Django 3.2.6 on 2021-08-16 20:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 16, 22, 39, 47, 215846), verbose_name='date published'),
        ),
    ]
