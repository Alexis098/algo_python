#ceci est un commentaire, il ne sera pas exécuté par la machine 
#ici on définit la fonction setup qui sera exécuté comme point d'entrée de mon code
def setup():
    #on appel la fonction print pour écrire dans la console 
    print("Hello World") #print imprime/affiche dans la console ce qu'il se trouve dans la paranthèse
    #ici on définit la taille de la fenêtre
    size(400,400)
    #on définit la couleur avec laquele on va remplir les formes suivantes
    fill(128, 0, 0)
    #le premier nombre de l'ellipse correspond à sa position sur l'axe des abscisses, le second nombre sa position sur l'axe des ordonnées, les deux autres définissent respectivement sa largeur et hauteur
    #dessine une ellipse avec les paramètres suivants : x, y, largeur de l'ellipse, hauteur de l'ellipse
    ellipse(50, 50, 40, 40) 
    fill(176, 78, 290)
    ellipse(150, 150, 60, 80) 
    #ici, on change le framerate de l'application
    frameRate(120)

def draw(): #la fonction draw fait tourner en boucle les éléments dedans #j'appelle la fonction draw car je veux que le programme dessine ce que je veux selon les instructions suiavantes comprises dans la fonction
    clear()#efface chaque cercle à chaque fois qu'on bouge la souris pour n'en avoir qu'un d'affiché à la fois, vide la fenêtre
    fill(255)
    ellipse(mouseX, mouseY, 80, 80)#dessine un cercle à l'emplacement de la souris, mais ne les effacent pas une fois qu'on bouge la souris, cumule les cercles
    #on récupère les coordonnées de la souris avec mouseX et mouseY
    
    ellipse(width/2, height/2+ cos(millis()*0.002)*100, 40, 40)# on dessine un cercle au centre de l'écran avec width et height divisés par 2
    #rajouter la fonction cos permet de donner du mouvement sur l'axe des ordonnées au cercle, millis signifie que la position du Y donné par la fonction cos change (suite dessous)
    #en fonction du temps. La fonction cos allant de 1 à -1 pour l'axe des ordonnées, on multiplie cette fonction par, ici, 100 pour avoir une plus grande amplitude qu'une amplitude allant de -1 à 1 pixel.
    #diviser le temps (le fois 0.002) permet de ralentir la vitesse du mouvement du cercle
    
    #essayer chaque semaine de reproduire une ou deux fois le code réalisé en classe sans regarder le code source pour reproduire le résultat obtenu en classe pour le cours suivant
