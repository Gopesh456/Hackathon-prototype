# Generated by Django 5.0 on 2023-12-25 16:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_alter_answer_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]