# Generated by Django 4.0.3 on 2022-04-17 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_admin', '0017_alter_city_id_alter_weather_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='weather',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
