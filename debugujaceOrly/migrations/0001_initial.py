# Generated by Django 4.2.3 on 2023-07-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=260)),
                ('address', models.CharField(max_length=200)),
                ('opening_hour', models.TimeField()),
                ('closing_hour', models.TimeField()),
            ],
        ),
    ]
