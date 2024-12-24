from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LaptopViewSet, LaptopPhotoViewSet

router = DefaultRouter()
router.register(r'laptops', LaptopViewSet)
router.register(r'laptop-photos', LaptopPhotoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
