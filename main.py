
from cgitb import reset
from fastapi import FastAPI
from  mysql_requete import *
import uvicorn
import pandas as pd 
import os



# Nomme l'Api
app = FastAPI(title='API',
    description="API pour intégration et séléction de données dans mysql",
    version="1",
    openapi_tags=[
    {
        'name': 'Status',
        'description': "Vérifie si l'API est opérationnel "
    },
    {
        'name': 'Intégration',
        'description': 'Intégration les données du fichier .csv dans la bd mysql '
    },
    {
        'name': 'Database',
        'description': 'Affiche les databases presentes dans mysql '
    },
    {
        'name':'Requete SELECT',
        'description': 'Permet de faire un requete SELECT simple pour intérroger la bd'
    },
    {
        'name': 'Requete INSERT',
        'description': 'Permet de faire un requete INSERT pour ajouter une ligne à la bd'
    },
])



# ========== Recuperation du chemin du repertoire ==========
path = os.path.realpath(__file__)               # donne le chemin du fichier app.py  xx/xx/xx/app.py
#print("Le chemin du script est : " + path)

chemin =os.path.split(path)                     # Séparer le chemin et le nom de fichier    [xx/xx/xx , app.py]  
path =   chemin[0] 
#print(chemin[0])


# ========== Retourne le status de l'API ==========
#renvoie 1 si l'API fonctionne
@app.get('/status',name="Vérification du fonctionnement de l'API", tags=['Status'])
def retourne_status():
        return 'API opérationnel'

# ========== Permet l'intégration des données dans la base ==========
@app.get('/integration',name="Intégration des données .csv", tags=['Intégration'])
def integration():
        try:    
                # ===== Supprime la base si elle existe ===== 
                suppression(database="stack_network_links",host="localhost",user="root",password="azerty",sql="DROP DATABASE IF EXISTS stack_network_links")
                # ===== Créé la base =====
                create_bdd(database="stack_network_links",host="localhost",user="root",password="azerty")
                # ===== Création de la table et integration des donnée depuis un csv =====
                df = pd.read_csv(path+"/stack_network_links.csv", sep =",")
                df_to_mysql(database ="stack_network_links", host="localhost",user="root",password="azerty",df=df)
              
                return "Integration des données ok "

        except Exception as e:
                erreur="Erreur , app.py ; integration() , erreur dans l'intégration des données"
                print(erreur,e)
                return erreur 


# ========== Permet voir les bases presente dans mysql ==========
@app.get('/database',name="Vidualisation des database présentes dans mysql", tags=['Database'])
def database():

        try:
                resultat = show_bdd(host="localhost",user="root",password="azerty")
                print(resultat)
                return {"liste data base":resultat}

        except Exception as e:
                erreur="Erreur , app.py ; show_database() , erreur dans la visualisation des databases "
                print(erreur,e)
                return erreur 


# ========== Requete SELECT sur la table  ==========
@app.get('/requete_select',name="Requete de selection ", tags=['Requete SELECT'])
def rq_select(select =None , FROM = "stack_network_links" ,where = None):

        try:
                # ===== Mise en forme de la requete sql ====
                if where == None:
                        sql = "SELECT "+select+" FROM "+FROM+""
                else:     
                        #sql = "SELECT * FROM stack_network_links"
                        sql = "SELECT "+select+" FROM "+FROM+" WHERE "+where+""

                #print("SELECT", SELECT);print("FORM",FROM);print("sql",sql)


                # ===== Requete sql sur la base mysql =====
                res = requete_select(database ="stack_network_links", host="localhost",user="root",password="azerty",sql=sql )

                # ===== Mise en forme dans un tableau de la variable "SELECT" =====
                tab_select = select.replace(" ","")
                print(tab_select)

                tab_select2 = tab_select.replace(","," ")
                print(tab_select2)

                tab_select = tab_select2.split()
                print(tab_select)     

                # ===== Creation d'un dataframe pour l'afficher le resultat =====
                if select == "*":
                        res = pd.DataFrame(res,columns = ['source','target','value'])
                if select != "*":
                        res = pd.DataFrame(res,columns = tab_select)
                #print(res)

                return res

        except Exception as e:
                erreur="Erreur , app.py ; rq_select() , erreur dans la requete de selection"
                print(erreur,e)
                return erreur 

# ========== Requete INSERT sur la table ==========
@app.get('/requete_insert',name="Requete pour insertion de donnée ", tags=['Requete INSERT'])
def rq_insert(val_source =None , val_target = None ,val_value = None):

        try:
                sql= "INSERT INTO stack_network_links (source,target,value) VALUES ('"+val_source+"','"+val_target+"',"+val_value+")"
                #print(sql)

                res=requete_insert(database ="stack_network_links", host="localhost",user="root",password="azerty",sql=sql)
                return "requete insert ok"

        except Exception as e:
                erreur="Erreur , app.py ; rq_insert() , erreur dans la requete insert "
                print(erreur,e)
                return erreur 


# ========== rendre exécutable. ==========

#La méthode .run permet  de lancer l'application sur un serveur de développement local , à chaque lancement du fichier.py
#if __name__ == '__main__':
#    uvicorn.run(app, host="0.0.0.0" , port=8001)
