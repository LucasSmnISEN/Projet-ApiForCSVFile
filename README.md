# Projet de Recherche de Prix Immobiliers

Ce projet Flask permet aux utilisateurs de rechercher les prix immobiliers en fonction de la ville et du quartier, d'afficher les résultats, d'ajouter de nouveaux éléments au fichier CSV et de naviguer entre les pages.

## Structure du Projet

- `app.py`: Le script principal de l'application Flask.
- `templates/`: Répertoire contenant les fichiers HTML des différentes vues.
- `static/`: Répertoire contenant les fichiers statiques (CSS dans notre cas).
- `votre_fichier.csv`: Fichier CSV contenant les données des prix immobiliers.

## Fonctionnement

### `app.py`

Le script principal qui configure et exécute l'application Flask. Il contient les routes et la logique de l'application.

#### Fonctions Principales

- `charger_donnees()`: Fonction pour charger les données depuis le fichier CSV.
- `sauvegarder_donnees(donnees)`: Fonction pour enregistrer les données dans le fichier CSV.
- `accueil()`: Route pour la page d'accueil permettant la recherche et l'affichage initial.
- `afficher_prix(ville, quartier)`: Route pour afficher les prix correspondant à la recherche.
- `ajouter_element()`: Route pour ajouter un nouvel élément au fichier CSV.

### `templates/`

Répertoire contenant les fichiers HTML pour les différentes vues de l'application.

#### `accueil.html`

La vue de la page d'accueil qui permet à l'utilisateur de sélectionner une ville et un quartier.

#### `afficher_prix.html`

La vue de la page qui affiche les résultats de recherche des prix immobiliers.

#### `ajouter_element.html`

La vue de la page qui permet à l'utilisateur d'ajouter un nouvel élément au fichier CSV.

### `static/`

Répertoire contenant les fichiers statiques, principalement le fichier CSS.

#### `styles.css`

Fichier CSS contenant les styles pour la mise en forme de l'interface utilisateur.

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/votre-utilisateur/votre-projet.git

2. Accédez au répertoire du projet :
   cd votre-projet

## Utilisation
Exécutez l'application Flask :

Copy code
python app.py

Accédez à l'application dans votre navigateur à l'adresse http://localhost:5000/.

Utilisez l'interface pour rechercher, afficher les prix, ajouter de nouveaux éléments, etc.

## Tests unitaires
Les tests sont à lancer avec le commande pytest ou python -m pytest
Ils sont écris dans le fichier test-app.py

1. Test de la page principale
2. Test de l'affichage des prix pour une ville et un quartier donnés
3. Test de l'ajout d'un nouvel élément (ville, quartier, prix) à la base de données

Les 3 tests passent avec succès.

## Auteur
Lucas SIMON & Quentin EPINAT




