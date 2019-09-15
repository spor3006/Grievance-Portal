# Generated by Django 2.2.1 on 2019-09-14 20:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grievant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room', models.CharField(max_length=50)),
                ('Hostel', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('media', models.ImageField(upload_to='media/')),
                ('created_date', models.DateTimeField(default=datetime.datetime(2019, 9, 14, 20, 28, 58, 417457, tzinfo=utc))),
                ('status', models.CharField(choices=[('D', 'Done'), ('P', 'Pending'), ('N', 'Not Accepted')], default='N', max_length=1)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='complaints_app.Department')),
                ('grievant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='complaints_app.Grievant')),
            ],
        ),
    ]
