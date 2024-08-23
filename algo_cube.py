import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
<<<<<<< HEAD
import numpy as np

# Définir la classe Cube
class Cube:
    def __init__(self, size=10):
        self.size = size
        self.points = []

    def add_point(self, number):
        if 0 <= number < self.size ** 3:
            z = number // (self.size ** 2)
            y = (number % (self.size ** 2)) // self.size
            x = number % self.size
            self.points.append((x, y, z))
        else:
            raise ValueError(f"Le nombre {number} est hors de la plage pour un cube de taille {self.size}.")

    def get_points(self):
        return self.points

# Dessiner les contours d'un cube
def draw_cube(ax, origin_x, origin_y, origin_z, size):
    r = [0, size]
    vertices = [
        [origin_x + r[i], origin_y + r[j], origin_z + r[k]]
        for i in range(2) for j in range(2) for k in range(2)
    ]
    edges = [
        [vertices[0], vertices[1]], [vertices[0], vertices[2]], [vertices[1], vertices[3]], [vertices[2], vertices[3]],
        [vertices[4], vertices[5]], [vertices[4], vertices[6]], [vertices[5], vertices[7]], [vertices[6], vertices[7]],
        [vertices[0], vertices[4]], [vertices[1], vertices[5]], [vertices[2], vertices[6]], [vertices[3], vertices[7]]
    ]
    for edge in edges:
        ax.plot3D(*zip(*edge), color="black")

# Convertir un nombre en coordonnées dans cube2
def number_to_coordinates_cube2(number):
    if 0 <= number < 1000:
        z = number // 100
        y = (number % 100) // 10
        x = number % 10
        return x * 10, y * 10, z * 10  # Multiplier par 10 pour l'échelle de cube2
    else:
        raise ValueError("Le nombre doit être compris entre 0 et 999 pour cube2.")

# Créer un cube de taille 10x10x10 (cube1)
cube1 = Cube(size=10)

# Ajouter des points à cube1
while True:
    user_input = input("Entrez un nombre entre 0 et 999 pour cube1 (ou 'q' pour quitter) : ")
    
    if user_input.lower() == 'q':
        break

    try:
        number = int(user_input)
        cube1.add_point(number)
        print(f"Point {number} ajouté avec succès à cube1.")
    
    except ValueError as e:
        print(f"Erreur: {e}. Veuillez entrer un nombre valide.")
        continue

# Afficher les points de cube1
print("Points dans cube1:", cube1.get_points())

# Demander à l'utilisateur le nombre pour placer cube1 dans cube2
try:
    placement_number = int(input("Entrez un nombre entre 0 et 999 pour placer cube1 dans cube2 : "))
    cube2_x, cube2_y, cube2_z = number_to_coordinates_cube2(placement_number)

except ValueError as e:
    print(f"Erreur: {e}. Réessayez.")
    exit()
=======

print ("##############################################")
print ("##############################################")
print ("#####                                   ######")
print ("#####           génération              ######")
print ("#####       Cube de dimention           ######")
print ("#####                1                  ######")
print ("#####         entre 0 et 999            ######")
print ("#####                                   ######")
print ("##############################################")
print ("##############################################")
print ("")
print ("")

# Génération de la coordoné du nombre
def number_to_coordinates(n):
    if 0 <= n <= 999:
        z = n // 100
        y = (n % 100) // 10
        x = n % 10
        return x, y, z
    else:
        raise ValueError("Please, input betwwen 0 and 999")
>>>>>>> 69f0ab811253fa7ad2b20420ef51d148c54bec2a

# Configuration de la figure 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Configurer les labels des axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

<<<<<<< HEAD
# Fixer le ratio des axes pour que le cube apparaisse proportionnel
ax.set_box_aspect([1,1,1])  
# Maintient une échelle égale sur les axes

# Affichage du cube2
ax.set_xlim(0, 99)
ax.set_ylim(0, 99)
ax.set_zlim(0, 99)

# Ajouter les points de cube1 à cube2 avec un décalage
for (x, y, z) in cube1.get_points():
    ax.scatter(x + cube2_x, y + cube2_y, z + cube2_z, c='blue', marker='o')
    ax.text(x + cube2_x, y + cube2_y, z + cube2_z, f"({x},{y},{z})", size=10, zorder=1, color='k')

# Dessiner les contours de cube1 à l'intérieur de cube2
draw_cube(ax, cube2_x, cube2_y, cube2_z, 10)

# Affichage final
=======
# Affichage du cube
ax.set_xlim(0, 9)
ax.set_ylim(0, 9)
ax.set_zlim(0, 9)

# Espace pour entrer des nombres
while True:
    user_input = input("Entrez un nombre entre 0 et 999 (ou 'q' pour quitter) : ")

    if user_input.lower() == 'q':
        break

    try:
        number = int(user_input)
        x, y, z = number_to_coordinates(number)

        # Affichage du point
        ax.scatter(x, y, z, c='blue', marker='o')
        ax.text(x, y, z, str(number), size=10, zorder=1, color='k')

        # Maj d'affichage
        plt.draw()
        # decommenter si possible et revérifier utilité
        # plt.pause(0.5)

    except ValueError as e:
        print(f"Erreur: {e}. Veuillez entrer un nombre valide.")
        continue

# Figure finale (à customiser)
>>>>>>> 69f0ab811253fa7ad2b20420ef51d148c54bec2a
plt.show()
