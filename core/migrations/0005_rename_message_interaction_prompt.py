# Generated by Django 5.1 on 2024-09-02 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_conversation_interaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interaction',
            old_name='message',
            new_name='prompt',
        ),
    ]