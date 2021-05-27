from rest_framework import serializers
from django.contrib.auth import password_validation, authenticate, get_user_model
from django.core.validators import RegexValidator, FileExtensionValidator

from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from authentication.models import Usuari, Empresa


class UsuariModelSerializer(serializers.ModelSerializer):
    empresa = serializers.SlugRelatedField(read_only=True, slug_field='nom')

    class Meta:
        model = Usuari
        fields = [
            'email',
            'name',
            'username',
            'if_admin',
            'empresa'
        ]


class UsuariLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=24)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])

        if not user:
            raise serializers.ValidationError('Les credencials no son vàlides.')

        self.context['user'] = user
        return data

    def create(self, validated_data):
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class UsuariSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Usuari.objects.all())]
    )

    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=Usuari.objects.all())]
    )

    password = serializers.CharField(min_length=8, max_length=24)
    password_confirmation = serializers.CharField(min_length=8, max_length=24)

    name = serializers.CharField(min_length=1, max_length=100)
    if_admin = serializers.BooleanField(default=False, allow_null=True)
    empresa = serializers.CharField(max_length=200)

    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Les contrasenyes no coincideixen.")
        password_validation.validate_password(passwd)

        return data

    def create(self, data):
        data.pop('password_confirmation')
        print(data)
        name_empresa = data.pop('empresa')
        empresa = Empresa.objects.get(nom=name_empresa)
        user = Usuari.objects.create_user(**data, empresa=empresa)
        return user


class EmpresaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = [
            'nom'
        ]
