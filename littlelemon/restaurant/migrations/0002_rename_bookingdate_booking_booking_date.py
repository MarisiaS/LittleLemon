# Generated by Django 4.2 on 2023-04-11 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="bookingDate",
            new_name="booking_date",
        ),
    ]