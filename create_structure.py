import os

# Dictionnaire pour la structure des fichiers
file_structure = {
    "deployments": {
        "yaml-standard": {
            "fastapi": ["deployment.yaml", "service.yaml", "ingress.yaml"],
            "postgresql": ["deployment.yaml", "service.yaml"],
            "pgadmin": ["deployment.yaml", "service.yaml"]
        },
        "helm": {
            "fastapi": [],
            "postgresql": [],
            "pgadmin": []
        },
        "kustomize": {
            "fastapi": [],
            "postgresql": [],
            "pgadmin": []
        }
    }
}

# Fonction pour créer les répertoires et fichiers
def create_structure(base_path, structure):
    for folder, content in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        if isinstance(content, dict):
            create_structure(folder_path, content)
        else:
            for file in content:
                open(os.path.join(folder_path, file), 'w').close()

# Créer la structure de fichiers
base_path = "."
create_structure(base_path, file_structure)

print("Structure de fichiers et dossiers créée avec succès.")
