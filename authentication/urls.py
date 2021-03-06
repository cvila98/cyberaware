from django.urls import path, include
from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from authentication import views as auth_views

from authentication import api_endpoints

router = DefaultRouter()
router.register(r'', auth_views.UsuariViewSet, basename='authentication')
router.register(r'empreses', auth_views.EmpresaSet, basename='empreses')
router.register(r'users/profile', auth_views.CurrentUserView, basename='user profile')

urlpatterns = [
    path('', include(router.urls)),
    url('^update_profile/', api_endpoints.update_profile, name='update profile'),
    url('^get_puntuacio/', api_endpoints.get_puntuacio_usuari, name='get puntuacio'),

]