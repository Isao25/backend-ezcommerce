from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from epica2.models import Facultad, EscuelaProfesional
from django.urls import reverse

class FacultadViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.facultad = Facultad.objects.create(
            codigo="F005",
            nombre="Facultad de Prueba API",
            siglas="FPA"
        )

    def test_list_facultades(self):
        response = self.client.get("/epica2/facultades/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_facultad(self):
        response = self.client.get(f"/epica2/facultades/{self.facultad.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class EscuelaProfesionalViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.facultad = Facultad.objects.create(
            codigo="F006",
            nombre="Facultad Ciencias Naturales",
            siglas="FCN"
        )
        self.escuela = EscuelaProfesional.objects.create(
            id_facultad=self.facultad,
            codigo="EP003",
            nombre="Escuela de Ecología"
        )

    def test_list_escuelas(self):
        response = self.client.get("/epica2/escuelas/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_escuela(self):
        response = self.client.get(f"/epica2/escuelas/{self.escuela.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
