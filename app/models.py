from django.db import models

class Member(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    verification_code = models.CharField(max_length=16, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.nama
