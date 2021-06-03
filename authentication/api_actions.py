
from formacions.models import Formacio_Usuari, Formacio_Empresa


def update_user(user, jsonBody):
    try:
        if 'name' in jsonBody.keys():
            user.name = jsonBody['name']
        user.save()

        user_object = {
            'email': user.email,
            'name': user.name,
            'username': user.username,
            'if_admin': user.if_admin,
            'empresa': user.empresa.nom,
        }
        result = {'user': user_object}
        return None, result

    except Exception as e:
        return {'error': 'API error'}, None


def get_puntuacio_usuari(user):
    try:
        puntuacio=0
        max_puntuacio = 0
        realitzades = Formacio_Usuari.objects.filter(usuari=user)
        empresa = user.empresa
        formacions_empresa = Formacio_Empresa.objects.filter(empresa=empresa)
        for formacio in realitzades:
            puntuacio += formacio.puntuacio
            max_puntuacio += formacio.max_puntuacio

        user.puntuacio = puntuacio
        user.save()

        json_object = {
            'puntuacio': puntuacio,
            'max_puntuacio': max_puntuacio,
            'formacions_realitzades': len(realitzades),
            'formacions': len(formacions_empresa),
        }

        return None, json_object

    except Exception as e:
        return {'error': 'API error'}, None