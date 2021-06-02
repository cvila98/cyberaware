import json

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

import authentication.api_actions as api_actions


@csrf_exempt
@api_view(['PATCH'])
@permission_classes((IsAuthenticated,))
def update_profile(request):
    if request.method == 'PATCH':
        user = request.user
        jsonBody = json.loads(request.body)
        (error, response) = api_actions.update_user(user, jsonBody)
        if error:
            return Response(error, HTTP_400_BAD_REQUEST)

        return Response(response, HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_puntuacio_usuari(request):
    if request.method == 'GET':
        user = request.user
        (error, response) = api_actions.get_puntuacio_usuari(user)
        if error:
            return Response(error, HTTP_400_BAD_REQUEST)

        return Response(response, HTTP_200_OK)