# Generated by Django 5.1.2 on 2024-10-29 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_remove_reminder_user'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='conversation',
            name='unique_conversation_per_user',
        ),
    ]