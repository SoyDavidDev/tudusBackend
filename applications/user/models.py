# Django imports
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # username = models.CharField('Usuario',max_length=50, unique=True)
    # first_name = models.CharField('Nombre',max_length=50)
    # last_name = models.CharField('Apellidos',max_length=50)
    # email = models.EmailField('Email',max_length=50, unique=True)
    # is_active = models.BooleanField('Activo',default=True)

    # Los campos ya están definidos en AbstractUser
    # PermissionsMixin añade los campos is_staff y is_superuser
    # AbstractBaseUser añade el campo password
    # AbstractUser añade los campos username, first_name, last_name, email, is_active
    # AbstractUser hereda de AbstractBaseUser y PermissionsMixin
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-id']
    

    def __str__(self):
        return self.username
