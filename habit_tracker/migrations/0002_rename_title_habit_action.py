# Generated by Django 4.1.1 on 2022-09-07 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='title',
            new_name='action',
        ),
    ]