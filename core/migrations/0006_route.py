# Generated by Django 5.0.6 on 2024-07-02 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_is_student_profile_is_passenger'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_lat', models.FloatField()),
                ('origin_lng', models.FloatField()),
                ('destination_lat', models.FloatField()),
                ('destination_lng', models.FloatField()),
                ('duration', models.CharField(max_length=100)),
                ('distance_meters', models.IntegerField()),
                ('polyline', models.TextField()),
            ],
        ),
    ]