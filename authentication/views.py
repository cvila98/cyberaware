from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from rest_framework import status, viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveUpdateAPIView
import rest_framework.permissions
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import UsuariLoginSerializer, UsuariModelSerializer, UsuariSignUpSerializer

from authentication.models import Usuari, Empresa
from .serializers import EmpresaModelSerializer


class ExactMatchModelViweSet(viewsets.ModelViewSet):
    def get_queryset(self):
        qs = super(ExactMatchModelViweSet, self).get_queryset()
        filter = {}
        for param in self.request.query_params:
            if hasattr(self.model, param):
                filter[param] = self.request.query_params.get(param)

        if filter != {}:
            try:
                qs = qs.filter(**filter)
            except ValueError as error:
                raise NotFound(error.message)
        return qs


class UsuariViewSet(viewsets.GenericViewSet):
    queryset = Usuari.objects.all()
    serializer_class = UsuariModelSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = UsuariLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UsuariModelSerializer(user).data,
            'access_token': token,
        }

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = UsuariSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UsuariModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)


class EmpresaSet(ExactMatchModelViweSet):
    model = Empresa
    queryset = Empresa.objects.get_queryset()
    serializer_class = EmpresaModelSerializer
    filter_fields = list(serializer_class.Meta.fields)


class UsuariSet(ExactMatchModelViweSet):
    model = Usuari
    queryset = Usuari.objects.all()
    permission_classes = (rest_framework.permissions.IsAdminUser,)
    serializer_class = UsuariModelSerializer


class CurrentUserView(viewsets.ModelViewSet):
    serializer_class = UsuariModelSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Usuari.objects.filter(email=user.email)



