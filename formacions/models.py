from django.db import models


# Create your models here.
from authentication.models import Empresa


class Formacio(models.Model):
    nom = models.CharField(max_length=200)
    descripcio = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.nom

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Formacio'
        verbose_name_plural = 'Formacions'
        default_permissions = {'add', 'change', 'delete', 'view'}


class Pregunta(models.Model):
    enunciat = models.CharField(max_length=200)

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
    resposta = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s - %s' % (self.formacio.nom, self.pregunta.enunciat)

    def __str__(self):
        return '%s - %s' % (self.formacio.nom, self.pregunta.enunciat)

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
