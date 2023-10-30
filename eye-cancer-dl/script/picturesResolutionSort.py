from PIL import Image
import os
import shutil

"""
Entrée :
Le script traite les images contenues dans un dossier source spécifié. Le chemin de ce dossier est stocké dans la variable source_folder. Dans le code fourni, trois dossiers différents sont mentionnés (pour les ensembles de validation, de test, et d'entraînement), mais seul le chemin pour l'ensemble d'entraînement (Training_set) est activé (non-commenté).

Traitement :
Définition des Résolutions Cibles : Le script définit une liste de résolutions cibles (target_resolutions), dans ce cas, deux résolutions spécifiques.

Parcours des Fichiers : Il parcourt chaque fichier dans le dossier source.

Filtrage et Copie :

Pour chaque fichier se terminant par .png dans le dossier source, le script ouvre l'image et extrait ses dimensions (largeur et hauteur).
Si la résolution de l'image correspond à l'une des résolutions cibles, l'image est alors copiée dans le dossier de destination.
Sortie :
Le script copie les fichiers image du dossier source vers le dossier de destination, mais uniquement ceux dont les dimensions correspondent aux résolutions cibles spécifiées. Le chemin du dossier de destination est stocké dans la variable dest_folder. Ici, il est configuré pour un chemin correspondant à l'ensemble d'entraînement trié (Training_set).
"""
# Chemin du dossier source contenant les images

# Validation_set
# source_folder = (r"C:\Data\Projet CODE\Code Python\DataCamp "
#                  r"Code\data\eyes-dataset\Evaluation_Set\Evaluation_Set\Validation")

# Test_set
# source_folder = r"C:\Data\Projet CODE\Code Python\DataCamp Code\data\eyes-dataset\Test_Set\Test_Set\Test"

# Training_set
source_folder = r"C:\Data\Projet CODE\Code Python\DataCamp Code\data\eyes-dataset\Training_Set\Training_Set\Training"

# Chemin du dossier de destination où les images seront copiées

# validation_set
# dest_folder = (r"C:\Data\Projet CODE\Code Python\DataCamp "
#                r"Code\data\eyes-dataset\Evaluation_Set\Evaluation_Set\ValidationSorted")

# Test_set
# dest_folder = (r"C:\Data\Projet CODE\Code Python\DataCamp "
#                r"Code\data\eyes-dataset\Test_Set\Test_Set\TestSorted")

# Training_set
dest_folder = (r"C:\Data\Projet CODE\Code Python\DataCamp "
               r"Code\data\eyes-dataset\Training_Set\Training_Set\TrainingSorted")

# Les résolutions cibles
target_resolutions = [(2144, 1424), (2048, 1536)]

# Parcourir chaque fichier dans le dossier source
for filename in os.listdir(source_folder):
    if filename.endswith(".png"):
        filepath = os.path.join(source_folder, filename)

        # Ouvrir l'image et obtenir ses dimensions
        with Image.open(filepath) as img:
            width, height = img.size

            # Vérifier si la résolution de l'image est l'une des résolutions cibles
            if (width, height) in target_resolutions:
                # Copier l'image dans le dossier de destination
                shutil.copy(filepath, os.path.join(dest_folder, filename))

print("Images triées et copiées pour les résolutions cibles du dossier source vers le dossier de destination."
      "Dossier source: {}".format(source_folder)
      + "\nDossier de destination: {}".format(dest_folder))
