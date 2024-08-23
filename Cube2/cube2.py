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
def draw_cube(ax, origin_x, origin_y, origin_z, size, edge_color=(0, 0, 1, 0.3)):
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
        ax.plot3D(*zip(*edge), color=edge_color, linewidth=0.7)

# Convertir un nombre en coordonnées dans un cube de taille 10
def number_to_coordinates_cube(number):
    if 0 <= number < 1000:
        z = number // 100
        y = (number % 100) // 10
        x = number % 10
        return x, y, z
    else:
        raise ValueError("Le nombre doit être compris entre 0 et 999 pour ce cube.")

# Ajouter un cube coloré et transparent
def draw_colored_transparent_cube(ax, origin_x, origin_y, origin_z, size, color='red', alpha=0.3):
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
    ax.add_collection3d(art3d.Poly3DCollection(faces, facecolors=color, linewidths=0.7, edgecolors=(0, 0, 1, 0.3), alpha=alpha))

# Créer un cube de taille 10x10x10 (cube1)
cube1 = Cube(size=10)

# Demander à l'utilisateur de saisir un seul nombre entre 0 et 999999999
while True:
    user_input = input("Entrez un nombre entre 0 et 999999999 : ")
    
    try:
        number = int(user_input)
        if 0 <= number <= 999999999:
            # Extraire les trois derniers chiffres pour définir le point dans cube1
            point_number = number % 1000
            # Extraire les trois chiffres du milieu pour placer cube1 dans cube2
            placement_number_cube2 = (number // 1000) % 1000
            # Extraire les trois premiers chiffres pour placer cube2 (et donc cube1) dans cube3
            placement_number_cube3 = number // 1000000
            
            # Ajouter le point dans cube1
            cube1.add_point(point_number)
            print(f"Point {point_number} ajouté avec succès à cube1.")
            break  # On sort de la boucle après avoir entré un seul nombre
        else:
            print("Le nombre doit être compris entre 0 et 999999999.")
    except ValueError:
        print("Erreur: Veuillez entrer un nombre valide.")

# Afficher les points de cube1
print("Points dans cube1:", cube1.get_points())

# Convertir les trois chiffres du milieu pour obtenir les coordonnées de cube2
cube2_x, cube2_y, cube2_z = number_to_coordinates_cube(placement_number_cube2)
# Convertir les trois premiers chiffres pour obtenir les coordonnées de cube3
cube3_x, cube3_y, cube3_z = number_to_coordinates_cube(placement_number_cube3)

# Normaliser les coordonnées pour les ramener à une échelle de 0 à 9
norm_cube2_x = cube2_x / 10
norm_cube2_y = cube2_y / 10
norm_cube2_z = cube2_z / 10

norm_cube3_x = cube3_x  # Pas de division par 100, car on veut que cube3 soit placé dans le référentiel de 0 à 9
norm_cube3_y = cube3_y
norm_cube3_z = cube3_z

# Configuration de la figure 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Configurer les labels des axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Fixer le ratio des axes pour que le cube apparaisse proportionnel
ax.set_box_aspect([1,1,1])  # Maintient une échelle égale sur les axes

# Affichage du cube3
ax.set_xlim(0, 9)
ax.set_ylim(0, 9)
ax.set_zlim(0, 9)

# Ajouter les points de cube1 à cube2 avec un décalage, puis cube2 à cube3
for (x, y, z) in cube1.get_points():
    ax.scatter(x * 0.1 + norm_cube2_x + norm_cube3_x, y * 0.1 + norm_cube2_y + norm_cube3_y, z * 0.1 + norm_cube2_z + norm_cube3_z, c='blue', marker='o')
    ax.text(x * 0.1 + norm_cube2_x + norm_cube3_x, y * 0.1 + norm_cube2_y + norm_cube3_y, z * 0.1 + norm_cube2_z + norm_cube3_z, f"Point ({x},{y},{z})", size=10, zorder=1, color='k')

# Dessiner les contours de cube1 à l'intérieur de cube2, puis de cube2 dans cube3
draw_cube(ax, norm_cube2_x + norm_cube3_x, norm_cube2_y + norm_cube3_y, norm_cube2_z + norm_cube3_z, 1)  # Taille ajustée pour que cube1 soit imbriqué dans cube2
draw_cube(ax, norm_cube3_x, norm_cube3_y, norm_cube3_z, 3)  # Taille ajustée pour que cube2 soit imbriqué dans cube3

# Ajouter les annotations pour les coordonnées de cube2 et cube3
ax.text(norm_cube2_x + norm_cube3_x, norm_cube2_y + norm_cube3_y, norm_cube2_z + norm_cube3_z, f"Cube2 ({cube2_x},{cube2_y},{cube2_z})", size=12, zorder=1, color='red')
ax.text(norm_cube3_x, norm_cube3_y, norm_cube3_z, f"Cube3 ({cube3_x},{cube3_y},{cube3_z})", size=12, zorder=1, color='green')

# Ajouter le cube coloré et transparent pour cube1 et cube2
draw_colored_transparent_cube(ax, norm_cube2_x + norm_cube3_x, norm_cube2_y + norm_cube3_y, norm_cube2_z + norm_cube3_z, 1, color='red', alpha=0.3)
draw_colored_transparent_cube(ax, norm_cube3_x, norm_cube3_y, norm_cube3_z, 3, color='green', alpha=0.2)  # Un cube vert pour visualiser cube3

# Affichage final
plt.show()
