# Generated by Django 3.2.12 on 2023-01-30 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SampleApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
