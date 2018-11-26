#!/usr/bin/env python3
# coding: utf-8

from tkinter import *

# CONSTANTES

# Dimensions du plateau de jeu
NB_LIGNES = 9
NB_COLONNES = 7

# Largeur/Hauteur d'une case du plateau
D = 51

# Types de case
TERRE = 0
EAU = 1
PIEGE_BLANC = 2
PIEGE_NOIR = 3
TANIERE_BLANC = 4
TANIERE_NOIR = 5


# VARIABLES GLOBALES du Jeu

# Représentation mémoire du plateau de jeu (9 x 7 cases : Tuple de tuples qui peut-être vu comme un tableau 2 dimensions)
plateau = (
		( TERRE , TERRE , PIEGE_NOIR , TANIERE_NOIR , PIEGE_NOIR , TERRE , TERRE ) ,
		( TERRE , TERRE , TERRE , PIEGE_NOIR , TERRE , TERRE , TERRE ) ,
		( TERRE , TERRE , TERRE , TERRE , TERRE , TERRE , TERRE ) ,
		( TERRE , EAU , EAU , TERRE , EAU , EAU , TERRE ) ,
		( TERRE , EAU , EAU , TERRE , EAU , EAU , TERRE ) ,
		( TERRE , EAU , EAU , TERRE , EAU , EAU , TERRE ) ,
		( TERRE , TERRE , TERRE , TERRE , TERRE , TERRE , TERRE ) ,
		( TERRE , TERRE , TERRE , PIEGE_BLANC , TERRE , TERRE , TERRE ) ,
		( TERRE , TERRE , PIEGE_BLANC , TANIERE_BLANC , PIEGE_BLANC , TERRE , TERRE )
	)

# FONCTIONS

def creerGUI() :
	
	global fenetre , plateauGUI
	
	fenetre = Tk()
	fenetre.title( 'pyXouDouQi' )
	
	plateauGUI = Canvas( fenetre )
	plateauGUI[ 'width'] = 365
	plateauGUI[ 'height'] = 469
	plateauGUI[ 'background' ] = 'black'
	
	plateauGUI.pack( side = LEFT , fill = BOTH , pady = 2 , padx = 2 )
	
	
def dessinerCase( ligne , colonne , typeCase = TERRE ) :
	
	x1 = D * colonne - D + colonne + 1
	x2 = ( D + 1 ) * colonne
	
	y1 = D * ligne - D + ligne + 1
	y2 = ( D + 1 ) * ligne
	
	if typeCase == TERRE :
		plateauGUI.create_rectangle( x1 , y1 , x2 , y2 , outline = 'green' , fill = 'green' )
	elif typeCase == EAU :
		plateauGUI.create_rectangle( x1 , y1 , x2 , y2 , outline = 'blue' , fill = 'blue' )
	elif typeCase == PIEGE_BLANC or typeCase == PIEGE_NOIR :
		plateauGUI.create_rectangle( x1 , y1 , x2 , y2 , outline = 'green' , fill = 'green' , stipple = 'gray50' )
	elif typeCase == TANIERE_BLANC or typeCase == TANIERE_NOIR :
		plateauGUI.create_rectangle( x1 , y1 , x2 , y2 , outline = 'green' , fill = 'green' , stipple = 'gray75' )
	

def consulterPlateau() :
	# Question 3.4
	# votre code ici
	pass


def dessinerPlateau() :
	# Question 3.5
	# votre code ici
	pass
	
	
def getNbCasesEau() :
	# Question 3.6
	# votre code ici
	pass
	
	
def getCasesEau() :
	cases = []
	# Question 3.7
	# votre code ici
	
	return cases
	
	
def getNbCasesParType() :
	casesParType = []
	# Question 3.8
	# votre code ici
	
	return casesParType




# ENTRÉE DU PROGRAMME

if __name__ == '__main__' :
	
	creerGUI()
	
	# Question 3.1
	print( '\nQuestion 3.1 :' )
	# Votre code ici
	
	
	# Question 3.2
	print( '\nQuestion 3.2 :' )
	# Votre code ici
	
	
	# Question 3.3
	print( '\nQuestion 3.3 :' )
	# Votre code ici
	
	
	# Question 3.4
	print( '\nQuestion 3.4 :' )
	consulterPlateau()
	
	
	# Question 3.5
	print( '\nQuestion 3.5 :' )
	dessinerPlateau()
	
	
	# Question 3.6
	print( '\nQuestion 3.6 :' )
	print( 'Nombre de cases de type "Eau" :' , getNbCasesEau() )
	
	
	# Question 3.7
	print( '\nQuestion 3.7 :' )
	lstCasesEau = getCasesEau()
	for uneCase in lstCasesEau :
		# Utilisation des chaînes formatées pour éviter l'utilisation
		# à outrance de l'opérateur de concaténation (+)
		# https://docs.python.org/fr/3.5/library/string.html#format-string-syntax
		print( '({0},{1})'.format( uneCase[ 0 ] , uneCase[ 1 ] ) )
		
		
	# Question 3.8
	print( '\nQuestion 3.8 :' )
	lstBilanTypes = getNbCasesParType()
	for unType in lstBilanTypes :
		print( 'Type : {0} ---> {1} cases'.format( unType[ 0 ] , unType[ 1 ] ) )


	fenetre.mainloop()
