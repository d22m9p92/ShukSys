from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from shuksys.viewsets import ProductoViewSet, ProductoCategoriaViewSet
from shuksys import views

router = DefaultRouter()
router.register('api/producto',ProductoViewSet)
router.register('api/productocategoria',ProductoCategoriaViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('api/login',views.login),

]
