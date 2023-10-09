# Generated by Django 4.1.7 on 2023-10-07 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0034_bincangalumni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pesan_reply', models.CharField(max_length=250)),
                ('tanggal', models.DateField()),
                ('pesan_utama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bincangalumni')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
