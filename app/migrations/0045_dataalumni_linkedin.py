# Generated by Django 4.1.7 on 2023-10-25 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_dataalumni_grup'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataalumni',
            name='linkedin',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
