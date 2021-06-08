from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from CyberAware import api_actions

from authentication.models import Usuari, Empresa


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_puntuacions_empresa(request):
    user = request.user
    if request.method == 'GET':
        (error, response) = api_actions.get_puntuacions_empresa(user)

        if error:
            return Response(error, HTTP_400_BAD_REQUEST)

    return Response(response, HTTP_200_OK)