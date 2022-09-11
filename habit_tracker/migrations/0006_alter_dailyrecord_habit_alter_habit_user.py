# Generated by Django 4.1.1 on 2022-09-11 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0005_dailyrecord_date_dailyrecord_target_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyrecord',
            name='habit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habit', to='habit_tracker.habit'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habit', to=settings.AUTH_USER_MODEL),
        ),
    ]