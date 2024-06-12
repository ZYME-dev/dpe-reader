# dpe-reader
Une demo app pour montrer comment exploiter les xml de l'Observatoire DPE

## Données du DPE

Pour récupérer un DPE de l'[Observatoire DPE-AUDIT](https://observatoire-dpe-audit.ademe.fr/accueil), un simple call sur l'url suivante suffit :

````
https://observatoire-dpe-audit.ademe.fr/pub/dpe/${ID}/xml
````

## Génération du modèle à partir du xsd

Installation du package `xsdata-pydantic`. Attention, sur mon mac il faut échapper les brackets.

````
pip install xsdata\[cli,lxml,soap\]
pip install xsdata-pydantic\[cli,lxml,soap\]
````

Commande pour générer automatiquement le modèle `models.py` à partir du schéma de l'observatoire DPE `DPEv2.4.xsd`

````
xsdata assets/DPEv2.2.xsd --package models_dataclass --structure-style single-package
xsdata assets/DPEv2.2.xsd --output pydantic --package models_pydantic --structure-style single-package
````

## Chargement d'un DPE

On utilise un DPE [n° 2344E0308327N](https://observatoire-dpe-audit.ademe.fr/afficher-dpe/2344E0308327N) récupéré sur le site de l'observatoire.

````






