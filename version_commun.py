## Conceptrices : Junya Wang et Dipika Patel 
## Date : 31 octobre 2023

import time

def random_int(max):
    return math.floor(random()*max)

# Fonction à un parametre qui retourne un tableau d'une séquence de longeur n
def sequence(n):
    tab = []
    for i in range(0,n):
        tab.append(i)
    return tab

def test_sequence():
    assert sequence(5) == [0, 1, 2, 3, 4]
    assert sequence(0) == []
test_sequence()

# Fonction qui prend deux paramètres qui vérifie si la valeur est contenu
# dans le tableau
def contient(tab,x):
    if x in tab:
        return True
    return False 
def test_contient ():
    assert contient([9,2,5], 2) == True
    assert contient([9,2,5], 4) == False
test_contient()

# Fonction qui prend deux paramètres qui va ajouter une valeur au tableau si 
# et seulement si elle n'est pas déjà comprise dans celui-ci. 
def ajouter(tab,x):
    if not contient(tab,x):
        tab.append(x)
    return tab
def test_ajouter ():
    assert ajouter([9,2,5], 2) == [9,2,5]
    assert ajouter([9,2,5], 4) == [9,2,5,4]
test_ajouter()
#print(ajouter([9,2,5], 3))

# Fonction qui prend deux paramètres qui va retirer une valeur du tableau si 
# et seulement si elle est déjà comprise dans celui-ci. 
def retirer(tab,x):
    if contient(tab,x):
        tab.remove(x)
    return tab
def test_retirer():
    assert retirer([9,2,5], 2) == [9,5]
    assert retirer([9,2,5], 4) == [9,2,5]
test_retirer()
#print(retirer([9,2,5], 2))

def coordonnee(case,valeur):
      return [case % valeur, case // valeur]
    
# Fonction qui prend 4 paramètres pour identifier les cases voisines à partir
# des cooordonnées de la case en question et les retourner sous forme tableau
# de numéro de case.  

def voisins(x,y,nx,ny):
    coord = []                   # coordonnées x et y des cases 
    no_case = []                 # numéro de case 
    if x-1 >= 0 :                # case voisin de gauche
        coord.append([x-1,y])   
    if x+1 < nx:                 # case voisin de droite
        coord.append([x+1,y])    
    if y-1 >= 0 :                # case voisin d'en haut 
        coord.append([x,y-1])    
    if y+1 < ny:                 # case voisin d'en bas
        coord.append([x,y+1])  
        
    for element in coord:                   # chaque coordonnée des voisins est 
        no_case.append(element[0]+element[1]*nx) # assigné à son numero de case 
    return no_case

def test_voisins():
    assert voisins(7,2,8,4) == [22,15,31]
    assert voisins(0,0,8,4) == [1,8]
test_voisins()

# Fonction qui prend 4 paramètres pour enlever un mur en fonction de la 
# différence entre les coordonnées des murs voisins permettant d'dentifier le 
# type de mur à retirer entre Nord, Ouest, Sud et Est. 

def enlever_mur(case,nx,voisin,verti,horiz):
    coord = coordonnee(case,nx)          # coordonnées x,y 
    valeur = case-voisin                 # difference entre les cases voisins
    if valeur == 1 :                                # mur Ouest 
        mur_ouest = coord[0] + coord[1] * (nx+1)
        retirer(verti,mur_ouest)
        
    elif valeur == -1 :                             # mur Est
        mur_est = 1 + coord[0] + coord[1]* (nx+1)
        retirer(verti,mur_est)   

    elif valeur == nx :                             # mur Nord
        mur_nord = coord[0] + coord[1] * nx
        retirer(horiz,mur_nord)

    elif valeur == -nx :                            # mur Sud
        mur_sud = coord[0] + (coord[1]+1) * nx
        retirer(horiz,mur_sud)
        
#def test_enlever_mur : 
#    assert enlever_mur()
# Fonction qui dessinera les murs à partir des ensembles de murs verticales et
# et horizontales disponibles
def dessiner_mur (ensemble,nx,ny,dimension,est_horiz):
    for mur in ensemble :
        if est_horiz:
            coord = coordonnee(mur,nx)
            if mur >= nx and mur < nx*ny:
                fillRectangle(
                    coord[0]*dimension, 
                    coord[1]*dimension, 
                    dimension, 
                    1, 
                    "#000")
        else:
            coord = coordonnee(mur,nx+1)
            if mur % (nx+1) != 0 and mur % (nx+1) != nx:
                fillRectangle(
                    coord[0]*dimension, 
                    coord[1]*dimension, 
                    1, 
                    dimension, 
                    "#000")
            #sleep(0.1)
            
# Fonction qui va rendre une liste aléatoire peut importe le nombre d'éléments
def randomiser_liste(liste):
    for i in range(len(liste)-1, 0, -1):  #code inspiré du chapitre 8 p.104
        j = random_int(i+1)              # index de 0 à i aléatoire 
        temp = liste[i]            
        liste[i] = liste[j]
        liste[j] = temp 
    return liste

def laby(nx, ny, dimension):
    noire = "#000"
    blanc = "#fff"
    #mise en place du fond blanc 
    set_screen_mode(nx*dimension,ny*dimension)     
    fill_rectangle(0,0,nx*dimension,ny*dimension, blanc)
    taille_px = 1
    
    cave = []
    front = []
    horiz = sequence(nx*(ny+1))
    verti = sequence((nx+1)*ny)
    NB_CELLULES = nx*ny                    
    case_init = random_int(NB_CELLULES-1)  # case initiale

    cave.append(case_init)  
    coord = coordonnee(case_init,nx)
    front = voisins(coord[0], coord[1], nx, ny) 

    while(len(cave) < NB_CELLULES):
        a_retirer = True
        random_nb = random_int(len(front)-1)
        random_case = front[random_nb]
        coord = coordonnee(random_case,nx)
        random_voisins = voisins(coord[0], coord[1], nx, ny)
        random_voisins = randomiser_liste(random_voisins)

        for i in random_voisins:
            if not contient(cave, i):
                ajouter(front, i)
            elif a_retirer:
                enlever_mur(random_case,nx,i,verti,horiz)
                a_retirer = False

        retirer(front, random_case)
        ajouter(cave, random_case)
   
    dessiner_mur(horiz,nx,ny,dimension,True)
    dessiner_mur(verti,nx,ny,dimension,False)
    
    # x,y,width, height
    largeur = dimension*(nx-1)
    hauteur = dimension*ny
    
    fill_rectangle(dimension, 0, largeur, taille_px, noire)     # en haut
    fill_rectangle(0,dimension*ny-1, largeur, taille_px, noire) # en bas 
    fill_rectangle(0,0, taille_px, hauteur, noire)              # gauche
    fill_rectangle(dimension*nx-1,0, taille_px, hauteur, noire) # droite 

print(laby(16, 9, 20))  

def test_laby(x,y,dimension):
    ligne = export_screen().split('\n')
    entree = ligne[0].split('#')
    sortie = ligne[(y*dimension)-1].split('#')
    #print(ligne[(y*dimension-1)].split('#'))
    #print(sortie[(-dimension+1):-1])
   # assert len(entree[2:dimension+1]) == dimension-1
    #assert len(sortie[(-dimension):-2]) == dimension-1
print(test_laby(16,9,20))
    
   #print(ligne[(9*20)-1])

#def test_laby(laby):
   # export_screen(laby(35,18,10)) 
#print(test_laby(laby))
