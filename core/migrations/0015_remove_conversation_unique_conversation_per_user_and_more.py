# Generated by Django 5.1.2 on 2024-10-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_reminder_user'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='conversation',
            name='unique_conversation_per_user',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='user',
        ),
        migrations.AlterField(
            model_name='conversation',
            name='conversation_id',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]