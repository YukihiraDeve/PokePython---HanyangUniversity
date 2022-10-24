#Projet Game Pokemon in Python. No use Graphic librairys

def initGame():
    print("initGame")
    Pokedex = []
    InitPokedex(Pokedex)
    PokedexDisplay(Pokedex)
    print("-- Pokedex create --")


    print("Welcome to the world of Pokemon !")




class Pokemon():
    def __init__(self, name, level, type, life, number):
        self.name = name
        self.level = level
        self.type = type
        self.life = life
        self.number = number


def InitPokedex(Pokedex):
    Pokedex.append(Pokemon("Bulbizarre", 5, "Plante", 100, 1))
    Pokedex.append(Pokemon("Salameche", 5, "Fire", 100, 4))
    Pokedex.append(Pokemon("Carapuce", 5, "Water", 100, 7))
    Pokedex.append(Pokemon("Pikachu", 5, "Electrik", 100, 10))

def PokedexDisplay(Pokedex):
    print("Pokedex")
    for pokemon in Pokedex:
        print(pokemon.name, pokemon.level, pokemon.type, pokemon.life, pokemon.number)


initGame()

