# Generated by Django 5.0 on 2023-12-27 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_alter_answer_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]