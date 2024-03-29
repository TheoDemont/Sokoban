"""
légende:

0 = vide
1 = mur
2 = objectif
3 = Caisse
4 = joueur
5 = sol
"""
# Nombre de niveaux
def nb_level():
    return 12


# Niveau 1
def level1_Static():
    static = [
        [0,0,1,1,1,1,1,0],
        [1,1,1,5,5,5,1,0],
        [1,2,5,5,5,5,1,0],
        [1,1,1,5,5,2,1,0],
        [1,2,1,1,5,5,1,0],
        [1,5,1,5,2,5,1,1],
        [1,5,5,2,5,5,2,1],
        [1,5,5,5,2,5,5,1],
        [1,1,1,1,1,1,1,1]
    ]
    return static

def level1_Dynamic():
    dynamic = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,3,0,0,0,0],
        [0,0,0,0,3,0,0,0],
        [0,0,0,0,3,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,3,0,3,3,3,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
    ]
    return dynamic

def level1_PosX():
    return 2

def level1_PosY():
    return 2


# Niveau 2
def level2_Static():
    static = [
        [0,0,1,1,1,1,1,0],
        [1,1,1,5,5,5,1,0],
        [1,5,5,5,1,5,1,1],
        [1,5,1,5,5,2,5,1],
        [1,5,5,5,5,1,5,1],
        [1,1,5,1,5,5,5,1],
        [0,1,5,5,5,1,1,1],
        [0,1,1,1,1,1,0,0]
    ]
    return static

def level2_Dynamic():
    dynamic = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,3,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
    ]
    return dynamic

def level2_PosX():
    return 3

def level2_PosY():
    return 2


# Niveau 3
def level3_Static():
    static = [
        [1,1,1,1,1,0,0,0,0],
        [1,5,5,5,1,0,0,0,0],
        [1,5,5,5,1,0,1,1,1],
        [1,5,5,5,1,0,1,2,1],
        [1,1,1,5,1,1,1,2,1],
        [0,1,1,5,5,5,5,2,1],
        [0,1,5,5,5,1,5,5,1],
        [0,1,5,5,5,1,1,1,1],
        [0,1,1,1,1,1,0,0,0]
    ]
    return static

def level3_Dynamic():
    dynamic = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,3,0,0,0,0,0,0],
        [0,0,3,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,3,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    return dynamic

def level3_PosX():
    return 2

def level3_PosY():
    return 6


# Niveau 4
def level4_Static():
    static = [
        [0,1,1,1,1,0],
        [1,1,5,5,1,0],
        [1,5,5,5,1,0],
        [1,1,5,5,1,1],
        [1,1,5,5,5,1],
        [1,2,5,5,5,1],
        [1,2,2,2,2,1],
        [1,1,1,1,1,1]
    ]
    return static

def level4_Dynamic():
    dynamic = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,3,0,0],
        [0,0,3,0,0,0],
        [0,0,0,3,0,0],
        [0,0,3,0,0,0],
        [0,0,0,3,0,0],
        [0,0,0,0,0,0]
    ]
    return dynamic

def level4_PosX():
    return 2

def level4_PosY():
    return 2


# Niveau 5
def level5_Static():
    static = [
        [0,1,1,1,1,0,0,0],
        [0,1,5,5,1,1,1,0],
        [0,1,5,5,5,5,1,0],
        [1,1,1,5,1,5,1,1],
        [1,2,1,5,1,5,5,1],
        [1,2,5,5,5,1,5,1],
        [1,2,5,5,5,5,5,1],
        [1,1,1,1,1,1,1,1]
    ]
    return static

def level5_Dynamic():
    dynamic = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,3,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,3,0,0,0,0,0],
        [0,0,0,0,0,3,0,0],
        [0,0,0,0,0,0,0,0]
    ]
    return dynamic

def level5_PosX():
    return 2

def level5_PosY():
    return 1


# Niveau 6
def level6_Static():
    static = [
        [0,0,1,1,1,1,1,1],
        [0,0,1,5,5,5,5,1],
        [1,1,1,5,5,5,5,1],
        [1,5,5,5,2,2,5,1],
        [1,5,5,2,2,2,1,1],
        [1,1,1,1,5,5,1,0],
        [0,0,0,1,1,1,1,0]
    ]
    return static

