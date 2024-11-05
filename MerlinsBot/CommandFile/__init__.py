import os

# Obtenir la liste des fichiers Python dans le dossier
__all__ = []
dossier_actuel = os.path.dirname(__file__)
for fichier in os.listdir(dossier_actuel):
    if fichier.endswith(".py") and fichier != "__init__.py":
        module_name = fichier[:-3]  # Enlever le ".py"
        __all__.append(module_name)
        # Importer le module dynamiquement
        globals()[module_name] = __import__(f"CommandFile.{module_name}", fromlist=[None])
