# Generated by Django 4.1.7 on 2023-10-06 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_bincangalumni'),
    ]

    operations = [
        migrations.AddField(
            model_name='bincangalumni',
            name='date',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]