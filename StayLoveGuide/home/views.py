from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.conf import settings
from django.db import models
from .models import HomePage


class HomeView(TemplateView):
    template_name = 'home/home.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = HomePage.objects.first()
        return context

