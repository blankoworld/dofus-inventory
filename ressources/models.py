# -*- coding: UTF-8 -*-

from django.db import models

class Categorie(models.Model):
    code = models.CharField(max_length=120)
    nom = models.CharField(max_length=200)
    description = models.TextField()
    # relation réflexive (récursive)
    parente = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.nom

    def __str__(self):
        return self.nom

class Ressource(models.Model):
    code = models.CharField(max_length=120)
    nom = models.CharField(max_length=200)
    description = models.TextField()
    dofus_id = models.CharField('ID Dofus', max_length=10, blank=True)
    # une ressource appartient de 1 à N catégories
    categories = models.ManyToManyField(Categorie)

    def __unicode__(self):
        return self.nom

    def __str__(self):
        return self.nom

