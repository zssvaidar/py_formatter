# Generated by Django 2.0.9 on 2020-03-10 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiler', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='_mail',
            new_name='mail',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='_phone_number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='_surname',
            new_name='surname',
        ),
    ]