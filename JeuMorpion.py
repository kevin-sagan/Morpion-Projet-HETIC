# Création de la classe pour créer le jeu du Morpion

class JeuMorpion:
    
    # Inialisation du jeu
    def __init__(self):
        # Création de mon quadrillage pour jouer
        self.quadrillage = [['', '', ''],['', '', ''],['', '', '']]
        # Initialisation de la réponse de mon Joueur 1
        self.joueur_1 = 'O'
        # Initialisation de la réponse de mon Joueur 2
        self.joueur_2 = 'X'
        
    # Demande au joueur de jouer 
    def jouer_au_morpion(self, joueur):
        
        # Input pour l'absisse du placement du joueur
        x = int(input("Inscrivez l'absisse où vous voulez placer votre indicateur entre 1 et 3"))
        # Input pour l'ordonnée du placement du joueur
        y = int(input("Inscrivez l'absisse où vous voulez placer votre indicateur entre 1 et 3"))
        
        # Inscription des coordonnées de l'indicateur du joueur sur le quadrillage
        
        self.quadrillage[x][y]
        
        
        