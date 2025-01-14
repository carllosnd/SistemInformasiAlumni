# Generated by Django 4.1.7 on 2023-09-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0006_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('verification_code', models.CharField(blank=True, max_length=16)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
    ]
