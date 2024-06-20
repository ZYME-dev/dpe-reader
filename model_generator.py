"""
    Génération auto des models de données DPE à partir du schéma xsd,
    selon le numéro de version.

    Plusieurs versions du schéma coexistent sur le plateforme de l'observatoire :
    https://gitlab.com/observatoire-dpe/observatoire-dpe/-/tree/master/modele_donnee?ref_type=heads

    help : https://xsdata.readthedocs.io/en/latest/codegen/intro/
"""

import os
import subprocess

DPE_VERSIONS = ["2", "2.2", "2.3", "2.4"]
AUDIT_VERSION = ["v2.0", "v2.1", "regv1.1", "regv1.2"]

def generate_dpe_models(version_ids):

    for v in DPE_VERSIONS:
    # for v in ["2.4"]:

        schema_path = f"assets/schemas/DPEv{v}.xsd"
        model_filename = f"dpe_v{v.replace('.','_')}"

        subprocess.run([
            "xsdata", 
            "--debug",
            "--package", model_filename, 
            "--output", "dataclasses",                  # [dataclasses]
            "--structure-style", "single-package",      # [filenames|namespaces|clusters|single-package|namespace-clusters]
            "--docstring-style", "Google",              # [reStructuredText|NumPy|Google|Accessible|Blank]
            schema_path
            ])
        
        os.replace(f"{model_filename}.py", f"models/{model_filename}.py")
        os.remove("__init__.py")


if __name__ == "__main__":

    generate_dpe_models(DPE_VERSIONS)



