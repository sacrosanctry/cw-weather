# Generated by Django 4.0.3 on 2022-04-17 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_admin', '0011_remove_weather_field_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
