import datetime

from authentication.models import Usuari
from formacions.models import Formacio_Usuari


def get_puntuacions_empresa(user):
    try:
        if not user.if_admin:
            return {'error': 'L\'usuari no és administrador de l\'empresa.'}, None

        date_before = datetime.date.today() - datetime.timedelta(days=7)

        puntuacio_actual = 0
        max_puntuacio_actual = 0
        puntuacio_acumulada = 0
        max_puntuacio_acumulada = 0
        empresa = user.empresa

        usuaris = Usuari.objects.filter(empresa=empresa)

        for usuari in usuaris:
            puntuacio_acumulada += usuari.puntuacio_acumulada
            max_puntuacio_acumulada += usuari.max_puntuacio_acumulada

            formacions_realitzades = Formacio_Usuari.objects.filter(usuari=usuari, data_realitzacio__gte=date_before)
            for formacio in formacions_realitzades:
                puntuacio_actual += formacio.puntuacio
                max_puntuacio_actual += formacio.max_puntuacio

        json_object = {
            'puntuacio_actual': puntuacio_actual,
            'max_puntuacio_actual': max_puntuacio_actual,
            'puntuacio_acumulada': puntuacio_acumulada,
            'max_puntuacio_acumulada': max_puntuacio_acumulada,
        }

        return None, json_object

    except Exception as e:
        return {'error': 'API error'}, None