def level6_Dynamic():
    dynamic = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,3,3,3,0,0],
        [0,0,0,3,0,0,0,0],
        [0,0,3,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
    ]
    return dynamic

def level6_PosX():
    return 1

def level6_PosY():
    return 3


# Niveau 7
def level7_Static():
    static = [
        [0,0,1,1,1,1,1,0],
        [1,1,1,5,5,5,1,0],
        [1,5,5,5,2,5,1,1],
        [1,5,5,2,5,2,5,1],
        [1,1,1,5,2,5,5,1],
        [0,0,1,5,5,5,1,1],
        [0,0,1,1,1,1,1,0]
    ]
    return static

def level7_Dynamic():
    dynamic = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,3,0,0,0,0],
        [0,0,0,0,3,0,0,0],
        [0,0,0,0,3,3,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
    ]
    return dynamic

def level7_PosX():
    return 5

def level7_PosY():
    return 1


# Niveau 8
def level8_Static():
    static = [
        [0,0,1,1,1,1,0,0],
        [0,0,1,2,2,1,0,0],
        [0,1,1,5,2,1,1,0],
        [0,1,5,5,5,2,1,0],
        [1,1,5,5,5,5,1,1],
        [1,5,5,1,5,5,5,1],
        [1,5,5,5,5,5,5,1],
        [1,1,1,1,1,1,1,1]
    ]
    return static

def level8_Dynamic():
    dynamic = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,3,0,0,0],
        [0,0,0,3,0,0,0,0],
        [0,0,0,0,3,3,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
    ]
    return dynamic

def level8_PosX():
    return 3

def level8_PosY():
    return 6


# Niveau 9
def level9_Static():
    static = [
        [1,1,1,1,1,1,1,1],
        [1,5,5,1,5,5,5,1],
        [1,5,5,2,2,5,5,1],
        [1,5,5,2,2,5,1,1],
        [1,5,5,2,2,5,5,1],
        [1,5,5,1,5,5,5,1],
        [1,1,1,1,1,1,1,1]
    ]
    return static

def level9_Dynamic():
    dynamic = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,3,0,0,3,0,0],
        [0,0,3,0,3,0,0,0],
        [0,0,3,0,0,3,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
    ]
    return dynamic

def level9_PosX():
    return 1

def level9_PosY():
    return 3


# Niveau 10
def level10_Static():
    static = [
        [1,1,1,1,1,1,0,0,0],
        [1,5,5,5,5,1,0,0,0],
        [1,5,5,5,5,1,1,0,0],
        [1,5,5,1,2,2,1,1,1],
        [1,1,5,5,2,2,5,5,1],
        [0,1,5,5,5,5,5,5,1],
        [0,1,1,1,1,1,1,1,1]
    ]
    return static

def level10_Dynamic():
    dynamic = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,3,3,3,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,3,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    return dynamic

def level10_PosX():
    return 3

def level10_PosY():
    return 5


# Niveau 11
def level11_Static():
    static = [
        [1,1,1,1,1,1,1],
        [1,2,2,5,2,2,1],
        [1,2,2,1,2,2,1],
        [1,5,5,5,5,5,1],
        [1,5,5,5,5,5,1],
        [1,5,5,5,5,5,1],
        [1,5,5,1,5,5,1],
        [1,1,1,1,1,1,1]
    ]
    return static

def level11_Dynamic():
    dynamic = [
        [0,0,0,0,0,0,0],
        [0,0,0,3,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,3,3,3,0,0],
        [0,0,0,3,0,0,0],
        [0,0,3,3,3,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ]
    return dynamic

def level11_PosX():
    return 4

def level11_PosY():
    return 6


# Niveau 12
def level12_Static():
    static = [
        [1,1,1,1,1,1],
        [1,5,5,5,5,1],
        [1,5,5,5,5,1],
        [1,1,2,5,5,1],
        [1,5,2,5,1,1],
        [1,5,2,5,1,0],
        [1,5,2,5,1,0],
        [1,5,2,5,1,0],
        [1,1,1,1,1,0]
    ]
    return static

def level12_Dynamic():
    dynamic = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,3,0,0,0],
        [0,0,3,0,0,0],
        [0,0,3,0,0,0],
        [0,0,3,0,0,0],
        [0,0,3,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]
    ]
    return dynamic

def level12_PosX():
    return 4

def level12_PosY():
    return 2