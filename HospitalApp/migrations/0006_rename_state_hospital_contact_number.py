# Generated by Django 5.1.1 on 2024-10-27 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0005_history_created_at_history_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='state',
            new_name='contact_number',
        ),
    ]