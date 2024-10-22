# Generated by Django 5.1 on 2024-09-10 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_content_reminder_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='description',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='title',
        ),
        migrations.AddField(
            model_name='reminder',
            name='Descrição',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='reminder',
            name='Evento',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='reminder',
            name='Local',
            field=models.TextField(blank=True),
        ),
    ]