# Generated by Django 4.0.6 on 2022-08-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_hotel_details_hotel_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='resultsnotfound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
