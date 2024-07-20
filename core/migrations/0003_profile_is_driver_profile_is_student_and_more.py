# Generated by Django 5.0.6 on 2024-07-02 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_driver',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(),
        ),
    ]