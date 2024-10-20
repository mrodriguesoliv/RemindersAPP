# Generated by Django 5.1 on 2024-09-04 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_message_interaction_prompt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reminder',
            old_name='description',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='response',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='title',
        ),
        migrations.AddField(
            model_name='reminder',
            name='date_time',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='reminder',
            name='location',
            field=models.TextField(null=True),
        ),
    ]
