# Generated by Django 3.2.3 on 2021-06-08 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formacions', '0005_formacio_usuari_max_puntuacio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formacio_usuari',
            old_name='data_ultima_realitzacio',
            new_name='data_realitzacio',
        ),
    ]