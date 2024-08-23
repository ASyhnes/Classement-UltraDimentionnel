import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d
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
        ax.plot3D(*zip(*edge), color=(0, 0, 1, 0.3), linewidth=0.7)  # Bleu transparent avec une faible épaisseur

# Convertir un nombre en coordonnées dans cube2
def number_to_coordinates_cube2(number):
    if 0 <= number < 1000:
        z = number // 100
        y = (number % 100) // 10
        x = number % 10
        return x * 10, y * 10, z * 10  # Multiplier par 10 pour l'échelle de cube2
    else:
        raise ValueError("Le nombre doit être compris entre 0 et 999 pour cube2.")

# Ajouter un cube coloré et transparent
def draw_colored_transparent_cube(ax, origin_x, origin_y, origin_z, size, color='red', alpha=0.3):
    # Définir les faces du cube
    faces = [
        # Face avant
        [[origin_x, origin_y, origin_z], [origin_x + size, origin_y, origin_z],
         [origin_x + size, origin_y + size, origin_z], [origin_x, origin_y + size, origin_z]],
        # Face arrière
        [[origin_x, origin_y, origin_z + size], [origin_x + size, origin_y, origin_z + size],
         [origin_x + size, origin_y + size, origin_z + size], [origin_x, origin_y + size, origin_z + size]],
        # Face gauche
        [[origin_x, origin_y, origin_z], [origin_x, origin_y, origin_z + size],
         [origin_x, origin_y + size, origin_z + size], [origin_x, origin_y + size, origin_z]],
        # Face droite
        [[origin_x + size, origin_y, origin_z], [origin_x + size, origin_y, origin_z + size],
         [origin_x + size, origin_y + size, origin_z + size], [origin_x + size, origin_y + size, origin_z]],
        # Face supérieure
        [[origin_x, origin_y + size, origin_z], [origin_x + size, origin_y + size, origin_z],
         [origin_x + size, origin_y + size, origin_z + size], [origin_x, origin_y + size, origin_z + size]],
        # Face inférieure
        [[origin_x, origin_y, origin_z], [origin_x + size, origin_y, origin_z],
         [origin_x + size, origin_y, origin_z + size], [origin_x, origin_y, origin_z + size]]
    ]
    
    # Créer une collection de polygones 3D pour représenter les faces du cube
    ax.add_collection3d(art3d.Poly3DCollection(faces, facecolors=color, linewidths=0.7, edgecolors=(0, 0, 1, 0.3), alpha=alpha))

# Créer un cube de taille 10x10x10 (cube1)
cube1 = Cube(size=10)

# Demander à l'utilisateur de saisir un seul nombre entre 0 et 999999
while True:
    user_input = input("Entrez un nombre entre 0 et 999999 : ")
    
    try:
        number = int(user_input)
        if 0 <= number <= 999999:
            # Extraire les trois derniers chiffres pour définir le point dans cube1
            point_number = number % 1000
            # Extraire les trois premiers chiffres pour placer cube1 dans cube2
            placement_number = number // 1000
            
            # Ajouter le point dans cube1
            cube1.add_point(point_number)
            print(f"Point {point_number} ajouté avec succès à cube1.")
            break  # On sort de la boucle après avoir entré un seul nombre
        else:
            print("Le nombre doit être compris entre 0 et 999999.")
    except ValueError:
        print("Erreur: Veuillez entrer un nombre valide.")

# Afficher les points de cube1
print("Points dans cube1:", cube1.get_points())

# Convertir les trois premiers chiffres pour obtenir les coordonnées de cube2
cube2_x, cube2_y, cube2_z = number_to_coordinates_cube2(placement_number)

# Configuration de la figure 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Configurer les labels des axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Fixer le ratio des axes pour que le cube apparaisse proportionnel
ax.set_box_aspect([1,1,1])  # Maintient une échelle égale sur les axes

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

# Ajouter le cube coloré et transparent à l'intérieur de cube2
draw_colored_transparent_cube(ax, cube2_x, cube2_y, cube2_z, 10, color='red', alpha=0.3)

# Affichage final
plt.show()
