# Generated by Django 3.2.12 on 2023-11-10 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='data_de_execucao',
            field=models.DateField(blank=True, null=True),
        ),
    ]
