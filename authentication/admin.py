from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group  # new

from simple_history.admin import SimpleHistoryAdmin

from .models import Empresa

admin.site.unregister(Group)

@admin.register(get_user_model())
class UsuariAdmin(SimpleHistoryAdmin):
    list_per_page = 100

    list_display = (
        'email',
        'name',
        'if_admin',
        'empresa',

    )

    search_fields = [
        'email',
        'empresa'
    ]

class EmpresaAdmin(SimpleHistoryAdmin):
    list_per_page = 100

    list_display = (
        'nom',
    )

    search_fields = ['nom']

admin.site.register(Empresa, EmpresaAdmin)

