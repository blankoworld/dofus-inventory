from rest_framework import filters, viewsets

from inventaire.models import (
    Carte,
    Inventaire,
    Localisation,
    Origine,
)
from ressources.models import Categorie, Ressource

from api.serializers import (
    CarteSerializer,
    CategorySerializer,
    InventaireSerializer,
    LocalisationSerializer,
    OrigineSerializer,
    RessourceSerializer,
)

import django_filters


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorySerializer

class CarteViewSet(viewsets.ModelViewSet):
    queryset = Carte.objects.all()
    serializer_class = CarteSerializer


class InventaireViewSet(viewsets.ModelViewSet):
    queryset = Inventaire.objects.filter(
        dofus_version='2.35',
    )
    serializer_class = InventaireSerializer

class OrigineViewSet(viewsets.ModelViewSet):
    queryset = Origine.objects.all()
    serializer_class = OrigineSerializer


class LocalisationFilter(django_filters.FilterSet):
    class Meta:
        model = Localisation
        fields = ['coordonnee']


class LocalisationViewSet(viewsets.ModelViewSet):
    queryset = Localisation.objects.all()
    serializer_class = LocalisationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = LocalisationFilter
    search_fields = ['coordonnee']


class RessourceViewSet(viewsets.ModelViewSet):
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer
