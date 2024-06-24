# dpe-reader
Une demo app en python/streamlit pour montrer comment exploiter les xml de l'Observatoire DPE

## Ressources

Le méthode 3CL, décrite dans [ce PDF](https://rt-re-batiment.developpement-durable.gouv.fr/IMG/pdf/consolide_annexe_1_arrete_du_31_03_2021_relatif_aux_methodes_et_procedures_applicables.pdf), est la base de calcul pour les DPE.

On trouve sur le [gitlab de l'Observatoire DPE](https://gitlab.com/observatoire-dpe/observatoire-dpe/-/blob/master/README.md) les différentes version des schémas de données (au format xsd).

- [PDF Méthode 3CL v1.3](https://rt-re-batiment.developpement-durable.gouv.fr/IMG/pdf/consolide_annexe_1_arrete_du_31_03_2021_relatif_aux_methodes_et_procedures_applicables.pdf)
- [Légifrance valeurs GES](https://www.legifrance.gouv.fr/download/pdf?id=doxMrRr0wbfJVvtWjfDP4gHzzERt1iX0PtobthCE6A0=)
- [CSTB Procédure de certification](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjH-fG2-s7_AhXLaqQEHTP8CwMQFnoECA4QAQ&url=https%3A%2F%2Frt-re-batiment.developpement-durable.gouv.fr%2FIMG%2Fpdf%2Freglement_evaluation_logiciel_dpe_2021_-_audit_energetique-13122022_v2.pdf&usg=AOvVaw3SWv8drhqbgMMT8K9m6a2C&opi=89978449)
- [Valeurs des étiquettes énergétiques](https://docs.google.com/spreadsheets/d/1QVXUOLP8aJukA-PLBGyVB0ZJTWmLEE1WbflXUfsT_jU/edit#gid=0)


## Données du DPE

Pour récupérer un DPE de l'[Observatoire DPE-AUDIT](https://observatoire-dpe-audit.ademe.fr/accueil), un simple call sur l'url suivante suffit :

````
https://observatoire-dpe-audit.ademe.fr/pub/dpe/${ID}/xml
````

## Génération auto du modèle de données à partir du .xsd

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


## Dev

* see [RUFF](https://docs.astral.sh/ruff/)
* see [BLACK](https://github.com/psf/black?tab=readme-ov-file)
* see [TYPER](https://typer.tiangolo.com)
* see [MYPY](https://github.com/python/mypy)


[Packaging](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

### imports

absolute / relative

[The Definitive Guide to Python import Statements](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html)

https://iq-inc.com/importerror-attempted-relative-import/

