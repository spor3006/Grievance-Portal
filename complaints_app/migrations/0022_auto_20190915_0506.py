# Generated by Django 2.2.1 on 2019-09-15 05:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('complaints_app', '0021_auto_20190915_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 15, 5, 6, 34, 192184, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(choices=[('Pl', 'Plumbing'), ('Ca', 'Carpentry'), ('El', 'Electricity')], default='Pl', max_length=2),
        ),
    ]
