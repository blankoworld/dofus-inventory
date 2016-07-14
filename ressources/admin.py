# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Ressource, Categorie


class RessourceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'code', 'description')
    search_fields = ['nom', 'code']
    ordering = ['nom']


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('parente', 'nom', 'code', 'description')
    search_fields = ['nom', 'code']
    ordering = ['nom']
    list_filter = ('parente',)


admin.site.register(Ressource, RessourceAdmin)
admin.site.register(Categorie, CategorieAdmin)
