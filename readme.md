# TP: Docker && K8s

Consigne: 

Faire une application qui possède deux containers docker dont un sur une image custom. Puis la faire avec K8s.

# How to

Cloner le dépôt.

Application:

Pour docker :

```bash
$ docker build -t devops .
$ source variables.env
$ docker-compose up
# Can access with localhost:3300
```

- Image custom:  une application web en python (bottle) qui sur les routes suivantes :
    - / : liste tous les produits
    - /insert/<name>/<price> : ajoute un nouveau produit avec les paramètres passés
    - /<id> : affiche le produit avec l’id correspondant
- L’autre conteneur est une image **mariadb** qui va contenir les produits

Pour K8s :

```bash
$ minikube start
$ eval $(minikube -p minikube docker-env)
$ docker build -t devops .
$ kubectl apply -f config-map.yaml
$ kubectl apply -f deploy-sql.yaml
$ kubectl apply -f deploy-python.yaml
$ minikube service myapp-service
```

Endpoint disponible : 

/insert/<name>/<price> :  Insert new product in the database

ex : [http://192.168.49.2:30000/insert/productOne/85](http://192.168.49.2:30000/insert/productOne/85)

/<id> : Get the product with the corresponding id

ex : [http://192.168.49.2:30000/6](http://192.168.49.2:30000/6)

/ : Get all product

ex : [http://192.168.49.2:30000/](http://192.168.49.2:30000)

Il peut y avoir de petites améliorations mais tout marche 🙂