# Generated by Django 5.0.3 on 2024-04-21 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("specialists", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="specialist",
            name="profile_photo",
            field=models.ImageField(null=True, upload_to="profile_photos/"),
        ),
    ]