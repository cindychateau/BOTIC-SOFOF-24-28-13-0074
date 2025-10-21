from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=200) #VARCHAR(cantidad_caracteres)
    email = models.EmailField(unique=True)
    #perfil = Objeto de Perfil

    def __str__(self):
        return f"Estudiante: {self.nombre}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=200) #VARCHAR(cantidad_caracteres)
    email = models.EmailField(unique=True)
    #cursos = [Curso]

    def __str__(self):
        return f"Profesor: {self.nombre}"

class Curso(models.Model):
    profesor = models.ForeignKey(
        Profesor,
        on_delete = models.CASCADE, #Si borro al profesor, se borra el curso que estaba relacionado
        related_name = 'cursos'
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Perfil(models.Model):
    estudiante = models.OneToOneField(
        Estudiante,
        on_delete = models.CASCADE,
        related_name = 'perfil'
    )
    biografia = models.TextField(blank=True, null=True)
    foto = models.TextField(blank=True, null=True)
    redes = models.TextField(blank=True, null=True)
