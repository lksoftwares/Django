# Generated by Django 5.0.6 on 2024-05-20 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newschanel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newschanel',
            name='newsImage',
            field=models.FileField(default=None, max_length=255, null=True, upload_to='news/'),
        ),
    ]
