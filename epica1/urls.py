from django.urls import path
from rest_framework.routers  import DefaultRouter
from . import views

app_name = 'epica1'
router = DefaultRouter()
router.register(r'vendedores', views.VendedoresViewSet, basename='vendedores')

urlpatterns = [
    #path("", views.index, name = "index"),
]