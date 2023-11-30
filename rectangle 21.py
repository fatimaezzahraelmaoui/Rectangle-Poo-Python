class Rectangle:
    NbrRectangle = 0
    def __init__(self,longueur,largeur):
        self.__longueur = longueur 
        self.__largeur = largeur 
        Rectangle.NbrRectangle += 1
        def getlongueur(self):
            return self.__longueur
        def setlongueur(self,longueur):
            self.__longueur = longueur
        def getlargeur(self):
            return self.larguer
        def setlarguer(self,largeur):
            self.__largeur = largeur
    def perimetre(self):
        self.perimetre = 2*(self.__longueur + self.__largeur)
        return self.perimetre
    def Surface(self):
        self.Surface = (self.__longueur * self.__largeur)
        return self.Surface
    def Equals(self,other=2):
        if (self.__longueur == other.__longueur) and (self.__largeur == other.__largeur):
            return True
        else :
            return False
    def ToSTring(self):
        return ("largeur est :",self.__largeur ,"longueur :", self.__longueur)
    
class Parallélépipède(Rectangle):
    NbrParallélépipère =0
    def __init__(self,largeur,longueur,hauteur):
        Rectangle.__init__(self,largeur,longueur)
        self.__largeur = largeur
        self.__longueur = longueur
        self.__hauteur = hauteur
        Parallélépipède.NbrParallélépipère += 1
    def gethauteur(self):
        return self.__hauteur
    def sethauteur(self,hauteur):
        self.__hauteur = hauteur
    def Equals(self,other=2):
        if (self.__largeur == other.__largeur)and(self.__longueur == other.__longueur)and(self.__hauteur == other.__hauteur) :
            return True
        else :
            return False
    def Surface(self):
        self.Surface = (self.__largeur*self.__longueur*2 ) +(self.__hauteur*self.__largeur*2)+(self.__hauteur*self.__longueur*2)
        return self.Surface
    def Volume(self):
        self.Volume = (self.__largeur*self.__longueur*self.__hauteur)
        return self.Volume
    def ToString(self):
        return ("largeur est :",self.__largeur ,"longueur :", self.__longueur,"hauteur :",self.__hauteur)
    
RE1 = Rectangle(2,4)
print(RE1.Equals())
print(RE1.Surface())
print(RE1.perimetre())
print(RE1.ToSTring())
print(RE1.NbrRectangle)


PE1 = Parallélépipède(3,1,5)
print(PE1.Equals())
print(PE1.Surface())
print(PE1.Volume())
print(PE1.ToSTring())
print(PE1.NbrParallélépipère)
    