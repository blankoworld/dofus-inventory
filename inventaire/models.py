# -*- coding: UTF-8 -*-
from django.db import models
from django.utils import timezone

from ressources.models import Ressource

from inventaire.validators import validation_coordonnee

from dmap import __dofus_version__ as dofus_version

class Origine(models.Model):
    nom = models.CharField(max_length=120)
    description = models.TextField()
    unique_id = models.CharField(max_length=256, null=True, blank=True)

    def __unicode__(self):
        return self.nom

    def __str__(self):
        return self.nom

def origine_par_defaut():
    return Origine.objects.filter(nom='WEB').first()

class Carte(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.nom

    def __str__(self):
        return self.nom

def espace_par_defaut():
    return Carte.objects.get(nom='Amakna')

class Localisation(models.Model):
    coordonnee = models.CharField(
        max_length=9,
        validators=[validation_coordonnee],
        help_text="Doit ressembler à : -12,48, -20,-45, 2,-10 ou encore 4,5",
        db_index=True)
    mapid = models.CharField(max_length=10, blank=True, null=True)
    carte = models.ForeignKey(Carte, default=espace_par_defaut)

    def __unicode__(self):
        return '%s' % self.coordonnee

    def __str__(self):
        return '%s' % self.coordonnee

class Inventaire(models.Model):
    AUCUN = 0
    VALIDE = 1
    REFUSE = 2
    CHOIX = (
        (AUCUN, ''),
        (VALIDE, 'Valide'),
        (REFUSE, 'Refusé')
    )

    nombre_total = models.PositiveIntegerField('Total')
    nombre_cachee = models.PositiveIntegerField('Quantité cachée', null=True, blank=True)
    date_verifiee = models.DateTimeField(null=True, blank=True)
    date_saisie = models.DateTimeField(default=timezone.now)
    dofus_version = models.CharField(max_length=10, default=dofus_version)
    statut = models.IntegerField(
        choices=CHOIX,
        default=AUCUN)
    # Link with other models
    ressource = models.ForeignKey(Ressource, blank=False, null=False)
    origine = models.ForeignKey(Origine, blank=False, null=False, default=origine_par_defaut)
    localisation = models.ForeignKey(Localisation, blank=False, null=False)

    def __unicode__(self):
        return self.ressource.nom

    def __str__(self):
        return self.ressource.nom
