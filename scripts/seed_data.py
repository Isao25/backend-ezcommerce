import os
import sys
import django


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ezcommerce.settings')
django.setup()

from epica1.models import Usuario, UsuarioManager
from epica2.models import Facultad, EscuelaProfesional
from epica4.models import Etiqueta

#Limpiar Facultades
Facultad.objects.all().delete()
EscuelaProfesional.objects.all().delete()
Etiqueta.objects.all().delete()

# Crear Facultades
facultad1 = Facultad.objects.create(codigo="01", nombre="Facultad de Medicina - San Fernando", siglas="FMSF") #
facultad2 = Facultad.objects.create(codigo="02", nombre="Facultad de Derecho y Ciencias Políticas", siglas="FDCP") # 
facultad3 = Facultad.objects.create(codigo="03", nombre="Facultad de Letras y Ciencias Humanas", siglas="FLCH") #
facultad4 = Facultad.objects.create(codigo="04", nombre="Facultad de Farmacia y Bioquímica", siglas="FFB") #
facultad5 = Facultad.objects.create(codigo="05", nombre="Facultad de Odontología", siglas="FO") #
facultad6 = Facultad.objects.create(codigo="06", nombre="Facultad de Educación", siglas="FEDU") #
facultad7 = Facultad.objects.create(codigo="07", nombre="Facultad de Química e Ingeniería Química", siglas="FQIQ") #
facultad8 = Facultad.objects.create(codigo="08", nombre="Facultad de Medicina Veterinaria", siglas="FMV") #
facultad9 = Facultad.objects.create(codigo="09", nombre="Facultad de Ciencias Administrativas", siglas="FCA") #
facultad10 = Facultad.objects.create(codigo="10", nombre="Facultad de Ciencias Biológicas", siglas="FCB") #
facultad11 = Facultad.objects.create(codigo="11", nombre="Facultad de Ciencias Contables", siglas="FCC") #
facultad12 = Facultad.objects.create(codigo="12", nombre="Facultad de Ciencias Económicas", siglas="FCE") #
facultad13 = Facultad.objects.create(codigo="13", nombre="Facultad de Ciencias Físicas", siglas="FCF") #
facultad14 = Facultad.objects.create(codigo="14", nombre="Facultad de Ciencias Matemáticas", siglas="FCM") #
facultad15 = Facultad.objects.create(codigo="15", nombre="Facultad de Ciencias Sociales", siglas="FCS") #
facultad16 = Facultad.objects.create(codigo="16", nombre="Facultad de Ingeniería Geológica, Minera, Metalúrgica y Geográfica", siglas="FIGMMG") #
facultad17 = Facultad.objects.create(codigo="17", nombre="Facultad de Ingeniería Industrial", siglas="FII") #
facultad18 = Facultad.objects.create(codigo="18", nombre="Facultad de Psicología", siglas="FPSI") #
facultad19 = Facultad.objects.create(codigo="19", nombre="Facultad de Ingeniería Eléctrica y Electrónica", siglas="FIEE") #
facultad20 = Facultad.objects.create(codigo="20", nombre="Facultad de Ingeniería de Sistemas e Informática", siglas="FISI") #

# Crear Escuelas Profesionales
escuela1 = EscuelaProfesional.objects.create(codigo="EPIS", nombre="Ingeniería de Sistemas", id_facultad=facultad20)
escuela2 = EscuelaProfesional.objects.create(codigo="EPISW", nombre="Ingeniería de Software", id_facultad=facultad20)
escuela3 = EscuelaProfesional.objects.create(codigo="EPCC", nombre="Ciencias de la Computación", id_facultad=facultad20)

# Crear Etiquetas:
etiqueta1 = Etiqueta.objects.create(nombre="Electrónica", descripcion="Productos electrónicos.")
etiqueta2 = Etiqueta.objects.create(nombre="Libros y Revistas", descripcion="Libros y revistas.")
etiqueta3 = Etiqueta.objects.create(nombre="Productos Alimenticios", descripcion="Alimentos, comidas, bebidas.")
etiqueta4 = Etiqueta.objects.create(nombre="Asesorías", descripcion="Asesorías personalizadas en cursos.")


print("Datos iniciales insertados con éxito.")