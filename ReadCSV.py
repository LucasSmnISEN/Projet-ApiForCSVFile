import pandas as pd

def lister_villes():
    df = pd.read_csv('prix_immobilier_fictif.csv')
    return df['Ville'].unique().tolist()

def lister_quartiers():
    df = pd.read_csv('prix_immobilier_fictif.csv')
    return df['Quartier'].unique().tolist()

def lister_prix():
    df = pd.read_csv('prix_immobilier_fictif.csv')
    return df['Prix au m²'].unique().tolist()


print(lister_quartiers())