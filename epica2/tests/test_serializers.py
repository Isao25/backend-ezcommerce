from django.test import TestCase
from epica2.models import Facultad, EscuelaProfesional
from epica2.serializers import FacultadSerializer, EscuelaProfesionalSerializer

class FacultadSerializerTest(TestCase):
    def test_serialize_facultad(self):
        facultad = Facultad.objects.create(
            codigo="F003",
            nombre="Facultad de Ciencias Exactas",
            siglas="FCE"
        )
        serializer = FacultadSerializer(facultad)
        expected_data = {
            'id': facultad.id,
            'codigo': "F003",
            'nombre': "Facultad de Ciencias Exactas",
            'siglas': "FCE"
        }
        self.assertEqual(serializer.data, expected_data)

class EscuelaProfesionalSerializerTest(TestCase):
    def test_serialize_escuela(self):
        facultad = Facultad.objects.create(
            codigo="F004",
            nombre="Facultad de Humanidades",
            siglas="FH"
        )
        escuela = EscuelaProfesional.objects.create(
            id_facultad=facultad,
            codigo="EP002",
            nombre="Escuela de Historia"
        )
        serializer = EscuelaProfesionalSerializer(escuela)
        expected_data = {
            'id': escuela.id,
            'id_facultad': facultad.id,
            'codigo': "EP002",
            'nombre': "Escuela de Historia"
        }
        self.assertEqual(serializer.data, expected_data)
