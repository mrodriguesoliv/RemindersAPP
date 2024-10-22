# Generated by Django 5.1 on 2024-09-06 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_reminder_conversation_reminder_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='conversation',
        ),
        migrations.AddField(
            model_name='reminder',
            name='conversation_id',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]