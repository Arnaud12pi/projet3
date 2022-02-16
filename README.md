# projet3

#Description 
API qui permet d'intégrer les données d'un fichier .csv dans une databes mysql.
Il est aussi possible de faire des requêtes SELECT simple ,pour intégroger la base et INSERT pour ajouter des lignes dans la bd

repertoires:
-- /app
--    /env                        #Repertoire de l'environement virtuel
--    /requirements.txt           #Fichier requirements
--    /main.py                    #Fichier main de l'API
--    /mysql_requete.py           #Fonctions pour manipuler mysql ( requete)
--    /stack_network_links.csv    #Fichier de donnée telecharger sur ●	https://www.kaggle.com/stackoverflow/stack-overflow-tag-network?select=stack_network_links.csv
 

#Installation de l'API

1- Télècharger l'image de mysql sur votre machine (docker nécessaire) 
```
docker pull mysql
```

2- lancer un container avec l'image mysql => le mot de passe ici sera "azerty"
```
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=azerty -d mysql
```

3-Crée un repertoire pour l'application 
```
mkdir app
```

4-Créer un environement virtuel dans ce repertoire (virtualenv nécessaire)
```
cd app
python3 -m venv env
```

5-copier les fichiers dans ce repertoire l'application (repertoire racine ) 

6-Activer l'environement virtuel 
```
source ./env/bin/activate
```

7-Dans le repertoire racine (/app) => telecharger les librairies avec le fichier requirements.txt
```
pip install -r requirements.txt
```
8-Dans le repertoire racine (/app), lancer le server uvicorn , 
```
uvicorn main:app --reload
```
L'api est maintenant disponible sur le navigateur à l'adresse http://localhost:8000


#Utilisation de l'API

Sur l'URL http://localhost:8000 on peut voir 5 endpoint :
```
-Status          : Permet de vérifier si l'API est opérationnel
-Intégration     : Création de la database et integration les données du fichier "stack_network_links.csv" dans la bd mysql 
-Database        : Permet d'affciher les database presente sur mysql 
-Requete SELECT  : Permet de faire des requete select simple pour intéroger la bd , exemple : 

    -select :  source,target          # Colonnes à afficher 
    -FROM   :  stack_network_links    # Table à intéroger
    -where  :  target = ".net"        # condiction pour la recherche 
![Screenshot](C:\Users\adouspis\Desktop\1.png)
     
-Requete INSERT  : Permet de faire des INSERT spour ajouter une ligne dans la bd , exemple:

    -val_source  : "test1"            # Valeur à attribuer à la colonne "source" (string)
    -valt_target : "test2"            # Valeur à attribuer à la colonne "target" (string)
    -val_value   : 5                  # Valeur à attribuer à la colonne "value"  (int)
```



