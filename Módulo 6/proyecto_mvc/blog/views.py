from django.shortcuts import render, redirect
#TemplateView : mostrar una plantilla
#ListView: muestra un listado de un model
from django.views.generic import ListView, TemplateView #CreateView, #UpdateView, #DeleteView
from .models import Post

#LoginRequiredMixin: inicio de sesión requerido = @login_required
#PermissionRequiredMixin: solo muestra la página si tiene los permisos indicados permision_required = @permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

#Pública: cualquiera puede entrar
#Mostrar una lista de las publicaciones guardadas
class ListaPosts(ListView):
    model = Post
    template_name = 'lista_posts.html'
    #object_list = lista del modelo
    #query_set -> Post.objects.all()

#Privada: aquellos que iniciaron sesión pueden ver
class MisPosts(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'mis_posts.html'

    def get_queryset(self):
        return Post.objects.filter(autor=self.request.user)

#Privada + Permisos: aquellos que iniciaron sesión Y tienen permisos
class EditarPost(PermissionRequiredMixin, TemplateView):
    template_name = 'editar_post.html'
    permission_required = 'blog.change_post'

    #Función para personalizar la página de 403 Forbiden
    def handle_no_permission(self):
        return redirect('pagina_prohibida')

#Privada + Permisos: ver_posts_exclusivos
class PostsExclusivos(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = "posts_exclusivos.html"
    permission_required = "blog.ver_posts_exclusivos" #view_post_exclusivos

    #Función para personalizar la página de 403 Forbiden
    def handle_no_permission(self):
        return redirect('pagina_prohibida')


class PaginaProhibida(TemplateView):
    template_name = "pagina_prohibida.html"
