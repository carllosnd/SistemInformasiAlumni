# Generated by Django 4.1.7 on 2023-10-09 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataalumni',
            name='diajukan',
        ),
    ]
