from rest_framework import serializers
from ressources.models import Categorie, Ressource
from inventaire.models import (
        Carte,
        Inventaire,
        Localisation,
        Origine,
)


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categorie
        fields = (
            'id',
            'code',
            'nom',
            'description',
            'parente',
        )

class CarteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carte
        fields = (
            'id',
            'nom',
            'description',
        )

class InventaireSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventaire
        fields = (
            'id',
            'localisation',
            'ressource',
            'nombre_total',
            'nombre_cachee',
            'date_saisie',
            'date_verifiee',
            'dofus_version',
            'origine',
            'statut',
        )


class LocalisationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Localisation
        fields = (
            'id',
            'coordonnee',
            'carte',
        )


class OrigineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Origine
        fields = (
            'id',
            'nom',
            'description',
        )


class RessourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ressource
        fields = (
            'id',
            'code',
            'nom',
            'description',
            'dofus_id',
            'categories',
        )
