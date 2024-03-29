# Projet Python Avance : GeoMinetry Dash

Notre projet consiste en la création d’un jeu vidéo. Nous avons fait le choix de concevoir un jeu sous format “Endless Runner”. Le joueur avance dans le jeu en évitant les obstacles qui apparaissent sur son chemin. Le jeu ne s'arrête que lorsqu'il y a contact entre un obstacle et le joueur

# Lancement du jeu :
Lancer le fichier game_launcher.ipynb

# Objectifs :
- Inspiration de Géométrie Dash avec personnalisation dans l'univers de l'Ecole des Mines de Paris en apportant des fonctionnalités propres (notamment tir de destruction d'obstacles)
- Produire des commandes simples et intuitives 
- Offrir un visuel attractif et esthétique 

# Type de plateforme :  PC 

# Préparatifs :

- Utilisation de la librairie Pygame 
- Code de base pour créer la plateforme  

# Interface du jeu :
L'interface du jeu se décompose en une page d'accueil, puis la page principale où se déroule le jeu, qui consiste en un défilement de plusieurs images dans l'univers des Mines de Paris tirées aléatoirement 

Page d'accueil :

Cet écran est constitué d'un bouton à actionner pour démarrer le jeu. Le meilleur score obtenu lors de la session est également conservé.

Page principale :
 
  - Le joueur contrôle une boule verte en la faisant sauter à l'aide de la touche espace pour éviter les obstacles
  - Le joueur a la possibilié d'effectuer deux sauts consécutifs au maximum
  - Les obstacles de forme rectangulaire aparaissent de manière aléatoire avec des hauteurs et des largeurs différentes
  - La vitesse des obstacles augmente avec le temps
  - Un système de score a été implémenté pour évaluer la distance parcourue par le joueur
  - A condition que le score soit suffisamment élevé, le joueur peut activer la commande de tir à l'aide d'un clic droit, ce qui entraîne la destruction de l'obstacle à venir
  - Le contact de la boule verte avec un obstacle entraine la fin du jeu et on retourne sur la page d'accueil

# Description des fonctionnalités du jeu : Programmation Orienté Objet

On introduit plusieurs modules :

 - Fonction obstacle : Génération d'obstacle rectangulaire consistant à la formation d'une liste de tuple contenant la position, la hauteur et la largeur du rectangle, ces valeurs sont générées aléatoirement à l'aide du module randint de random. L'obstacle s'affichera à l'aide du module draw.rect de pygame. Les obstacles qui sortent de l'écran sont progressivement supprimés en les retirant de la liste de tuple.
 - Fonction vitesse : Les obstacles se déplacent en modifiant la position de leur surface gauche à l'aide de la fonction vitesse implémentée en amont. La position est calculée en multipliant la temps entre chaque frame d'avec la vitesse des obstacles. La vitesse est constante pendant 10 secondes puis elle augmente proportionellement à la puissance 3/4 du temps, avant de se borner à ne vitesse élevée. Ainsi la difficultée augmente jusqu'à un niveau maximum puis reste la même.
 - Commande de saut : A l'actionnement de la touche espace, la hauteur du centre de la boule varie. Cette hauteur est calculée en multipliant la temps entre chaque frame d'avec la vitesse verticale de la boule verte qui varie également selon une accélération constante. La boule redescend lorsque la vitesse verticale devient négative. On impose une vitesse nulle lorsque que la hauteur atteint le sol.
 - Commande de tir : A l'actionnement du clique droit de la souris, un petit rectangle violet se déplace vers les obstacles. Plusieurs cas de figure apparaissent : si le "projectile" est en contact avec un obstacle de la liste, on l'a supprime de la liste. Si le projectile atteint la taille de l'écran, le projectile disparaît. Cette commande n'est accessible qu'avec un score supérieur 100, et limitée à un seul shot avant d'atteindre un score de 300
 - Défaite : Génération de 10 points sur le périmètre de la boule verte et on vérifie si leurs coordonnées sont situées à l'intérieur de chaque obstacle ( dont les coordonnées sont présent dans la liste de tuple)




# Problèmes rencontrés :

Problème de code :
  - implémenter un temps "virtuel" qui est difficile à manipuler suivant les différentes fonctions du code.
  - on a effectué la programmation orientée objet après avoir formalisé le code du jeu, ce qui a entrainé plusieurs bugs. Par exemple, la position verticale de la boule verte se rénitialisait toute seule et cela affectait la fluidité du saut. Les variables globales ont dû être affectées autrement.


L'aspect artisanal du jeu :
- La dynamique du jeu a été créée précocemment sur un modèle de "temps physique" et de chute libre, artisanal et sans modèle. Les difficultés sont donc apparues quand il a fallu gérer l'interface d'accueil, pas conçue dès le départ.
- Il a alors fallu introduire les classes pour la gestion du jeu, ce qui a causé d'innombrables bugs et erreurs en cascade (il est parfois plus difficile de réadapter un code plutôt que de repartir de zéro). Nous avons finalement réussi à préserver la physique artisanale du jeu sans affecter l'efficacité du code, avec un passage aux classes réussi. Cela peut expliquer pourquoi nous n'utilisons pas la superclasse Sprite pour la collision avec les obstacles par exemple.

La dynamique de jeu :
- L'accélération continue du défilement rend le jeu injouable au bout d'un certain temps. L'implémentation d'une fonction de tir permet de se sortir des situations délicates et d'améliorer l'expérience de jeu.

Manque de temps pour les fonctions suivantes : 
  - Créer plusieurs personnages 
  - Implémenter un système de progression récompensant les joueurs à mesure qu'ils continuent de jouer



# projet_python_avance_patch