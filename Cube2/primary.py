import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d
import numpy as np

# Générer la suite des nombres premiers jusqu'à 9999
def generate_prime_sequence(limit=9999):
    primes = []
    is_prime = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
    return primes

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

# Configuration de la figure 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Configurer les labels des axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Fixer le ratio des axes pour que le cube apparaisse proportionnel
ax.set_box_aspect([1, 1, 1])  # Maintient une échelle égale sur les axes

# Configurer les graduations des axes pour afficher de 0 à 9
ax.set_xticks(np.arange(0, 10, 1))
ax.set_yticks(np.arange(0, 10, 1))
ax.set_zticks(np.arange(0, 10, 1))

# Affichage du référentiel global
ax.set_xlim(0, 9)
ax.set_ylim(0, 9)
ax.set_zlim(0, 9)

# Générer la suite des nombres premiers jusqu'à 9999
prime_sequence = generate_prime_sequence(9999)

# Créer un cube pour placer les nombres premiers
cube1 = Cube(size=10)

# Ajouter les points au cube
for prime in prime_sequence:
    if prime < 1000:  # Limiter à un espace de cube1
        cube1.add_point(prime)

# Ajouter les points de cube1 à l'affichage
for (x, y, z) in cube1.get_points():
    ax.scatter(x, y, z, c='blue', marker='o')
    ax.text(x, y, z, str(f"{x},{y},{z}"), size=10, zorder=1, color='k')

# Dessiner les contours de cube1
draw_cube(ax, 0, 0, 0, 10)

# Affichage final
plt.show()
