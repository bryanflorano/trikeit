# Generated by Django 5.0.6 on 2024-07-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_profile_first_name_alter_profile_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='toda_number',
            new_name='TODA_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='toda',
        ),
        migrations.AddField(
            model_name='profile',
            name='TODA',
            field=models.CharField(blank=True, choices=[('loyola_heights', 'Loyola Heights (White)'), ('loyola_pansol', 'Loyola Pansol (Green)')], max_length=15),
        ),
    ]