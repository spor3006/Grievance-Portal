# Generated by Django 2.2.1 on 2019-09-15 01:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('complaints_app', '0018_auto_20190914_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 15, 1, 40, 25, 152927, tzinfo=utc)),
        ),
    ]
