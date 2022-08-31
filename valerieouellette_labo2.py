class Pizza:

    PI = 3.1416
    
    def __init__(self, rayon, diametre, cout):
        self.rayon = rayon
        self.diametre = diametre
        self.cout = cout

class Boite:
    
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

class AppPizza:

    def __init__(self):
        self.liste_pizza = []
        self.liste_boite = []

    def menu(self):
        menu = {}
        menu[1] = "Créer une nouvelle pizza"
        menu[2] = "Créer une nouvelle boîte"
        menu[3] = "Voir la liste de pizzas"
        menu[4] = "Voir la liste de boîtes"
        menu[5] = "Comparer spécial 2 pour 1"
        menu[6] = "Mettre une pizza dans une boîte"
        menu[7] = "Sortir du programme"

        for numero, option in menu.items():
            print(f"{numero}) {option} \n")
        
        sortie = True
        while sortie:
            choix = input("Votre choix: ")
            if choix == "1":
                self.creation_pizza()
            elif choix == "2":
                self.creation_boite()
            elif choix == "3":
                self.afficher_liste_pizza()
            elif choix == "4":
                self.afficher_liste_pizza()
            elif choix == "5":
                self.special_deux_un()
            elif choix == "6":
                self.pizza_dans_boite()
            elif choix == "7":
                print("Au revoir")
                sortie = False
            else:
                print("Choix invalide")

    def creation_pizza(self):
        rayon = int(input("Entrez le rayon de la pizza: "))
        diametre = rayon * 2
        cout = int(input("Entrez le cout de la pizza: "))
        self.liste_pizza.append(Pizza(rayon, diametre, cout))

    def creation_boite(self):
        longueur = int(input("Entrez la longueur de la boîte: "))
        largeur = int(input("Entrez la largeur de la boîte: "))
        self.liste_boite.append(Boite(longueur, largeur))

    def afficher_liste_pizza(self):
        pass

    def afficher_liste_boite(self):
        pass

    def special_deux_un(self):
        pass

    def pizza_dans_boite(self):
        pass


