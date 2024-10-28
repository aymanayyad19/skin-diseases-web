# Generated by Django 5.1.1 on 2024-10-24 07:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0004_history_image_url_remove_history_skin_diseases_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]