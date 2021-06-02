
from formacions.models import Formacio_Usuari

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

        max_puntuacio = 0
        realitzades = Formacio_Usuari.objects.filter(usuari=user)
        for formacio in realitzades:
            max_puntuacio += formacio.max_puntuacio
        json_object = {
            'puntuacio': user.puntuacio,
            'max_puntuacio': max_puntuacio,
            'formacions_realitzades': len(realitzades),
        }

        return None, json_object

    except Exception as e:
        return {'error': 'API error'}, None