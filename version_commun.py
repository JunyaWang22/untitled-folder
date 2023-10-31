## Conceptrices : Junya Wang et Dipika Patel 
## Date : 31 octobre 2023

NOIR = "#000"    # couleur de pixels du labyrinthe
BLANC = "#fff"
TAILLE_PX = 1    # épaisseur du mur en pixel 

# Fonction qui prend un paramètre et retourne une valeur aléatoire.
def random_int(max):
    return math.floor(random()*max)

def test_random_int():
    assert random_int(0) == 0 
    assert random_int(4) == 0 or 1 or 2 or 3 or 4
test_random_int() 

# Fonction à un parametre qui retourne un tableau d'une séquence de longeur n.
def sequence(n):
    tab = []
    for i in range(0,n):
        tab.append(i)
    return tab

def test_sequence():
    assert sequence(5) == [0, 1, 2, 3, 4]
    assert sequence(0) == []
test_sequence()

# Fonction qui prend deux paramètres qui retourne un booléen indiquant si x 
# est contenu dans le tableau.
def contient(tab,x):
    if x in tab:
        return True
    return False 
    
def test_contient ():
    assert contient([9,2,5], 2) == True
    assert contient([9,2,5], 4) == False
    assert contient([],2) == False
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
    assert ajouter([],2) == [2]
test_ajouter()


# Fonction qui prend deux paramètres qui va retirer une valeur du tableau si 
# et seulement si elle est déjà comprise dans celui-ci. 
def retirer(tab,x):
    if contient(tab,x):
        tab.remove(x)
    return tab

def test_retirer():
    assert retirer([9,2,5], 2) == [9,5]
    assert retirer([9,2,5], 4) == [9,2,5]
    assert retirer([],2) == []
test_retirer()

