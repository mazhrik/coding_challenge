# Generated by Django 3.1.13 on 2022-02-04 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vechile_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.TextField(default='')),
                ('manufacturer', models.TextField(default='')),
                ('status', models.TextField(default='')),
            ],
        ),
    ]
