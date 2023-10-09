# Generated by Django 4.1.7 on 2023-10-06 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0029_alter_loker_idloker'),
    ]

    operations = [
        migrations.CreateModel(
            name='BincangAlumni',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pesan', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
