from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from .models import Pregunta, Formacio_Pregunta, Formacio, Formacio_Empresa, Pregunta_Resposta, Formacio_Usuari


class PreguntaAdmin(SimpleHistoryAdmin):
    list_per_page = 100

    list_display = (
        'id',
        'enunciat',

    )

    search_fields = [
        'enunciat',
        'id'
    ]


admin.site.register(Pregunta, PreguntaAdmin)


class FormacioAdmin(SimpleHistoryAdmin):
    list_per_page = 100

    list_display = (
        'id',
        'nom',
        'descripcio',
    )

    search_fields = [
        'nom',
        'id',
    ]


admin.site.register(Formacio, FormacioAdmin)

class Formacio_PreguntaAdmin(SimpleHistoryAdmin):
    list_per_page = 100

    list_display = (
        'formacio',
        'pregunta',
    )

    search_fields = [
        'formacio',
        'pregunta',
    ]


admin.site.register(Formacio_Pregunta, Formacio_PreguntaAdmin)

class Formacio_EmpresaAdmin(SimpleHistoryAdmin):
    list_per_page = 100

    list_display = (
        'formacio',
        'empresa',
    )

    search_fields = [
        'formacio',
        'empresa',
    ]


admin.site.register(Formacio_Empresa, Formacio_EmpresaAdmin)

class Pregunta_RespostaAdmin(SimpleHistoryAdmin):
    list_per_page = 100

    list_display = (
        'pregunta',
        'resposta',
        'is_correct'
    )

    search_fields = [
        'pregunta',
        'resposta',
    ]

    list_filter = [
        'is_correct',
    ]


admin.site.register(Pregunta_Resposta, Pregunta_RespostaAdmin)

class Formacio_UsuariAdmin(SimpleHistoryAdmin):
    list_per_page = 100

    list_display = (
        'formacio',
        'usuari',
    )

    search_fields = [
        'formacio',
        'usuari',
    ]


admin.site.register(Formacio_Usuari, Formacio_UsuariAdmin)
