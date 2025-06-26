from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from epica2.models import EscuelaProfesional

#Clase Grupo
class Group(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        app_label = 'epica1'
    
    def __str__(self):
        return self.name

#Clase UsuarioManager
class UsuarioManager(BaseUserManager):
    #Crear usuario
    def create_user(self, nombres, username, email, id_escuela, password = None, **extra_fields):
        if not email: #verifica que tenga corre electrónico
            raise ValueError("El usuario debe registrar un correo electrónico")
        if not id_escuela: #verifica que pertenezca a una escuela profesional
            raise ValueError("El usuario debe tener una escuela asociada")
        
        user = self.model( #datos del usuario personalizado
            nombres = nombres,
            username = username,
            email = self.normalize_email(email),
            id_escuela=id_escuela,
            password = make_password(password, salt=None, hasher='default'),
            **extra_fields #acepta campos extras
        )

        user.set_password(password)
        user.save()
        return user
    
    #Crear superusuario
    def create_superuser(self, nombres, username, email, id_escuela, password, **extra_fields):
        user = self.create_user( #datos del superusuario personalizado
            nombres = nombres,
            username = username,
            email = email,
            id_escuela=id_escuela,
            password = password,
            **extra_fields #acepta campos extras
        )
        user.usuario_administrador = True
        user.save()
        return user

# Clase Usuario
class Usuario(AbstractBaseUser):
    username_validator = RegexValidator(
        regex=r'^[\w.@+-_%]+$', #verifica que el usuario cumple con los criterios de caracter alfanumérico y caracteres especiales requerdos
        message='El username puede contener letras, números y los caracteres @/./+/-/_%', #El caso del caracter '@' es para que el usuario sea el mismo que el correo electrónico de ser necesario
        code='invalid_username'
    )
    id_escuela = models.ForeignKey(EscuelaProfesional, on_delete = models.CASCADE, verbose_name = "Escuela Profesional") #Obligatorio
    username = models.CharField("Nombre de usuario", max_length = 100, unique = True) #Obligatorio
    email = models.EmailField("Correo electrónico", max_length = 254, unique = True) #Obligatorio
    nombres = models.CharField("Nombres", max_length = 200) #Obligatorio
    apellido_p = models.CharField("Apellido paterno", max_length = 200) #Obligatorio
    apellido_m = models.CharField("Apellido materno", max_length = 200)  #Obligatorio  
    celular = models.CharField("Celular", max_length = 20) #Obligatorio
    codigo = models.CharField("Código de estudiante", max_length = 100, unique = True)
    fecha_nacimiento = models.DateField("Fecha de nacimiento", null=True, blank=True) #Automático
    codigoqr = models.URLField("Código QR", null=True, blank=True)
    tiene_marca = models.BooleanField("Tiene marca", default=False) #Automático
    es_vendedor = models.BooleanField("Es usuario vendedor: ", default=False) #Automático

    fecha_registro = models.DateTimeField(auto_now_add=True) #Automático
    
    usuario_administrador = models.BooleanField(default=False) #Automático
    usuario_activo = models.BooleanField(default=True) #Automático

    objects = UsuarioManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "nombres", "id_escuela"] #Sí o sí te pide la escuela profesional al crear un usuario
    
    def __str__(self):
        return f"{self.nombres} {self.apellido_p} {self.apellido_m}" #cómo se mostará

    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador
    
    @property
    def is_active(self):
        return self.usuario_activo

    @property
    def date_joined(self):
        return self.usuario_administrador

    def save(self, *args, **kwargs): # Hasheo de contraseñas
        is_new = self._state.adding # Verifica si el objeto es nuevo (si es una creación)
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

        if is_new:
            from epica4.models import Catalogo  # Importación diferida
            Catalogo.objects.create(id_usuario=self)

    #clase meta
    class Meta:
        verbose_name = "Usuario" #Nombre con el que será visible
        verbose_name_plural = "Usuarios" #Nombre con el que será visible el plural
        