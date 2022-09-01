#Classe Pizza avec 3 attributs: rayon, diametre et cout
#PI 3.1416 attribut de classe
#Classe Boite avec 2 attributs: longueur, largeur
#Class AppPizza avec menu, méthode création pizza, création boîte, affichage liste pizza, affichage liste boîte
#spécial deux pour un, pizza dans la boîte

class Pizza:

    PI = 3.1416
    
    def __init__(self, rayon, diametre, cout):
        self.rayon = rayon
        self.diametre = diametre
        self.cout = cout


    def __str__(self):
        return f"PIZZA rayon: {self.rayon}, diamètre: {self.diametre}, coût: {self.cout}"


class Boite:
    
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    

    def __str__(self):
        return f"BOÎTE longueur: {self.longueur}, largeur {self.largeur}"


class AppPizza:

    def __init__(self):
        self.liste_pizza = []
        self.liste_boite = []
        self.menu()


    def menu(self):
        menu = {}
        menu[1] = "Créer une nouvelle pizza"
        menu[2] = "Créer une nouvelle boîte"
        menu[3] = "Voir la liste de pizzas"
        menu[4] = "Voir la liste de boîtes"
        menu[5] = "Comparer spécial 2 pour 1"
        menu[6] = "Mettre une pizza dans une boîte"
        menu[7] = "Sortir du programme"

        sortie = True
        while sortie:
            print()

            for numero, option in menu.items():
                print(f"{numero}) {option} ")

            print()
            choix = input("Votre choix: ")

            if choix == "1":
                self.creation_pizza()
            elif choix == "2":
                self.creation_boite()
            elif choix == "3":
                self.afficher_liste_pizza()
            elif choix == "4":
                self.afficher_liste_boite()
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
        diametre = int(input("Entrez le diametre de la pizza: "))
        rayon = diametre / 2
        cout = int(input("Entrez le cout de la pizza: "))
        self.liste_pizza.append(Pizza(rayon, diametre, cout))


    def creation_boite(self):
        longueur = int(input("Entrez la longueur de la boîte: "))
        largeur = int(input("Entrez la largeur de la boîte: "))
        self.liste_boite.append(Boite(longueur, largeur))


    def afficher_liste_pizza(self):
        for pizza in self.liste_pizza:
            print(str(pizza))


    def afficher_liste_boite(self):
        for boite in self.liste_boite:
            print(str(boite))


    def special_deux_un(self):
        #Affiche liste pizza, choix pizza par utilisateur
        for i in range(len(self.liste_pizza)):
            print(f"{str(i+1)}) {str(self.liste_pizza[i])}")
        
        choix_pizza1 = int(input(f"Choisissez une pizza (1-{str(len(self.liste_pizza))}): "))
        pizza1 = self.liste_pizza[choix_pizza1 - 1]
        print(f"Votre choix: {str(pizza1)}")

        cout_special = int(input("Quel est le coût du spécial? "))
        if cout_special > (pizza1.cout * 2):
            print("Ce spécial n'en vaut pas la peine!")

        #Affiche liste pizza même prix que spécial
        else:
            liste_temp_pizza = []
            for pizza in self.liste_pizza:
                if pizza.cout == cout_special:
                    liste_temp_pizza.append(pizza)
            
            if len(liste_temp_pizza) == 0:
                print("Aucune pizza ne correspond à ce prix.")
            
            else:
                for i in range(len(liste_temp_pizza)):
                    print(f"{str(i+1)}) {liste_temp_pizza[i]}")
        
                #Choix deuxième pizza par utilisateur
                choix_pizza2 = int(input(f"Choisissez une pizza au même prix (1-{str(len(liste_temp_pizza))}): "))
                pizza2 = liste_temp_pizza[choix_pizza2 - 1]
                print(f"Votre choix: {str(pizza2)}")
        
                aire_pizza1 = Pizza.PI * (pizza1.rayon ** 2)
                aire_pizza2 = Pizza.PI * (pizza2.rayon ** 2)

                #Comparaison aire 2 pizza1 versus 1 pizza2
                if (aire_pizza1 * 2) > aire_pizza2:
                    print("Le spécial est avantageux!")
                elif (aire_pizza1 * 2) < aire_pizza2:
                    print("Le spécial n'est pas avantageux.")
                else:
                    print("Le spécial est aussi avantageux que la deuxième pizza.")


    def pizza_dans_boite(self):
        #Affiche liste pizza, choix pizza par utilisateur
        for i in range(len(self.liste_pizza)):
            print(f"{str(i+1)}) {str(self.liste_pizza[i])}")
        
        choix_pizza = int(input(f"Choisissez une pizza (1-{str(len(self.liste_pizza))}): "))
        pizza = self.liste_pizza[choix_pizza - 1]
        print(f"Votre choix: {str(pizza)}")

        #Affiche liste boite, choix boite par utilisateur
        for i in range(len(self.liste_boite)):
            print(f"{str(i+1)}) {str(self.liste_boite[i])}")
        
        choix_boite = int(input(f"Choisissez une boîte (1-{str(len(self.liste_boite))}): "))
        boite = self.liste_boite[choix_boite - 1]
        print(f"Votre choix: {str(boite)}")

        #Vérification pizza rentre dans boite
        if (pizza.diametre * 2.54) <= boite.largeur and (pizza.diametre * 2.54) <= boite.longueur:
            self.liste_pizza.remove(pizza)
            self.liste_boite.remove(boite)
            print("La pizza rentre dans la boîte.")
        else:
            print("La pizza ne rentre pas dans la boîte.")


app_pizza = AppPizza()

