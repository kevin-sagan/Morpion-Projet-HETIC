#Permet de copier n'importe quel objet
import copy
#Importation d'un perceptron Multi-Couche
from sklearn.neural_network import MLPClassifier
import numpy as np
#Génère des nombres aléatoires
import random
#Importation des fonctions de prétraitement des données
from sklearn import preprocessing
#Importation d'une forêt d'arbre décisionnels
from sklearn.ensemble import RandomForestClassifier
#Importation des arbres de décisions
from sklearn import tree



class Morpion:

    #Permet d'initialiser le jeu
    def __init__(self):

    #Fonction de réinitialisation du tableau
    def intialiser_plateau(self):
        self.plateau=[['-','-','-'],['-','-','-'],['-','-','-']]

    #Fonction de jeu qui fera jouer l'ia pour l'entraîner
    def ai_jeu(self,i):

    #Fonction qui convertira le plateau de signe en plateau de données numériques compréhensibles pour un réseau de neurones
    def convert_plateau(self,plateau):

    #Fonction d'entraînement par renforcement de l'ia, elle fera l'ia jouer de nombreuses fois contre un joueur 
    # dont les mouvements seront aléatoire
    def train_ai_jeu(self):

    #Contient le code qui assure le bon déroulement du jeu en lui même
    def jeu(self):

    #Renvoie l'ensemble des mouvements possibles pour le joueur passé en paramètre
    def generateur_de_mouvement(self,joueur):

    #Fonction qui entraîne l'ia sur les parties passées
    def train_ai_player(self):

    #Fonction permet à l'adversaire de l'ia de jouer son tour
    def entraineur_ai_joue(self,list_mvt_possible):

    #Permet à l'ia de jouer son tour
    def ai_player_joue(self,joueur,list_mvt_possible):
        
    #Affiche le plateau de jeu
    def afficher_plateau(self):
   
    #Test si il y a un vainqueur où si il y a plus de mouvement possible
    def test_fin_jeu(self,joueur):
   
    #Permet à un joueur de jouer son tour      
    def jouer(self, joueur):