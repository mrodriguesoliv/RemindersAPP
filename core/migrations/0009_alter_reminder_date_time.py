# Generated by Django 5.1 on 2024-09-06 12:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_reminder_conversation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='date_time',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
