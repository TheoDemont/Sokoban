#!/usr/bin/python3

# imports Widgets
import sys
from PyQt5.QtGui import QPainter, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction,  QWidget, QLabel, qApp
from PyQt5.QtCore import Qt

# imports files
import list_levels

# vérification si existe
app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

class Dessin(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        

def est_mur(x, y, static):
    if static[y][x] == 1 :
        return True
    else:
        return False

def est_sol(x, y, static):
    if static[y][x] == 5 or static[y][x] == 2:
        return True
    else:
        return False

def est_caisse(x, y, dynamic):
    if dynamic[y][x] == 3:
        return True
    else:
        return False

def est_objectif(x, y, static):
    if static[y][x] == 2:
        return True
    else:
        return False

# Classe principale
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sokoban")
        self.initUI()
        self.keypush = None
        self.compteur = 0
        self.level_actuel = 1
        self.posx = list_levels.level1_PosX()
        self.posy = list_levels.level1_PosY()
        self.static = list_levels.level1_Static()
        self.dynamic = list_levels.level1_Dynamic()
        self.nbobjectif = self.nbObjectif()
        self.nbValide = self.objectifValide()
        self.Width = len(self.static[0])*50+1
        self.Height = len(self.static)*50+22+20
        self.resize(self.Width, self.Height)

        # creating a label widget
        self.label_1 = QLabel("Niveau "+str(self.level_actuel))
        # adding label to status bar
        self.statusBar().addPermanentWidget(self.label_1)
        

    def paintEvent(self, event):
        rect = self.geometry()
        # vérification déplacement joueur (voir incrémentation compteur)
        posx = self.posx
        posy = self.posy
        
        h = (rect.height()-42)/len(self.static)
        w = (rect.width()-1)/len(self.static[0])
        
        if self.keypush == Qt.Key_Return and self.level_actuel<list_levels.nb_level() and self.nbobjectif == self.nbValide:
            self.level_actuel += 1
            self.load_level(self.level_actuel)

        if self.nbobjectif != self.nbValide:
            # Mur (1)
            painter = QPainter(self)
            painter.setPen(Qt.white)
            painter.setBrush(Qt.black)
            for i in range(len(self.static)):
                for j in range(len(self.static[0])):
                    if est_mur(j, i, self.static):
                        if ((rect.width()-len(self.static[0])*h)/2) >= 0:
                            painter.drawRect(j*h+(rect.width()-len(self.static[0])*h)/2,21+ i*h, h, h)
                        else:
                            painter.drawRect(j*w,i*w+(rect.height()-len(self.static)*w)/2, w, w)

            # Sol (5)
            painter.setPen(Qt.gray)
            painter.setBrush(Qt.gray)
            for i in range(len(self.static)):
                for j in range(len(self.static[0])):
                    if est_sol(j, i, self.static):
                        if ((rect.width()-len(self.static[0])*h)/2) >= 0:
                            painter.drawRect(int(j*h+(rect.width()-len(self.static[0])*h)/2),21+ i*h, h, h)
                        else:
                            painter.drawRect(j*w,i*w+(rect.height()-len(self.static)*w)/2, w, w)

            # Joueur (4)
            painter.setPen(Qt.white)
            painter.setBrush(Qt.red)

            if ((self.keypush == Qt.Key_D) or (self.keypush == Qt.Key_Right)) and not est_mur(self.posx+1, self.posy, self.static):
                if est_caisse(self.posx+1, self.posy, self.dynamic) and not est_caisse(self.posx+2, self.posy, self.dynamic) and not est_mur(self.posx+2, self.posy, self.static):
                    self.dynamic[self.posy][self.posx+1] = 0
                    self.dynamic[self.posy][self.posx+2] = 3
                if not est_caisse(self.posx+1, self.posy, self.dynamic):
                    self.posx += 1
            elif ((self.keypush == Qt.Key_Q) or (self.keypush == Qt.Key_Left)) and not est_mur(self.posx-1, self.posy, self.static):
                if est_caisse(self.posx-1, self.posy, self.dynamic) and not est_caisse(self.posx-2, self.posy, self.dynamic) and not est_mur(self.posx-2, self.posy, self.static):
                    self.dynamic[self.posy][self.posx-1] = 0
                    self.dynamic[self.posy][self.posx-2] = 3
                if not est_caisse(self.posx-1, self.posy, self.dynamic):
                    self.posx -= 1
            elif ((self.keypush == Qt.Key_S) or (self.keypush == Qt.Key_Down)) and not est_mur(self.posx, self.posy+1, self.static):
                if est_caisse(self.posx, self.posy+1, self.dynamic) and not est_caisse(self.posx, self.posy+2, self.dynamic) and not est_mur(self.posx, self.posy+2, self.static):
                    self.dynamic[self.posy+1][self.posx] = 0
                    self.dynamic[self.posy+2][self.posx] = 3
                if not est_caisse(self.posx, self.posy+1, self.dynamic):
                    self.posy += 1
            elif ((self.keypush == Qt.Key_Z) or (self.keypush == Qt.Key_Up)) and not est_mur(self.posx, self.posy-1, self.static):
                if est_caisse(self.posx, self.posy-1, self.dynamic) and not est_caisse(self.posx, self.posy-2, self.dynamic) and not est_mur(self.posx, self.posy-2, self.static):
                    self.dynamic[self.posy-1][self.posx] = 0
                    self.dynamic[self.posy-2][self.posx] = 3
                if not est_caisse(self.posx, self.posy-1, self.dynamic):
                    self.posy -= 1
            if ((rect.width()-len(self.static[0])*h)/2) >= 0:
                painter.drawEllipse(h/20+ self.posx*h+(rect.width()-len(self.static[0])*h)//2,21+ h/20+ self.posy*h, (9*h)/10, (9*h)/10)
            else:
                painter.drawEllipse(w/20+ self.posx*w, w/20 +self.posy*w+(rect.height()-len(self.static)*w)/2, (9*w)/10, (9*w)/10)

            # Caisses (3)
            painter.setPen(Qt.darkRed)
            painter.setBrush(Qt.red)

            for i in range(len(self.dynamic)):
                for j in range(len(self.dynamic[0])):
                    if est_caisse(j, i, self.dynamic):
                        
                        if ((rect.width()-len(self.static[0])*h)/2) >= 0:
                            painter.drawRect(h/10+ j*h+(rect.width()-len(self.static[0])*h)//2,21+ h/10+ i*h, (8*h)/10, (8*h)/10)
                        else:
                            painter.drawRect(w/10+ j*w, w/10 +i*w+(rect.height()-len(self.static)*w)/2, (8*w)/10, (8*w)/10)

            # Coloration des caisses
            painter.setPen(Qt.darkGreen)
            painter.setBrush(Qt.green)

            for i in range(len(self.static)):
                for j in range(len(self.static[0])):
                    if est_objectif(j, i, self.static):
                        if est_caisse(j, i, self.dynamic):
                            if ((rect.width()-len(self.static[0])*h)/2) >= 0:
                                painter.drawRect(h/10+ j*h+(rect.width()-len(self.static[0])*h)//2,21+ h/10+ i*h, (8*h)/10, (8*h)/10)
                            else:
                                painter.drawRect(w/10+ j*w, w/10 +i*w+(rect.height()-len(self.static)*w)/2, (8*w)/10, (8*w)/10)

            # Objectif (2)
            painter.setPen(Qt.darkYellow)
            painter.setBrush(Qt.yellow)

            for i in range(len(self.static)):
                for j in range(len(self.static[0])):
                    if est_objectif(j, i, self.static):
                        if est_caisse(j, i, self.dynamic):
                            if ((rect.width()-len(self.static[0])*h)/2) >= 0:
                                painter.drawRect((3*h)/10+ j*h+(rect.width()-len(self.static[0])*h)//2,21+ (3*h)/10+ i*h, (4*h)/10, (4*h)/10)
                            else:
                                painter.drawRect((3*w)/10+ j*w, (3*w)/10 +i*w+(rect.height()-len(self.static)*w)/2, (4*w)/10, (4*w)/10)
                        else:
                            if ((rect.width()-len(self.static[0])*h)/2) >= 0:
                                painter.drawEllipse((3*h)/10+ j*h+(rect.width()-len(self.static[0])*h)//2,21+ (3*h)/10+ i*h, (4*h)/10, (4*h)/10)
                            else:
                                painter.drawEllipse((3*w)/10+ j*w, (3*w)/10 +i*w+(rect.height()-len(self.static)*w)/2, (4*w)/10, (4*w)/10)
            
                       

            # Incrémentation du compteur
            if posx != self.posx or posy !=self.posy:
                self.compteur += 1
                self.keypush = None
            self.statusBar().showMessage("Nombre de pas: "+str(self.compteur))
            
            

            self.nbValide = self.objectifValide()
            self.nbobjectif = self.nbObjectif()
            

            # Message de fin de niveau
            if self.nbobjectif == self.nbValide:
                if self.level_actuel != list_levels.nb_level():
                    label = QLabel("Félicitations, vous avez gagné en "+str(self.compteur)+" pas.<br/>Pour passer au niveau suivant, appuyez sur Entrer.")
                else:
                    label = QLabel("Félicitations, vous avez gagné en "+str(self.compteur)+" pas.<br/>Vous avez fini le dernier niveau.<br/>Appuyez sur Échap pour quitter.")
                
                label.setFont(QFont("Comic Sans MS", self.geometry().height()*0.03))
                label.setWordWrap(True)
                self.centralWidget = label
                self.centralWidget.setAlignment(Qt.AlignCenter)
                self.setCentralWidget(self.centralWidget)
            
            
            else:
                self.centralWidget = None
                self.setCentralWidget(self.centralWidget)
        

        
            
            
    # Mise en place des barres d'outils
    def initUI(self):
        reloadAction = QAction('&Réinitialiser', self)
        reloadAction.setShortcut('R')
        reloadAction.triggered.connect(self.reload)

        exitAction = QAction('&Quitter', self)        
        exitAction.setShortcut('Esc')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Fichier')
        fileMenu.addAction(reloadAction) 
        fileMenu.addAction(exitAction)
        
        level = menubar.addMenu('&Niveau') 
        
        tab_level = []
        for i in range(list_levels.nb_level()):
            tab_level.append(QAction('&Niveau '+str(i+1),self))
        tab_level[0].triggered.connect(lambda:self.load_level(1))    
        level.addAction(tab_level[0])
        tab_level[1].triggered.connect(lambda:self.load_level(2))    
        level.addAction(tab_level[1])
        tab_level[2].triggered.connect(lambda:self.load_level(3))    
        level.addAction(tab_level[2])
        tab_level[3].triggered.connect(lambda:self.load_level(4))    
        level.addAction(tab_level[3])
        tab_level[4].triggered.connect(lambda:self.load_level(5))    
        level.addAction(tab_level[4])
        tab_level[5].triggered.connect(lambda:self.load_level(6))    
        level.addAction(tab_level[5]) 
        tab_level[6].triggered.connect(lambda:self.load_level(7))    
        level.addAction(tab_level[6]) 
        tab_level[7].triggered.connect(lambda:self.load_level(8))    
        level.addAction(tab_level[7]) 
        tab_level[8].triggered.connect(lambda:self.load_level(9))    
        level.addAction(tab_level[8]) 
        tab_level[9].triggered.connect(lambda:self.load_level(10))    
        level.addAction(tab_level[9])  
        tab_level[10].triggered.connect(lambda:self.load_level(11))    
        level.addAction(tab_level[10])
        tab_level[11].triggered.connect(lambda:self.load_level(12))    
        level.addAction(tab_level[11])                          

  
        
        

    # Rechargement du niveau
    def reload(self):
        i = self.level_actuel
        self.posx = eval('list_levels.level'+str(i)+'_PosX')()
        self.posy = eval('list_levels.level'+str(i)+'_PosY')()
        self.static = eval('list_levels.level'+str(i)+'_Static')()
        self.dynamic = eval('list_levels.level'+str(i)+'_Dynamic')()
        self.compteur = 0
        self.nbValide = self.objectifValide()
        self.nbobjectif = self.nbObjectif()
        self.update()   

    # Chargment du niveau
    def load_level(self, i):
        rect = self.geometry()
    

        self.taille_case = (rect.height()-42)/len(self.static)
        self.posx = eval('list_levels.level'+str(i)+'_PosX')()
        self.posy = eval('list_levels.level'+str(i)+'_PosY')()
        self.static = eval('list_levels.level'+str(i)+'_Static')()
        self.dynamic = eval('list_levels.level'+str(i)+'_Dynamic')()
        self.Width = len(self.static[0])*50+1
        self.Height = len(self.static)*50+22+20
        
        rect = self.geometry()        
        h = (rect.height()-42)/len(self.static)
        w = (rect.width()-1)/len(self.static[0])

        if not self.isMaximized():
            self.resize(self.taille_case*len(self.static[0])+1, self.taille_case*len(self.static)+42)
            

        self.compteur = 0
        self.level_actuel = i
        self.nbValide = self.objectifValide()
        self.nbobjectif = self.nbObjectif()

        # creating a label widget
        self.statusBar().removeWidget(self.label_1)
        self.label_1 = QLabel("Niveau "+str(self.level_actuel))
        # adding label to status bar
        self.statusBar().addPermanentWidget(self.label_1)
        self.statusBar().update()
        self.update()

    def nbObjectif(self):
        nbObjectif = 0
        for i in range(len(self.static[0])):
            for j in range(len(self.static)):
                if self.static[j][i] == 2:
                    nbObjectif += 1
        return nbObjectif

    def objectifValide(self):
        nbValide = 0
        for i in range(len(self.static[0])):
            for j in range(len(self.static)):
                if self.dynamic[j][i] == 3 and self.static[j][i] == 2:
                    nbValide += 1
        return nbValide
    
    # Récupération des touches du clavier
    def keyPressEvent(self, event):
        self.keypush = event.key()
        self.update()  


# instance
window = MainWindow()
window.show()
sys.exit(app.exec_())