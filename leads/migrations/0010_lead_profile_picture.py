# Generated by Django 5.0.4 on 2024-04-13 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0009_lead_date_added_lead_description_lead_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
