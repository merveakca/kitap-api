from django.db import models

class Kitap(models.Model):
    isim = models.CharField(max_length=100)
    yazar = models.CharField(max_length=100)

    def __str__(self):
        return self.isim

