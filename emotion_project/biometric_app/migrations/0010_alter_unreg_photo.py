# Generated by Django 4.0.3 on 2022-05-21 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biometric_app', '0009_alter_unreg_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unreg',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='biometric_app/image'),
        ),
    ]
