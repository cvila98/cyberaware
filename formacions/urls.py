from django.urls import path, include
from django.conf.urls import url, include

from formacions import api_endpoints


urlpatterns = [
    url(r'^get_formacions', api_endpoints.get_formacions, name='get_formacions'),
]