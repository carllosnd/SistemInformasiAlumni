# Generated by Django 4.1.7 on 2023-09-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_agenda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pengumuman',
            fields=[
                ('idpengumuman', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('deskripsipengumuman', models.CharField(max_length=500)),
                ('filepengumuman', models.FileField(blank=True, null=True, upload_to='static/assets/file')),
            ],
        ),
    ]
