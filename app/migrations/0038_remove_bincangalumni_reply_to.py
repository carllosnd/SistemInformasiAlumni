# Generated by Django 4.1.7 on 2023-10-07 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_delete_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bincangalumni',
            name='reply_to',
        ),
    ]