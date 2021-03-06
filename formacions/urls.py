from django.urls import path, include
from django.conf.urls import url, include

from formacions import api_endpoints


urlpatterns = [
    url(r'^formacions_user/', api_endpoints.get_formacions, name='get_formacions'),
    url(r'^(?P<id_formacio>\d+)/preguntes/', api_endpoints.get_preguntes, name='get_preguntes'),
    url(r'^preguntes/(?P<id_pregunta>\d+)/', api_endpoints.check_resposta, name='get_resposta'),
    url(r'^pregunta/(?P<id_pregunta>\d+)/get_correcta/', api_endpoints.resposta_correcta, name='resposta correcta'),
    url(r'^(?P<id_formacio>\d+)/submit/', api_endpoints.submit_formacio, name='submit formacio'),
]