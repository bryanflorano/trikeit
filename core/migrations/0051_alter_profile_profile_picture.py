# Generated by Django 4.2.13 on 2024-07-19 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='profile_pictures/default_profile.png', upload_to='profile_pictures/'),
        ),
    ]