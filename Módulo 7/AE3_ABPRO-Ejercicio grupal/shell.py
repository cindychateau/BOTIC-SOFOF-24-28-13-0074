from academico.models import Profesor, Curso, Estudiante, Inscripcion, Perfil

prof1 = Profesor.objects.create(nombre="Ricardo", email="ricardo@skillnest.com")
prof2 = Profesor.objects.create(nombre="Cynthia", email="cynthia@skillnest.com")

'''
prof1 = Profesor(nombre="Ricardo", email="ricardo@skillnest.com")
prof1.save()
'''

curso1 = Curso.objects.create(nombre="Fundamentos de la Web", descripcion="HTML, CSS, JS", profesor=prof1)
curso2 = Curso.objects.create(nombre="Fullstack Python", descripcion="Python, POO, Django", profesor=prof1)
curso3 = Curso.objects.create(nombre="Fullstack Java", descripcion="Java, POO, SpringBoot", profesor=prof2)

est1 = Estudiante(nombre="Elena de Troya", email="elena@skillnest.com")
est2 = Estudiante(nombre="Juana de Arco", email="juana@skillnest.com")
est1.save()
est2.save()

curso1 = Curso.objects.get(id=1) #Fundamentos
curso2 = Curso.objects.get(id=2) #Python
curso3 = Curso.objects.get(id=3) #Java

est1 = Estudiante.objects.get(id=1) #Elena
est2 = Estudiante.objects.get(id=2) #Juana

#Inscribir a Elena en Fundamentos de la web y darle su nota final, Fullstack python
Inscripcion.objects.create(estudiante=est1, curso=curso1, nota_final=1.1, estado='FIN')
Inscripcion.objects.create(estudiante=est1, curso=curso2)

#Inscribir a Juana en Fullstack python y fullstack java
Inscripcion.objects.create(estudiante=est2, curso=curso2)
Inscripcion.objects.create(estudiante=est2, curso=curso3)

ins3 = Inscripcion.objects.get(id=3)
ins3.estado = 'FIN'
ins3.nota_final = 7
ins3.save()

Perfil.objects.create(estudiante=est1, biografia="Amante de lo aesthetic, le gusta el diseño de páginas web")

est1.delete()