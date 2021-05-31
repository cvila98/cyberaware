from rest_framework import serializers

from formacions.models import Formacio


class FormacioModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formacio
        fields = [
            'nom',
            'descripcio'
        ]