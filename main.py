#Projet Game Pokemon in Python. No use Graphic librairys




#Variable Globale


from nis import cat


team = 0
Pokedex = []
PokemonTeam = []
MAX_POKEMON_TEAM = 6
MIN_POKEMON_TEAM = 1
global Player


def initGame():
    InitPokedex()
    main()




def main():
    Pokemon2 = Pokedex[0]
    Pokemon3 = Pokedex[0]
    Pokemon4 = Pokedex[0]
    Pokemon5 = Pokedex[0]
    Pokemon6 = Pokedex[0]

    print("Welcome to the world of Pokemon !")
    sexe = input("What is your sexe ? (M/F) : ")
    name = input("What is your name ?")
    print("Nice to meet you", name )
    print("It's the time for chose your starter")
    choise = input("1.Bulbizare / 2.Salamèche / 3.Carapuce")
    if choise == "1" :
        Starter = Pokedex[1]
        print("Vous avez choisis", Starter.name)

    Player = Dresseur(name, sexe, Starter, Pokemon2, Pokemon3, Pokemon4, Pokemon5, Pokemon6)

    print("Enjoy", Player.name, Player.Pokemon1)

    Menu(Player)

#Pokemon class
class Pokemon():
    def __init__(self, name, level, type, life, id):
        self.name = name
        self.level = level
        self.type = type
        self.life = life
        self.id = id


#Init Pokemon

def InitPokedex():
    Any = Pokemon("None", 0, "None", 0, 0)
    Bulbizare = Pokemon("Bulbizarre", 5, "Plante", 100, 1)
    Herbizare = Pokemon("Herbizarre", 5, "Feu", 100, 2)
    Florizare = Pokemon("Florizarre", 5, "Eau", 100, 3)
    Salameche = Pokemon("Salameche", 5, "Fire", 100, 4)
    Reptincel = Pokemon("Reptincel", 5, "Fire", 100, 5)
    Dracaufeu = Pokemon("Dracaufeu", 5, "Fire", 100, 6)
    Carapuce  = Pokemon("Carapuce", 5, "Water", 100, 7)
    Carabaffe = Pokemon("Carabaffe", 5, "Water", 100, 8)
    Tortank   = Pokemon("Tortank", 5, "Water", 100, 9)
    Pokedex.append(Any)
    Pokedex.append(Bulbizare)
    Pokedex.append(Herbizare)
    Pokedex.append(Florizare)
    Pokedex.append(Salameche)
    Pokedex.append(Reptincel)
    Pokedex.append(Dracaufeu)
    Pokedex.append(Carapuce)
    Pokedex.append(Carabaffe)
    Pokedex.append(Tortank)


class Dresseur:
    def __init__(self, name, sexe, Pokemon1, Pokemon2, Pokemon3, Pokemon4, Pokemon5, Pokemon6):
        self.name = name
        self.sexe = sexe
        self.Pokemon1 = Pokemon1
        self.Pokemon2 = Pokemon2
        self.Pokemon3 = Pokemon3
        self.Pokemon4 = Pokemon4
        self.Pokemon5 = Pokemon5
        self.Pokemon6 = Pokemon6

    def TeamPokemon(self):
        print("1.", self.Pokemon1.name)
        while True:
            try:
                print("2.", self.Pokemon2.name)
                print("3.", self.Pokemon3.name)
                print("4.", self.Pokemon4.name)
                print("5.", self.Pokemon5.name)
                print("6.", self.Pokemon6.name)

                break
            except ValueError:
                print("Error team")



#Affichage Pokedex
def PokedexDisplay():
    print("Pokedex")
    for pokemon in Pokedex:
        print(pokemon.id,".", pokemon.name, pokemon.type)
    Menu()


#Menu init
def Menu(Player):
    
    print("Menu")
    print("1 - Pokedex")
    print("2 - Team")
    print("3 - Exit")
    choice = input("Choice : ")
    if choice == "1":
        PokedexDisplay()
    elif choice == "2":
        Player.TeamPokemon()
    elif choice == "3":
        exit()




initGame()

