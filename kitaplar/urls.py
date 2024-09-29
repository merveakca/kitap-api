from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KitapViewSet

router = DefaultRouter()
router.register(r'kitaplar', KitapViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