# Fonction qui prend 2 paramètres qui retourne les coordonnées de la case
def coordonnee(case,nx):
      return [case % nx, case // nx]
    
def test_coordonnee():
    assert coordonnee(21,8) == [3,2]
    assert coordonnee(16,8) == [0,2]
    
# Fonction qui prend 4 paramètres pour identifier les cases voisines à partir
# des cooordonnées de la case en question et les retourner sous forme tableau
# de numéro de case.  

def voisins(x,y,nx,ny):
    coord = []                   # coordonnées x et y des cases 
    no_case = []                 # numéro de case 
    if y-1 >= 0 :                # case voisin d'en haut 
        coord.append([x,y-1])   
    if x-1 >= 0 :                # case voisin de gauche
        coord.append([x-1,y])   
    if x+1 < nx:                 # case voisin de droite
        coord.append([x+1,y])     
    if y+1 < ny:                 # case voisin d'en bas
        coord.append([x,y+1])  
        
    for element in coord:                   # chaque coordonnée des voisins est 
        no_case.append(element[0]+element[1]*nx) # assigné à son numéro de case 
    return no_case

def test_voisins():
    assert voisins(7,2,8,4) == [15,22,31]
    assert voisins(0,0,8,4) == [1,8]
    assert voisins(0,0,1,1) == []
    assert voisins(4,1,8,4) == [4,11,13,20]
    assert voisins(0,3,8,4) == [16,25]
    assert voisins(0,0,2,1) == [1]
test_voisins()

# Fonction qui prend 4 paramètres pour enlever un mur en fonction de la 
# différence entre les coordonnées des murs voisins permettant d'dentifier le 
# type de mur à retirer entre Nord, Ouest, Sud et Est. 

def enlever_mur(case,nx,voisin,verti,horiz):
    coord = coordonnee(case,nx)          
    valeur = case-voisin                 # relation entre les cases voisins
    # mur Ouest 
    if valeur == 1 :                                
        mur_ouest = coord[0] + coord[1] * (nx+1)
        retirer(verti,mur_ouest)
    # mur Est    
    elif valeur == -1 :                             
        mur_est = 1 + coord[0] + coord[1]* (nx+1)
        retirer(verti,mur_est)   
    # mur Nord
    elif valeur == nx :                            
        mur_nord = coord[0] + coord[1] * nx
        retirer(horiz,mur_nord)
    # mur Sud
    elif valeur == -nx :                            
        mur_sud = coord[0] + (coord[1]+1) * nx
        retirer(horiz,mur_sud)
        
# Fonction qui dessinera les murs à partir des ensembles de murs verticales et
# et horizontales disponibles
def dessiner_mur (ensemble,nx,ny,dimension,est_horiz):
    global NOIR 
    for mur in ensemble :
        if est_horiz:
            coord = coordonnee(mur,nx)      
           # dessine seulement les murs internes horizontaux du labyrinthe
            if mur >= nx and mur < nx*ny:
                for i in range(coord[0]*dimension, (coord[0]+1)*dimension):
                    set_pixel(i, coord[1]*dimension, NOIR)
        else:
            coord = coordonnee(mur,nx+1)    
           # dessine seulement les murs internes verticaux du labyrinthe
            if mur % (nx+1) != 0 and mur % (nx+1) != nx:
                for i in range(coord[1]*dimension, (coord[1]+1)*dimension):
                    set_pixel(coord[0]*dimension, i, NOIR)
                    
# Fonction qui prend une liste en paramètres pour la rendre aléatoire peut
# importe le nombre d'éléments dans celle-ci. 
def randomiser_liste(liste):
    for i in range(len(liste)-1, 0, -1):    # code repris du chapitre 8 p.104
        j = random_int(i)                   # index de 0 à i aléatoire 
        temp = liste[i]            
        liste[i] = liste[j]
        liste[j] = temp 
    return liste

# Procédure qui prend 3 paramètres pour créer le labyrinthe aléatoire à partir 
# de la largeur et la hauteur et les dimensions pixels en éliminant un mur à la 
# fois résultant à un arbre sous-tendant avec un point d'entrée et de sortie. 

def laby(nx, ny, dimension):
    global NOIR 
    global BLANC
    global TAILLE_PX
    largeur = nx*dimension
    hauteur = ny*dimension
    
    # initialisation du fond blanc
    set_screen_mode(largeur,hauteur)     
    fill_rectangle(0,0,largeur,ny*dimension, BLANC)
    
    cave = []                     # cellules mises dans la cavité
    front = []                    # cellules voisines de cave
    horiz = sequence(nx*(ny+1))   # ensemble de murs horizontaux
    verti = sequence((nx+1)*ny)   # ensemble de murs verticaux
    NB_CELLULES = nx*ny           # nombre de cellules 
    
    case_init = random_int(NB_CELLULES)  # cavité initiale choisie et
    cave.append(case_init)               # déclenche la suite pour front
    coord = coordonnee(case_init,nx)
    
    # déterminer les voisins de de la case initiale
    front = voisins(coord[0], coord[1], nx, ny)  

    while(len(cave) < NB_CELLULES):                         
        a_retirer = True
        random_index = random_int(len(front))  # index de front choisi 
        random_case = front[random_index]      # aléatoirement 
        
      # Trouver les cases voisins à random_case et les réassigner à la liste
      # aléatoirement 
        coord = coordonnee(random_case,nx)                   
        voisins_alea = voisins(coord[0],coord[1], nx, ny) 
        random_voisins = randomiser_liste(voisins_alea)    
                                                            
       # déterminer les voisins existants dans le labyrinthe et déterminer 
       # aléatoirement le mur à enlever des ensembles verti, horiz.
        for voisin in random_voisins:                    
            if not contient(cave, voisin):
                ajouter(front, voisin)
            elif a_retirer:
                enlever_mur(random_case,nx,voisin,verti,horiz)
                a_retirer = False

        retirer(front, random_case)
        ajouter(cave, random_case)
   
    # dessine_mur avec les murs restants dans chaque ensemble selon leur 
    # orientation horizontale ou verticale
    dessiner_mur(horiz,nx,ny,dimension,True)
    dessiner_mur(verti,nx,ny,dimension,False)
 
    # contour laby (murs externes) 
    fill_rectangle(dimension,0,dimension*(nx-1),TAILLE_PX, NOIR)     # en haut
    fill_rectangle(0,dimension*ny-1,dimension*(nx-1),TAILLE_PX, NOIR)# en bas 
    fill_rectangle(0,0,TAILLE_PX,dimension*ny,NOIR)                  # gauche
    fill_rectangle(dimension*nx-1,0,TAILLE_PX, dimension*ny,NOIR)    # droite 

print(laby(34, 18, 10))
