Le projet de classement ultradimensionnel est un projet dont je ne perçois pas encore l'utilité finale.
 Partant du principe qu'il n'est pas nécessairement à l'inventeur d'un outil de trouver sa meilleure exploitation et que,
 même s'il n'y a pas d'utilité, cela reste un exercice intéressant à mettre en place,
 j'ai donc décidé de développer ce système de classement dans les mois à venir.


NOTA: Je dois fournir des graphiques pour exlicité l'idée, surtout sur la partie finale qui manque d'objectivité 
dans la présentation.

RESUME: Le projet de classement ultradimensionnel vise à créer un système permettant de stocker de grandes quantités
 de données de manière compacte en utilisant une indexation multidimensionnelle. 
Cela signifie que les données sont organisées dans un espace à plusieurs dimensions plutôt que dans une liste linéaire.
 Cela permet de raccourcir les chemins parcourus pour accéder à une donnée donnée 
et de minimiser la liste de chiffres intermédiaires.
 Le système utilise également un hachage intégré aux données elles-mêmes pour permettre de 
stocker ces données de manière plus efficace. Le projet nécessitera des connaissances en algorithme et 
la maîtrise d'un langage de programmation adapté, ainsi qu'un logiciel de visualisation 3D pour rendre
 le projet plus accessible à un public non technique.


Ce système de classement permet de compacter un espace multidimensionnel sur lui-même afin de stocker de grandes 
quantités de données grâce à un système de hachage intégré au nombre lui-même. 
En gros, chaque nombre est sa propre coordonnée dans un espace qui se replie sur lui-même.

Le développement de ce projet nécessitera :

Des bases solides en algorithme
Un language adapté (python ?)
Un logiciel de visualisation 3D peut gourmand en ressources et facilement exploitable à partir de lignes de code afin de
 proposer des models explicatifs.

Explication de base du projet :

Prenons le nombre "1". Nous pouvons facilement le classer sur un axe "X", dont l'échelle va de 0 à 9.

Prenons maintenant le nombre "21".
 Il pourra facilement être classé sur un axe X et Y : on prendra l'abscisse 1 et l'ordonnée 2.

Avec la même logique, le nombre 321 pourra facilement être classé sur trois axes XYZ.
 On dira, pour ce projet, que le chiffre 321 est de dimension 3, car il est placable sur un ensemble tridimensionnel XYZ.

Il faut imaginer que tous les nombres entre 0 et 999 peuvent être classés dans un cube XYZ¹ d'échelle 999.



Maintenant, imaginons le nombre 4321. 

Si nous pouvons facilement classer 321, avec une logique tridimensionnelle, placer 4000 peut sembler problématique.
 Il faut alors imaginer que le cube de dimension 3 dans lequel est classé 321 est lui-même classé sur un axe Y (de dimension 4). On l'appellera Y².

En appliquant cette logique,
 nous pouvons classer tous les nombres entre 0 et 999999 dans un cube de dimension XYZ² (X²Y²Z²). 
Par exemple, le nombre 67543 sera placé aux coordonnées X3 Y4 Z5 du cube lui-même placé aux coordonnées X²7 Y²6 Z²0.

Un des avantages que je vois à imaginer une indexation multidimensionnelle est de raccourcir les chemins parcourus entre deux données.

Par exemple, dans une liste linéaire de 1 à 999898, il faut parcourir 999898 points avant d'atteindre la donnée souhaitée.
 En imaginant un classement multidimensionnel, on peut donner un chiffre de départ,
 un vecteur et une force pour définir une liste, permettant ainsi de minimiser la liste de chiffres intermédiaires.