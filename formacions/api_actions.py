import datetime

from authentication.models import Empresa, Usuari
from formacions.models import Formacio, Formacio_Empresa, Formacio_Pregunta, Pregunta, Pregunta_Resposta, \
    Formacio_Usuari


def get_formacions(user):
    try:
        empresa = user.empresa
        formacions_array = []
        formacions = []
        realitzades = []
        realitzades_array = []
        formacions_empresa = Formacio_Empresa.objects.filter(empresa=empresa)
        for form_empresa in formacions_empresa:
            realitzada = False
            try:
                formacio_usuari = Formacio_Usuari.objects.filter(formacio=form_empresa.formacio, usuari=user)
                date_before = datetime.date.today() - datetime.timedelta(days=7)
                for formacio in formacio_usuari:
                    if not realitzada:
                        if date_before < formacio.data_realitzacio:
                            realitzada = True

            except Formacio_Usuari.DoesNotExist:
                realitzada = False

            if not realitzada:
                formacions.append(form_empresa.formacio)
            else:
                realitzades.append(form_empresa.formacio)


        for formacio in formacions:
            if formacio:
                formacio_object = {
                    'id': formacio.id,
                    'nom': str(formacio.nom),
                    'descripcio': str(formacio.descripcio),
                }

                formacions_array.append(formacio_object)

        for formacio in realitzades:
            if formacio:
                formacio_object = {
                    'id': formacio.id,
                    'nom': str(formacio.nom),
                    'descripcio': str(formacio.descripcio),
                }

                realitzades_array.append(formacio_object)

        result = {'formacions': formacions_array,
                  'realitzades': realitzades_array}


        return None, result

    except Exception as e:
        print(e)
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

        result = {'is_correct': resposta.is_correct,
                  'hint': resposta.hint.__str__()}
        return None, result

    except Exception as e:
        return {'error': 'API Error'}, None


def resposta_correcta(user, id_pregunta):
    try:
        resposta_correcta = 0
        empresa = user.empresa
        pregunta = Pregunta.objects.get(id=id_pregunta)

        try:
            formacio = Formacio_Pregunta.objects.get(pregunta=pregunta).formacio
            formacio_empresa = Formacio_Empresa.objects.get(formacio=formacio, empresa=empresa)
        except Formacio_Empresa.DoesNotExist:
            return {'error': 'Aquesta pregunta no pertany a cap formació de l\'empresa de l\'usuari.'}, None

        respostes = Pregunta_Resposta.objects.filter(pregunta= pregunta)

        for resposta in respostes:
            if resposta.is_correct:
                resposta_correcta = resposta.id


        result = {'resposta_correcta': resposta_correcta}
        return None, result

    except Exception as e:
        return {'error': 'API Error'}, None


def submit_formacio(user, id_formacio, jsonBody):
    try:
        date_aux = jsonBody['date'].split('-')
        print(date_aux)
        date= datetime.date(int(date_aux[0]), int(date_aux[1]), int(date_aux[2]))
        puntuacio = jsonBody['puntuacio']
        max_puntuacio = jsonBody['max_puntuacio']
        try:
            formacio = Formacio.objects.get(id=id_formacio)
        except Formacio.DoesNotExist:
            return {'error': 'Aquesta formacio no existeix.'}, None

        empresa = user.empresa
        try:
            formacio_empresa = Formacio_Empresa.objects.get(formacio=formacio, empresa=empresa)
        except Formacio_Empresa.DoesNotExist:
            return {'error': 'Aquesta formació no pertany a l\'empresa de l\'usuari.'}, None

        try:
            formacio_usuari = Formacio_Usuari.objects.get(usuari=user, formacio=formacio, data_realitzacio=date)
        except Formacio_Usuari.DoesNotExist:
            formacio_usuari = Formacio_Usuari(usuari=user, formacio=formacio, data_realitzacio=date)

        if formacio_usuari.data_realitzacio != date:
            user.puntuacio_acumulada += puntuacio
            user.max_puntuacio_acumulada += max_puntuacio
            user.formacions_acumulades +=1
            user.save()

        formacio_usuari.puntuacio = puntuacio
        formacio_usuari.max_puntuacio = max_puntuacio
        formacio_usuari.save()


        result = {'Submit realitzat amb exit.'}
        return None, result
    except Exception as e:
        print(e)
        return {'error': 'API Error'}, None