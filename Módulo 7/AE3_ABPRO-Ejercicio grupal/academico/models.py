from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=200) #VARCHAR(cantidad_caracteres)
    email = models.EmailField(unique=True)
    #perfil = Objeto de Perfil
    #cursos = [Curso] -> Los cursos que el estudiante está inscrito

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

    #estudiantes que se inscribieron al curso
    estudiantes = models.ManyToManyField(
        Estudiante,
        through = 'Inscripcion', #Tabla intermediaria
        related_name = 'cursos' #estudiante.cursos = [Curso]
    )

class Perfil(models.Model):
    estudiante = models.OneToOneField(
        Estudiante,
        on_delete = models.CASCADE,
        related_name = 'perfil'
    )
    biografia = models.TextField(blank=True, null=True)
    foto = models.TextField(blank=True, null=True)
    redes = models.TextField(blank=True, null=True)

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True) #CURRENT_TIMESTAMP
    estado = models.CharField(
        max_length = 3,
        choices = [('ACT', 'Activo'), ('FIN', 'Finalizado')],
        default = 'ACT'
    )
    nota_final = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)