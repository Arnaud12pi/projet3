#==================================================
#============= Manipulation de mysql  =============
#==================================================

# pip install mysqlclient
# pip install mysql-connector-python

import mysql.connector


def conn(database=None,host=None,user=None,password=None):
    '''
        Fonction qui permet de lancer une connexion à mysql

        Parametre :
            database    : Nom de la base de données si elle existe
            host        : Nom ou ip de l'hote où est mysql exemple : "localhost ou 127.0.0.1"
            user        : Login de connexion 
            password    : Mot de passe de connexion 
a
        renvoie :
            Si la connexion fonction => renvoie un message  de validation 
            Si la connexion ne fonction pas => renvoie un message d'erreur 

        Exemple d'appel :
            res=conn(database="mydatabase",host="localhost",user="root",password="azerty")          
    '''
    
    try:
        mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
        )
        resultat="Connection ok "
        return resultat

    except Exception as e:
        erreur ="Echec de la connexion "
        print(erreur,e)
        return erreur 



def create_bdd(database=None,host=None,user=None,password=None):
    '''
        Fonction qui permet de Créer une bdd dans mysql

        Parametre :
            database    : Nom de la base de données à créer
            host        : Nom ou ip de l'hote où est mysql exemple : "localhost ou 127.0.0.1"
            user        : Login de connexion 
            password    : Mot de passe de connexion 

        renvoie :
            Si la connexion fonction => renvoie un message 
            Si la connexion ne fonction pas => renvoie un message d'erreur 

        Exemple d'appel :
            res=create_bdd(database="db1",host="localhost",user="root",password="azerty")     
    '''
    try:
        mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password
        )

        mycursor = mydb.cursor()

        #mycursor.execute("CREATE DATABASE nom_bd ")
        mycursor.execute("CREATE DATABASE "+database+" ")
        resultat="Création database "+database+" ok "
        return resultat

    except Exception as e:
        erreur=("Erreur :  create_bdd() ")
        print(erreur,e)
        return erreur 


def show_bdd(host=None,user=None,password=None):
    '''
        Fonction qui permet de retourner la liste des noms des bd mysql

        Parametre :
            host        : Nom ou ip de l'hote où est mysql exemple : "localhost ou 127.0.0.1"
            user        : Login de connexion 
            password    : Mot de passe de connexion 

        renvoie :
            Si la connexion fonction => renvoie la liste des bd 
            Si la connexion ne fonction pas => renvoie un message d'erreur 

        Exemple d'appel :
            res=show_bdd(host="localhost",user="root",password="azerty")      
    '''
    try:
        bdd_nom = []

        mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password
        )

        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        for x in mycursor:
            bdd_nom.append(x)
            #print(x)

        resultat=bdd_nom
        return resultat

    except Exception as e:
        erreur="Erreur :  show_bdd()"
        print(erreur)
        return erreur 

def suppression(database=None,host=None,user=None,password=None,sql=None):
    '''
        Fonction qui permet une table dans une bd

        Parametre :
            database    : Nom de la base de données si elle existe
            host        : Nom ou ip de l'hote où est mysql exemple : "localhost ou 127.0.0.1"
            user        : Login de connexion 
            password    : Mot de passe de connexion 
            sql         : Requete sql à executer exemple => Supprime une table ou db: "DROP TABLE customers"  /  "DROP DATABASE db1"

        renvoie :
            Si la connexion fonction => renvoie un message  de validation 
            Si la connexion ne fonction pas => renvoie un message d'erreur 

        Exemple d'appel :
            res=suppression(database="db1",host="localhost",user="root",password="azerty",sql= "DROP DATABASE db1")       
    '''
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
            )

        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()

        resultat = "requetes executé"
        return resultat

    except Exception as e:
        erreur="Erreur :  suppression()"
        print(erreur,e)
        return erreur 

def create_table(database=None,host=None,user=None,password=None,sql=None):
    '''
        Fonction qui permet une table dans une bd

        Parametre :
            database    : Nom de la base de données si elle existe
            host        : Nom ou ip de l'hote où est mysql exemple : "localhost ou 127.0.0.1"
            user        : Login de connexion 
            password    : Mot de passe de connexion 
            sql         : Requete sql à executer exemple => Creation de table : "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"

        renvoie :
            Si la connexion fonction => renvoie un message  de validation 
            Si la connexion ne fonction pas => renvoie un message d'erreur 

        Exemple d'appel :
            res=create_table(database ="stack_network_links", host="localhost",user="root",password="azerty",sql="CREATE TABLE stackNetworkLinks (source VARCHAR(255), target VARCHAR(255) , value FLOAT )" )  
    '''
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
            )

        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()

        resultat = "requetes executé"
        return resultat

    except Exception as e:
        erreur="Erreur :  create_table()"
        print(erreur,e)
        return erreur 

