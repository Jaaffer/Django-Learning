# Generated by Django 3.2.12 on 2023-01-31 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SampleApp', '0002_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='media'),
        ),
    ]
