# Generated by Django 5.0.7 on 2024-08-27 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_reminder_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='response',
            field=models.TextField(blank=True, null=True),
        ),
    ]