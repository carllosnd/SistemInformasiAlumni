# Generated by Django 4.1.7 on 2023-09-19 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]