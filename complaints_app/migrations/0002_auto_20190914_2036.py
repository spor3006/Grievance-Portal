# Generated by Django 2.2.1 on 2019-09-14 20:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('complaints_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 14, 20, 36, 3, 538300, tzinfo=utc)),
        ),
    ]
