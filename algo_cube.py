import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

# Configuration de la figure 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Configurer les labels des axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

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
plt.show()
