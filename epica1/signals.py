from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.conf import settings
from .models import EscuelaProfesional, Facultad, User

@receiver(post_migrate)
def create_facultades(sender, **kwargs):
    if sender.name == 'epica1':
        facultades = [
            {'codigo': '01', 'nombre': 'Facultad de Medicina'},
            {'codigo': '02', 'nombre': 'Facultad de Derecho y Ciencias Políticas'},
            {'codigo': '03', 'nombre': 'Facultad de Letras y Ciencias Humanas'},
            {'codigo': '04', 'nombre': 'Facultad de Farmacia y Bioquímica'},
            {'codigo': '05', 'nombre': 'Facultad de Odontología'},
            {'codigo': '06', 'nombre': 'Facultad de Educación'},
            {'codigo': '07', 'nombre': 'Facultad de Quimica e Ingenieria Quimica'},
            {'codigo': '08', 'nombre': 'Facultad de Medicina Veterinaria'},
            {'codigo': '09', 'nombre': 'Facultad de Ciencias Administrativas'},
            {'codigo': '10', 'nombre': 'Facultad de Ciencias Biológicas'},
            {'codigo': '11', 'nombre': 'Facultad de Ciencias Contables'},
            {'codigo': '12', 'nombre': 'Facultad de Ciencias Económicas'},
            {'codigo': '13', 'nombre': 'Facultad de Ciencias Físicas'},
            {'codigo': '14', 'nombre': 'Facultad de Ciencias Matemáticas'},
            {'codigo': '15', 'nombre': 'Facultad de Ciencias Sociales'},
            {'codigo': '16', 'nombre': 'Facultad de Ingeniería Geologica, Minera, Metalurgia y Geografica'},
            {'codigo': '17', 'nombre': 'Facultad de Ingeniería Industrial'},
            {'codigo': '18', 'nombre': 'Facultad de Psicología'},
            {'codigo': '19', 'nombre': 'Facultad de Ingeniería Electrónica y Eléctrica'},
            {'codigo': '20', 'nombre': 'Facultad de Ingeniería de Sistemas e Informática'},
        ]

        for facultad_data in facultades:
            Facultad.objects.get_or_create(codigo=facultad_data['codigo'], defaults=facultad_data)

        facultad_fisi = Facultad.objects.get(codigo='20')
        escuela, created = EscuelaProfesional.objects.get_or_create(facultad=facultad_fisi, codigo='01', nombre='Ingeniería de Sistemas')


        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(username='admin',
                               email='admin@example.com',
                               password='admin151',
                               code='21200277',
                               birth_date='1990-01-01',
                               escuela=escuela  # Ajusta según sea necesario
                           )
