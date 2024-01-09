import csv
import pandas as pd
from flask import *
from ReadCSV import *

app = Flask(__name__)

# Charger les données depuis le fichier CSV
def charger_donnees():
    donnees = []
    with open('prix_immobilier_fictif.csv', newline='', encoding='utf-8') as csvfile:
        lecteur = csv.DictReader(csvfile)
        for ligne in lecteur:
            donnees.append(ligne)
    return donnees

# Enregistrer les données dans le fichier CSV
def sauvegarder_donnees(donnees):
    with open('prix_immobilier_fictif.csv', 'w', newline='', encoding='utf-8') as csvfile:
        champs = ['Ville', 'Quartier', 'Prix au m²']
        ecrivain = csv.DictWriter(csvfile, fieldnames=champs)
        ecrivain.writeheader()
        ecrivain.writerows(donnees)


#Main page for search
@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        ville = request.form.get('ville')
        quartier = request.form.get('quartier')
        return redirect(url_for('afficher_prix', ville=ville, quartier=quartier))
    
    else:
        return render_template('home.html', villes=lister_villes(), quartiers=lister_quartiers())

# Endpoint pour rechercher le prix en fonction de la ville et du quartier
@app.route('/<ville>/<quartier>', methods=['GET'])
def afficher_prix(ville,quartier):

    if not ville or not quartier:
        return jsonify({'erreur': 'Veuillez fournir à la fois la ville et le quartier'}), 400

    donnees = charger_donnees()

    resultats = [{'Prix': x['Prix au m²']} for x in donnees if x['Ville'] == ville and x['Quartier'] == quartier]

    if resultats:
        return render_template('afficher_prix.html', ville=ville, quartier=quartier, resultats=resultats)
    else:
        return render_template('afficher_prix.html', erreur='Aucun prix trouvé pour la ville et le quartier spécifiés')


# Nouvelle route pour ajouter un élément
@app.route('/ajouter_element', methods=['GET', 'POST'])
def ajouter_element():
    if request.method == 'POST':
        ville = request.form.get('ville')
        quartier = request.form.get('quartier')
        prix = request.form.get('prix')

        if not ville or not quartier or not prix:
            return jsonify({'erreur': 'Veuillez remplir tous les champs'}), 400

        donnees = charger_donnees()
        nouvelle_donnee = {'Ville': ville, 'Quartier': quartier, 'Prix au m²': prix}
        donnees.append(nouvelle_donnee)
        sauvegarder_donnees(donnees)

        return redirect(url_for('main_page'))

    else:
        return render_template('ajouter_element.html')
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
