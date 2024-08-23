import math

def calculer_vecteur_et_angles(x1, y1, z1, x2, y2, z2):
    # Vecteur de déplacement
    vx = x2 - x1
    vy = y2 - y1
    vz = z2 - z1
    
    # Magnitude du vecteur
    magnitude = math.sqrt(vx**2 + vy**2 + vz**2)
    
    # Angle azimutal (en degrés)
    theta = math.degrees(math.atan2(vy, vx))
    
    # Angle d'élévation (en degrés)
    if magnitude == 0:
        phi = 0  # éviter la division par zéro
    else:
        phi = math.degrees(math.acos(vz / magnitude))
    
    return (vx, vy, vz), magnitude, theta, phi

# Demander à l'utilisateur de saisir les coordonnées du point de départ
print("Entrez les coordonnées du point de départ dans un cube de taille 0 à 9 pour chaque axe:")
x1 = int(input("Coordonnée X du point de départ (0-9) : "))
y1 = int(input("Coordonnée Y du point de départ (0-9) : "))
z1 = int(input("Coordonnée Z du point de départ (0-9) : "))

# Demander à l'utilisateur de saisir les coordonnées du point d'arrivée
print("\nEntrez les coordonnées du point d'arrivée:")
x2 = int(input("Coordonnée X du point d'arrivée (0-9) : "))
y2 = int(input("Coordonnée Y du point d'arrivée (0-9) : "))
z2 = int(input("Coordonnée Z du point d'arrivée (0-9) : "))

# Calculer le vecteur de déplacement et les angles
vecteur, magnitude, azimuth, elevation = calculer_vecteur_et_angles(x1, y1, z1, x2, y2, z2)

# Afficher les résultats
print(f"\nVecteur de déplacement : {vecteur}")
print(f"Magnitude du vecteur : {magnitude:.2f}")
print(f"Angle azimutal (θ) : {azimuth:.2f} degrés")
print(f"Angle d'élévation (φ) : {elevation:.2f} degrés")
