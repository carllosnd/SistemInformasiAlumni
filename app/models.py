from enum import Enum
import os
from django.db import models
from django.contrib.auth.models import User

from project import settings


class DataAlumni(models.Model):
    nim = models.CharField(primary_key=True, max_length=20)
    nama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    nohp = models.CharField(max_length=255)
    thnlulus = models.IntegerField()
    prodi = models.CharField(max_length=255)
    instansi = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=255)
    gambar = models.ImageField(upload_to='static/assets/images', blank=True, null=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diajukan = models.BooleanField(default=False)
    
    def delete(self, *args, **kwargs):
        # hapus foto yang terkait dengan instance Alumni saat dihapus
        if self.gambar:
            os.remove(self.gambar.path)
        super().delete(*args, **kwargs)


class Agenda(models.Model):
    idagenda = models.AutoField(primary_key=True)
    namaagenda = models.CharField(max_length=255)
    dateagenda = models.DateField()
    deskripsiagenda = models.CharField(max_length=500)
    
class Pengumuman(models.Model):
    idpengumuman = models.AutoField(primary_key=True)
    namapengumuman = models.CharField(max_length=255)
    datepengumuman = models.DateField()
    deskripsipengumuman = models.CharField(max_length=500)
    filepengumuman = models.FileField(upload_to='static/assets/file', blank=True, null=True)
    
    def delete(self, *args, **kwargs):
        # hapus file yang terkait dengan Pengumuman saat dihapus
        if self.filepengumuman:
            os.remove(self.filepengumuman.path)
        super().delete(*args, **kwargs)

class Loker(models.Model):
    idloker = models.AutoField(primary_key=True)
    dateloker = models.DateField()
    namaloker = models.CharField(max_length=255)
    instansi = models.CharField(max_length=255)
    fileloker = models.FileField(upload_to='static/assets/file', blank=True, null=True)
    
    def delete(self, *args, **kwargs):
        # hapus file yang terkait dengan Loker saat dihapus
        if self.fileloker:
            os.remove(self.fileloker.path)
        super().delete(*args, **kwargs)
