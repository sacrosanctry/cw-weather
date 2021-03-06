# Generated by Django 4.0.3 on 2022-04-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_admin', '0007_remove_weather_date_remove_weather_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='date_time',
        ),
        migrations.AddField(
            model_name='weather',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='time',
            field=models.IntegerField(choices=[(1, 'Day'), (2, 'Night')], default=1),
            preserve_default=False,
        ),
    ]
