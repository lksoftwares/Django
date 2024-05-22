# Generated by Django 5.0.6 on 2024-05-18 10:21

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsChanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsTitle', models.CharField(max_length=50)),
                ('newsInfo', tinymce.models.HTMLField()),
            ],
        ),
    ]