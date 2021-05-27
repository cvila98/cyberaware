from authentication.models import Empresa, Usuari
from formacions.models import Formacio, Formacio_Empresa, Formacio_Pregunta, Pregunta, Pregunta_Resposta


def get_formacions(user):
    try:
        empresa = user.empresa
        formacions_array = []
        formacions = []
        formacions_empresa = Formacio_Empresa.objects.filter(empresa=empresa)
        for form_empresa in formacions_empresa:
            formacions.append(form_empresa.formacio)

        for formacio in formacions:
            if formacio:
                formacio_object = {
                    'id': formacio.id,
                    'nom': formacio.nom,
                    'descripcio': formacio.descripcio,
                }

                formacions_array.append(formacio_object)

        result = {'formacions': formacions_array}
        return None, result

    except Exception as e:
        return {'error': 'API error'}, None
