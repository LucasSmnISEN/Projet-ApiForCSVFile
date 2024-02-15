import unittest
from unittest.mock import patch, MagicMock
from app import app, charger_donnees, sauvegarder_donnees

class TestApp(unittest.TestCase):

    def setUp(self):
        # Configuration du client de test Flask
        self.app = app.test_client()

    # Test de la page principale ("/")
    @patch('app.open', new_callable=MagicMock, read_data="Ville,Quartier,Prix au m²\nParis,Marais,1000\n")
    def test_main_page(self, mock_file_open):
        # Effectuer une requête GET sur la page principale
        response = self.app.get('/')
        # Vérifier que le code de statut de la réponse est 200 (OK)
        self.assertEqual(response.status_code, 200)

    # Test de l'affichage des prix pour une ville et un quartier donnés
    @patch('app.open', new_callable=MagicMock) 
    def test_afficher_prix(self, mock_file_open):
        # Données de test pour charger_donnees
        donnees = [{'Ville': 'Paris', 'Quartier': 'Marais', 'Prix au m²': '1000'}]
        # Mock de la fonction charger_donnees pour renvoyer les données de test
        charger_donnees.return_value = donnees

        # Effectuer une requête GET pour afficher les prix pour Paris/Marais
        response = self.app.get('/Paris/Marais')
        # Vérifier que le code de statut de la réponse est 200 (OK)
        self.assertEqual(response.status_code, 200)

    # Test de l'ajout d'un nouvel élément (ville, quartier, prix) à la base de données
    @patch('app.open', new_callable=MagicMock)        
    @patch('app.sauvegarder_donnees')
    def test_ajouter_element(self, sauvegarder_donnees_mock, mock_file_open):   
        # Configuration de la fonction charger_donnees pour renvoyer une liste vide (pas de données)
        charger_donnees.return_value = []

        # Effectuer une requête POST pour ajouter un nouvel élément
        response = self.app.post('/ajouter_element', data={'ville': 'Paris', 'quartier': 'Marais', 'prix': '1000'})
        # Vérifier que le code de statut de la réponse est 302 (redirection après ajout)
        self.assertEqual(response.status_code, 302)  

        # Vérifier que les données sont sauvegardées correctement
        donnees = [{'Ville': 'Paris', 'Quartier': 'Marais', 'Prix au m²': '1000'}]
        # Vérifier que la fonction sauvegarder_donnees est appelée une fois avec les données spécifiées
        sauvegarder_donnees_mock.assert_called_once_with(donnees)
        
    
if __name__ == '__main__':
    unittest.main()
