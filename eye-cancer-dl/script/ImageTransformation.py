import cv2
import pandas as pd
import glob
import time

"""
Code to convert each images to RGB and save them in a CSV file
"""

# Liste des chemins source et destination
paths = [
    {
        "source": (r"C:\Data\Projet CODE\Code Python\DataCamp "
                   r"Code\data\eyes-dataset\Evaluation_Set\Evaluation_Set\ValidationSorted\*.png"),
        "dest": (r"C:\Data\Projet CODE\Code Python\DataCamp "
                 r"Code\data\eyes-dataset\Evaluation_Set\Evaluation_Set\ValidationSet.csv")
    },
    {
        "source": (r"C:\Data\Projet CODE\Code Python\DataCamp "
                   r"Code\data\eyes-dataset\Test_Set\Test_Set\TestSorted\*.png"),
        "dest": (r"C:\Data\Projet CODE\Code Python\DataCamp "
                 r"Code\data\eyes-dataset\Test_Set\Test_Set\TestSet.csv")
    },
    {
        "source": (r"C:\Data\Projet CODE\Code Python\DataCamp "
                   r"Code\data\eyes-dataset\Training_Set\Training_Set\TrainingSorted\*.png"),
        "dest": (r"C:\Data\Projet CODE\Code Python\DataCamp "
                 r"Code\data\eyes-dataset\Training_Set\Training_Set\TrainingSet.csv")
    }
]


def process_images(source, dest):
    print(f"Processing images from {source}...")

    start_time = time.time()
    files = glob.glob(source)
    images = [cv2.cvtColor(cv2.imread(file), cv2.COLOR_BGR2RGB) for file in files]

    print("Done processing images")

    end_time = time.time()

    print(end_time - start_time)

    ids = [int(file.split('\\')[-1].split('.png')[0]) for file in files]

    data = {'ID': ids, 'Pixels_data': images}
    df = pd.DataFrame(data)
    # sort by ID
    df = df.sort_values(by='ID')
    df.to_csv(dest, sep=',', index=False, header=True)

    print(f"Data saved to {dest}")


for path in paths:
    process_images(path['source'], path['dest'])



"""
Entrée :
Il prend en entrée un ensemble d'images au format .png localisées dans les chemins spécifiés par la clé source dans la liste paths. Chaque chemin source utilise un joker *.png pour sélectionner toutes les images PNG dans le dossier spécifié.

Traitement :
Chargement des Images : Pour chaque image dans le chemin source, l'image est chargée en mémoire.
Conversion de Couleur : Chaque image chargée est convertie de BGR (Bleu, Vert, Rouge, un format standard pour OpenCV) en RGB.
Extraction d'Identifiants : Les identifiants (IDs) sont extraits des noms de fichier des images. Ces IDs sont supposés être les parties numériques des noms de fichier.
Création d'un DataFrame : Un DataFrame Pandas est créé avec deux colonnes : ID et Pixels_data, où ID contient les identifiants des images et Pixels_data contient les données d'image converties en RGB.
Tri et Enregistrement : Le DataFrame est trié par ID et ensuite enregistré dans un fichier CSV au chemin spécifié par dest.

Sortie :
Le script génère un fichier CSV pour chaque chemin spécifié dans paths. Chaque fichier CSV contient deux colonnes :

"""