ballX=0
ballY=0
ballspeedX=5
ballspeedY=2
recsizeX = 50 #il s'agit de la longueur du rectangle
recX =0 # il s'agit de la position sur l'axe des abscices du rectangle
ballRadius =5 #le rayon de la balle
recY=0
recsizeY =10

def setup() :
    global ballX,ballY
    size(400,400)
    ballX=width/2
    ballY=height/2
    
def draw() :
    clear()
    drawRectangle()
    drawBall()

def drawRectangle() :
    global recizeX,recX,recY,recsizeY
    recX = mouseX-recsizeX/2 
    recY = height-20
    rect(recX,recY, recsizeX, recsizeY)
    
    

def drawBall() :
    global ballX,ballY,ballspeedX,ballspeedY,recsizeX,ballRadius,recY,recsizeY
    #les if sont placés avant pour vérifier la position de la balle avant de l'afficher à l'écran
    
    #droite et gauche si une condition n'est pas active l'autre l'est forcément
    if ballX>width-ballRadius :
        ballspeedX*=-1
    elif (ballX<ballRadius) :
        ballspeedX *= -1
        
    #haut et bas
    if (ballY<ballRadius):
        ballspeedY*=-1
    elif (ballY>height-ballRadius):
        ballspeedY*= -1
        recsizeX-=10 # à chaque fois que la balle touche le bas de la fenêtre la raquette perd 4 pixels
    
    #permet de laisser la raquette à 0 une fois qu'elle est réduite au maximum sinon elle se grandit de nouveau car les valeurs deviennent négatives 0 -> -2 -> -4 etc...
    if (recsizeX<=0):
        recsizeX=0
        print("perdu")
        
    circle(ballX,ballY, ballRadius*2)
    ballX+=ballspeedX
    ballY+=ballspeedY
    
    #ma version de la collision de la balle sur la raquette
    #if (ballY>height-25 and ballX>=recX and ballX<=recX+recsizeX) :
        #ballspeedY *= -1
    
    #version du prof, recY correspond au haut de la raquette et recY+recsizeY au bas de la raquette
    if (recY<ballY+ballRadius<recY+recsizeY and ballspeedY>0): #supérieur car les valeurs positives sont vers le bas (les coordonnées de la fenêtre 0,0 sont en haut à gauche)
        #ballspeedY>0 permet d'éviter de faire rebondir la balle sous la raquette car sa valeur est négative quand elle remonte
        if(recX<ballX<recX+recsizeX):
            ballspeedY *=-1
            ballY = recY-ballRadius
            
