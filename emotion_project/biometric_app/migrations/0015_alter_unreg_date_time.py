# Generated by Django 4.0.3 on 2022-05-23 05:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biometric_app', '0014_alter_unreg_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unreg',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 23, 11, 18, 53, 863751), null=True),
        ),
    ]
