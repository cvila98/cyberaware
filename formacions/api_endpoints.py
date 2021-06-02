import json

import formacions.api_actions as api_actions
from django.http import HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import render, HttpResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.http import FileResponse, Http404

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR,
)


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_formacions(request):
    if request.method == 'GET':
        user = request.user

        (error, response) = api_actions.get_formacions(user)
        if error:
            return Response(error, HTTP_400_BAD_REQUEST)

        return Response(response, HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_preguntes(request, id_formacio):
    if request.method == 'GET':
        user = request.user
        (error, response) = api_actions.get_preguntes(user, id_formacio)

        if error:
            return Response(error, HTTP_400_BAD_REQUEST)

        return Response(response, HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def check_resposta(request, id_pregunta):
    if request.method == 'POST':
        jsonBody = json.loads(request.body)
        user = request.user
        (error, response) = api_actions.check_resposta(user, id_pregunta, jsonBody['resposta'])

        if error:
            return Response(error, HTTP_400_BAD_REQUEST)

        return Response(response, HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def resposta_correcta(request, id_pregunta):
    if request.method == 'GET':
        user = request.user
        (error, response) = api_actions.resposta_correcta(user, id_pregunta)

        if error:
            return Response(error, HTTP_400_BAD_REQUEST)

        return Response(response, HTTP_200_OK)
