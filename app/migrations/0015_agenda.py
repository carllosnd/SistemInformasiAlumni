# Generated by Django 4.1.7 on 2023-09-26 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_dataalumni_gambar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('idagenda', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('dateagenda', models.DateField()),
                ('deskripsiagenda', models.CharField(max_length=500)),
            ],
        ),
    ]