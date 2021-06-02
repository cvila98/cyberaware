from django.db import models


# Create your models here.
from authentication.models import Empresa, Usuari


class Formacio(models.Model):
    nom = models.CharField(max_length=200)
    descripcio = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.nom

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Formacio'
        verbose_name_plural = 'Formacions'
        default_permissions = {'add', 'change', 'delete', 'view'}


class Pregunta(models.Model):
    enunciat = models.TextField()

    def __unicode__(self):
        return self.enunciat

    def __str__(self):
        return self.enunciat

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntes'
        default_permissions = {'add', 'change', 'delete', 'view'}

class Formacio_Pregunta(models.Model):
    formacio = models.ForeignKey(Formacio, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s - %s' % (self.formacio.nom, self.pregunta.enunciat)

    def __str__(self):
        return '%s - %s' % (self.formacio.nom, self.pregunta.enunciat)

    class Meta:
        verbose_name = 'Relacio Formacio-Pregunta'
        verbose_name_plural = 'Relacions Formacio-Pregunta'
        default_permissions = {'add', 'change', 'delete', 'view'}


class Pregunta_Resposta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    resposta = models.TextField()
    hint = models.TextField(null=True, blank=True)
    is_correct = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s - %s' % (self.pregunta.enunciat, self.resposta)

    def __str__(self):
        return '%s - %s' % (self.pregunta.enunciat, self.resposta)

    class Meta:
        verbose_name = 'Relacio Pregunta-Resposta'
        verbose_name_plural = 'Relacions Pregunta-Resposta'
        default_permissions = {'add', 'change', 'delete', 'view'}

class Formacio_Empresa(models.Model):
    formacio = models.ForeignKey(Formacio, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s - %s' % (self.formacio.nom, self.empresa.nom)

    def __str__(self):
        return '%s - %s' % (self.formacio.nom, self.empresa.nom)

    class Meta:
        verbose_name = 'Relacio Formacio-Empresa'
        verbose_name_plural = 'Relacions Formacio-Empresa'
        default_permissions = {'add', 'change', 'delete', 'view'}

class Formacio_Usuari(models.Model):
    formacio = models.ForeignKey(Formacio, on_delete=models.CASCADE)
    usuari = models.ForeignKey(Usuari, on_delete=models.CASCADE)
    max_puntuacio = models.IntegerField(default=0, null=True, blank=True)
    puntuacio = models.IntegerField(default=0, null=True, blank=True)
    data_ultima_realitzacio = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return '%s - %s' % (self.formacio.nom, self.usuari.name)

    def __str__(self):
        return '%s - %s' % (self.formacio.nom, self.usuari.name)

    class Meta:
        verbose_name = 'Relacio Formacio realitzada-Usuari'
        verbose_name_plural = 'Relacions Formacions realitzades-Usuaris'
        default_permissions = {'add', 'change', 'delete', 'view'}
