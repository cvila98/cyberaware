# Generated by Django 3.2.3 on 2021-06-02 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20210526_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuari',
            name='puntuacio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]