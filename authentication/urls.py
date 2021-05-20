from django.urls import path, include

from rest_framework.routers import DefaultRouter

from authentication import views as auth_views

router = DefaultRouter()
router.register(r'', auth_views.UsuariViewSet, basename='authentication')
router.register(r'empreses', auth_views.EmpresaSet, basename='empreses')
router.register(r'users', auth_views.UsuariSet, basename='users')
router.register(r'users/profile', auth_views.CurrentUserView, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]