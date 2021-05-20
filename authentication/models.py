from django.db import models
from django.contrib.auth.models import AbstractUser


class Empresa(models.Model):
    nom = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.nom

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name= 'Empresa'
        verbose_name_plural = 'Empreses'
        default_permissions = {'add', 'change', 'delete', 'view'}


class Usuari(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    name = models.CharField(max_length=200, null=True, blank=True)
    if_admin = models.BooleanField(null=True, default=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.email

    class Meta:
        verbose_name= 'Usuari'
        verbose_name_plural = 'Usuari'
        default_permissions = {'add', 'change', 'delete', 'view'}