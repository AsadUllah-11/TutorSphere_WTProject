# Generated by Django 5.0.6 on 2024-07-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_market', '0019_tutor_calendly_access_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='profile_status',
            field=models.BooleanField(default=False),
        ),
    ]