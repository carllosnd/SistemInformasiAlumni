# Generated by Django 4.1.7 on 2023-09-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_pengumuman'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loker',
            fields=[
                ('idloker', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('dateloker', models.DateField()),
                ('namaloker', models.CharField(max_length=255)),
                ('instansi', models.CharField(max_length=255)),
                ('fileloker', models.FileField(blank=True, null=True, upload_to='static/assets/file')),
            ],
        ),
    ]
