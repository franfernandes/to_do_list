# Generated by Django 3.2.12 on 2023-11-10 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20231110_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
