# Generated by Django 4.1.3 on 2023-03-25 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='autor',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
