# Generated by Django 5.0 on 2023-12-25 16:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_answer_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='create',
            field=models.TimeField(verbose_name=datetime.time),
        ),
    ]
