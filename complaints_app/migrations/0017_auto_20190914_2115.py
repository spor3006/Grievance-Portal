# Generated by Django 2.2.1 on 2019-09-14 21:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('complaints_app', '0016_auto_20190914_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 14, 21, 15, 34, 825407, tzinfo=utc)),
        ),
    ]
