# Generated by Django 5.0 on 2024-01-04 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_booking_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='status',
            field=models.CharField(default='new', max_length=50),
        ),
    ]