def requete_select(database=None,host=None,user=None,password=None,sql=None):
    '''
        Fonction qui permet une table dans une bd

        Parametre :
            database    : Nom de la base de données si elle existe
            host        : Nom ou ip de l'hote où est mysql exemple : "localhost ou 127.0.0.1"
            user        : Login de connexion 
            password    : Mot de passe de connexion 
            sql         : Requete sql à executer exemple => Select dans la table : "SELECT * FROM customers"    /     "SHOW TABLE stackNetworkLinks"
                                                         
        renvoie :
            Si la connexion fonction => renvoie un message  de validation 
            Si la connexion ne fonction pas => renvoie un message d'erreur 

        Exemple d'appel :
            res=requete_select(database ="stack_network_links", host="localhost",user="root",password="azerty",sql="SHOW TABLE stackNetworkLinks" )
         
    '''
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
            )
        resultat = []
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        resultat_sql = mycursor.fetchall()

        for x in resultat_sql:
            resultat.append(x)
            #print(x)

        return resultat

    except Exception as e:
        erreur="Erreur :  requete_sql()"
        print(erreur,e)
        return erreur 

def requete_insert(database=None,host=None,user=None,password=None,sql=None,valeur=None):
    '''
        Fonction qui permet des faire des insertions dans la bd

        Parametre :
            database    : Nom de la base de données si elle existe
            host        : Nom ou ip de l'hote où est mysql exemple : "localhost ou 127.0.0.1"
            user        : Login de connexion 
            password    : Mot de passe de connexion 
            sql         : Requete sql à executer 
                                                         
        renvoie :
            Si la connexion fonction => renvoie un message  de validation 
            Si la connexion ne fonction pas => renvoie un message d'erreur 

        Exemple d'appel :
            res1=requete_insert(database ="stack_network_links", host="localhost",user="root",password="azerty",sql="INSERT INTO stack_network_links (source,target,value) VALUES ('val1','val2',2)")
    '''
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
            )

        sql =sql
        #print(sql)

        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()

        return "insert ok"

    except Exception as e:
        erreur="Erreur :  requete_insert()"
        print(erreur,e)
        return erreur 


def df_to_mysql(database=None,host=None,user=None,password=None,df=None,table=None):
    '''
        Fonction qui permet une table dans une bd

        Parametre :
            database    : Nom de la base de données si elle existe
            host        : Nom ou ip de l'hote où est mysql exemple : "localhost ou 127.0.0.1"
            user        : Login de connexion 
            password    : Mot de passe de connexion 
            df          : Dataframe à intégrer 
            table       : Nom de la table ou importer le dataframe
                                                         
        renvoie :
            Si la connexion fonction => renvoie un message  de validation 
            Si la connexion ne fonction pas => renvoie un message d'erreur 

        Exemple d'appel :
            res=requete_select(database ="stack_network_links", host="localhost",user="root",password="azerty",sql="SHOW TABLE stackNetworkLinks" )
         
    '''
    from sqlalchemy import create_engine
    import pymysql
    try:

        host=host
        user=user
        password=password
        database=database

        # Create SQLAlchemy engine to connect to MySQL Database
        engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=host, db=database, user=user, pw=password))

        # Convert dataframe to sql table                                   
        df.to_sql('stack_network_links', engine, index=False)

    except Exception as e:
        erreur="Erreur :  df_to_mysql()"
        print(erreur,e)
        return erreur 


# Décomenter pour tester le fonction df_to_mysql()
'''
import pandas as pd
import os 
path = os.path.realpath(__file__)               # donne le chemin du fichier app.py  xx/xx/xx/app.py
#print("Le chemin du script est : " + path)
chemin =os.path.split(path)                     # Séparer le chemin et le nom de fichier    [xx/xx/xx , app.py]  
path =   chemin[0] 
df = pd.read_csv(path+"/stack_network_links.csv", sep =",")
#print(df)
'''


#res=conn(host="localhost",user="root",password="azerty")
#res=create_bdd(database="db1",host="localhost",user="root",password="azerty")
#res=show_bdd(host="localhost",user="root",password="azerty")
#res=create_table(database ="stack_network_links", host="localhost",user="root",password="azerty",sql="CREATE TABLE stackNetworkLinks (source VARCHAR(255), target VARCHAR(255) , value FLOAT )" )
#res=suppression(database ="stack_network_links", host="localhost",user="root",password="azerty",sql="DROP TABLE stack_network_links" )
#res=requete_select(database ="stack_network_links", host="localhost",user="root",password="azerty",sql="SELECT * FROM stack_network_links WHERE source ='val11' " )
#res=df_to_mysql(database ="stack_network_links", host="localhost",user="root",password="azerty",df = df  )
#res=requete_insert(database ="stack_network_links", host="localhost",user="root",password="azerty",sql="INSERT INTO stack_network_links (source,target,value) VALUES ('val1','val2',2)")

#print(res)

