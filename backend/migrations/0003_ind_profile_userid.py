# Generated by Django 4.1.9 on 2023-06-24 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_ind_profile_contact_number_ind_profile_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ind_profile',
            name='userid',
            field=models.IntegerField(default=45),
            preserve_default=False,
        ),
    ]
