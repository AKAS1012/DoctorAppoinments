# Generated by Django 4.1 on 2022-09-21 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Appointments", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appoinment_patient",
            name="phone_no",
            field=models.CharField(max_length=10),
        ),
    ]
