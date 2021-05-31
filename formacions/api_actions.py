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


def get_preguntes(user, id_formacio):
    try:
        empresa = user.empresa
        formacio = Formacio.objects.get(id=id_formacio)

        try:
            formacio_empresa = Formacio_Empresa.objects.get(formacio=formacio, empresa=empresa)
        except Formacio_Empresa.DoesNotExist:
            return {'error': 'Aquesta formació no pertany a l\'empresa de l\'usuari.'}, None

        preguntes_array = []
        preguntes = []
        formacion_preguntes = Formacio_Pregunta.objects.filter(formacio=formacio)
        for form_empresa in formacion_preguntes:
            preguntes.append(form_empresa.pregunta)

        for pregunta in preguntes:
            if pregunta:
                pregunta_respostes = Pregunta_Resposta.objects.filter(pregunta=pregunta)
                respostes_array = []


                for preg_resposta in pregunta_respostes:

                    resposta_object = {
                        'id': preg_resposta.id,
                        'resposta': preg_resposta.resposta,
                    }

                    respostes_array.append(resposta_object)

                pregunta_object = {
                    'id': pregunta.id,
                    'enunciat': pregunta.enunciat,
                    'respostes': respostes_array,
                }

                preguntes_array.append(pregunta_object)

        result = {'preguntes': preguntes_array}
        return None, result
    except Exception as e:
        return {'error': 'API Error'}, None


def check_resposta(user, id_pregunta, id_resposta):
    try:

        empresa = user.empresa
        pregunta = Pregunta.objects.get(id=id_pregunta)

        try:
            formacio = Formacio_Pregunta.objects.get(pregunta=pregunta).formacio
            formacio_empresa = Formacio_Empresa.objects.get(formacio=formacio, empresa=empresa)
        except Formacio_Empresa.DoesNotExist:
            return {'error': 'Aquesta pregunta no pertany a cap formació de l\'empresa de l\'usuari.'}, None
        try:
            resposta = Pregunta_Resposta.objects.get(id=id_resposta)
        except Pregunta_Resposta.DoesNotExist:
            return {'error': 'Aquesta resposta no existeix.'}, None

        try:
            resposta = Pregunta_Resposta.objects.get(id=id_resposta, pregunta=pregunta)
        except Pregunta_Resposta.DoesNotExist:
            return {'error': 'Aquesta resposta no pertany a aquesta pregunta.'}, None

        result = {'is_correct': resposta.is_correct}
        return None, result

    except Exception as e:
        return {'error': 'API Error'}, None