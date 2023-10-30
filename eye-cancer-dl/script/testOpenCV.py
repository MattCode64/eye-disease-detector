import cv2
import glob

# Spécifiez le chemin vers le dossier contenant vos images
chemin_dossier = (r"C:\Data\Projet CODE\Code Python\DataCamp "
                  r"Code\data\eyes-dataset\Evaluation_Set\Evaluation_Set\Validation\*.png")

# Utilisez glob pour obtenir la liste de tous les fichiers images dans le dossier spécifié
fichiers_images = glob.glob(chemin_dossier)

for fichier in fichiers_images:
    # Lire l'image
    image = cv2.imread(fichier)
    print("Affichage de l'image {}".format(fichier))

    # Afficher l'image
    cv2.imshow('Image', image)

    # Attendez que l'utilisateur appuie sur une touche et fermez l'image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
