from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

def index(request):
    return render(request, 'index.html')

class PeliculaListView(LoginRequiredMixin, TemplateView): #ListView
    template_name = 'lista.html'