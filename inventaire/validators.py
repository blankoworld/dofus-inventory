from django.core.exceptions import ValidationError
import re

def validation_coordonnee(valeur):
    """
    Verification de la coordonnée. Elle est de la forme : X,Y où : 
      - X et Y est un nombre
      - X, ou Y, peuvent être négatifs
      - X et Y doivent être des entiers
    """
    regex = re.compile('^(-?\d{1,3},-?\d{1,3})$')
    if not regex.search(valeur):
        raise ValidationError(
             '%(valeur)s doit être sous la forme -28,-32',
             params={'valeur': valeur})
