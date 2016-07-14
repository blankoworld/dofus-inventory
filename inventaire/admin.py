# -*- coding: UTF-8 -*-
from django.contrib import admin

from .models import Origine, Carte, Localisation, Inventaire


class OrigineAdmin(admin.ModelAdmin):
    model = Origine
    list_display = ['nom', 'description']
    ordering = ['nom']


class InventaireInline(admin.TabularInline):
    model = Inventaire
    extra = 1
    fields = ('ressource', 'nombre_total', 'nombre_cachee', 'statut')
    readonly_fields = ('statut',)


class LocalisationAdmin(admin.ModelAdmin):
    model = Localisation
    fields = ('coordonnee', 'carte', 'mapid')
    list_filter = ['carte']
    list_display = ['coordonnee', 'carte']
    search_fields = ['coordonnee']

    inlines = [InventaireInline,]


class CarteAdmin(admin.ModelAdmin):
    model = Carte
    ordering = ['nom']
    list_display = ['nom', 'description']


admin.site.register(Origine, OrigineAdmin)
admin.site.register(Carte, CarteAdmin)
admin.site.register(Localisation, LocalisationAdmin)
