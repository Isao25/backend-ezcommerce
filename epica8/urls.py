from django.urls import path
from . import views

app_name = 'epica8'

urlpatterns = [
    path("", views.index, name = "index")
]