#Projet Game Pokemon in Python. No use Graphic librairys




#Variable Globale
Pokedex = []


def initGame():
    InitPokedex()
    main()



def main():
    print("Welcome to the world of Pokemon !")
    Menu()

#Pokemon class
class Pokemon():
    def __init__(self, name, level, type, life, number):
        self.name = name
        self.level = level
        self.type = type
        self.life = life
        self.number = number


#Init Pokemon

def InitPokedex():
    Pokedex.append(Pokemon("Bulbizarre", 5, "Plante", 100, 1))
    Pokedex.append(Pokemon("Herbizarre", 5, "Feu", 100, 2))
    Pokedex.append(Pokemon("Florizarre", 5, "Eau", 100, 3))
    Pokedex.append(Pokemon("Salameche", 5, "Fire", 100, 4))
    Pokedex.append(Pokemon("Reptincel", 5, "Fire", 100, 5))
    Pokedex.append(Pokemon("Dracaufeu", 5, "Fire", 100, 6))
    Pokedex.append(Pokemon("Carapuce", 5, "Water", 100, 7))
    Pokedex.append(Pokemon("Carabaffe", 5, "Water", 100, 8))
    Pokedex.append(Pokemon("Tortank", 5, "Water", 100, 9))
    Pokedex.append(Pokemon("Chenipan", 5, "Insect", 100, 10))
    Pokedex.append(Pokemon("Chrysacier", 5, "Insect", 100, 11))
    Pokedex.append(Pokemon("Papilusion", 5, "Insect", 100, 12))
    Pokedex.append(Pokemon("Aspicot", 5, "Insect", 100, 13))
    Pokedex.append(Pokemon("Coconfort", 5, "Insect", 100, 14))
    Pokedex.append(Pokemon("Dardargnan", 5, "Insect", 100, 15))
    Pokedex.append(Pokemon("Roucool", 5, "Normal", 100, 16))
    Pokedex.append(Pokemon("Roucoups", 5, "Normal", 100, 17))
    Pokedex.append(Pokemon("Roucarnage", 5, "Normal", 100, 18))
    Pokedex.append(Pokemon("Rattata", 5, "Normal", 100, 19))
    Pokedex.append(Pokemon("Rattatac", 5, "Normal", 100, 20))
    Pokedex.append(Pokemon("Piafabec", 5, "Normal", 100, 21))
    Pokedex.append(Pokemon("Rapasdepic", 5, "Normal", 100, 22))
    Pokedex.append(Pokemon("Abo", 5, "Normal", 100, 23))
    Pokedex.append(Pokemon("Arbok", 5, "Normal", 100, 24))
    Pokedex.append(Pokemon("Pikachu", 5, "Electric", 100, 25))
    Pokedex.append(Pokemon("Raichu", 5, "Electric", 100, 26))
    Pokedex.append(Pokemon("Sabelette", 5, "Normal", 100, 27))
    Pokedex.append(Pokemon("Sablaireau", 5, "Normal", 100, 28))
    Pokedex.append(Pokemon("Nidoran", 5, "Poison", 100, 29))
    Pokedex.append(Pokemon("Nidorina", 5, "Poison", 100, 30))
    Pokedex.append(Pokemon("Nidoqueen", 5, "Poison", 100, 31))
    Pokedex.append(Pokemon("Nidoran", 5, "Poison", 100, 32))
    Pokedex.append(Pokemon("Nidorino", 5, "Poison", 100, 33))
    Pokedex.append(Pokemon("Nidoking", 5, "Poison", 100, 34))
    Pokedex.append(Pokemon("Melo", 5, "Normal", 100, 35))
    Pokedex.append(Pokemon("Melodelfe", 5, "Normal", 100, 36))
    Pokedex.append(Pokemon("Goupix", 5, "Fire", 100, 37))
    Pokedex.append(Pokemon("Feunard", 5, "Fire", 100, 38))
    Pokedex.append(Pokemon("Rondoudou", 5, "Normal", 100, 39))
    Pokedex.append(Pokemon("Grodoudou", 5, "Normal", 100, 40))
    Pokedex.append(Pokemon("Nosferapti", 5, "Poison", 100, 41))
    Pokedex.append(Pokemon("Nosferalto", 5, "Poison", 100, 42))
    Pokedex.append(Pokemon("Mystherbe", 5, "Plante", 100, 43))
    Pokedex.append(Pokemon("Ortide", 5, "Plante", 100, 44))
    Pokedex.append(Pokemon("Rafflesia", 5, "Plante", 100, 45))
    Pokedex.append(Pokemon("Paras", 5, "Insect", 100, 46))
    Pokedex.append(Pokemon("Parasect", 5, "Insect", 100, 47))
    Pokedex.append(Pokemon("Mimitoss", 5, "Insect", 100, 48))
    Pokedex.append(Pokemon("Aéromite", 5, "Insect", 100, 49))
    Pokedex.append(Pokemon("Taupiqueur", 5, "Normal", 100, 50))
    Pokedex.append(Pokemon("Triopikeur", 5, "Normal", 100, 51))
    Pokedex.append(Pokemon("Miaouss", 5, "Normal", 100, 52))
    Pokedex.append(Pokemon("Persian", 5, "Normal", 100, 53))
    Pokedex.append(Pokemon("Psykokwak", 5, "Water", 100, 54))
    Pokedex.append(Pokemon("Akwakwak", 5, "Water", 100, 55))
    Pokedex.append(Pokemon("Férosinge", 5, "Normal", 100, 56))
    Pokedex.append(Pokemon("Colossinge", 5, "Normal", 100, 57))
    Pokedex.append(Pokemon("Caninos", 5, "Normal", 100, 58))
    Pokedex.append(Pokemon("Arcanin", 5, "Normal", 100, 59))
    Pokedex.append(Pokemon("Ptitard", 5, "Water", 100, 60))
    Pokedex.append(Pokemon("Têtarte", 5, "Water", 100, 61))
    Pokedex.append(Pokemon("Tartard", 5, "Water", 100, 62))
    Pokedex.append(Pokemon("Abra", 5, "Psychic", 100, 63))
    Pokedex.append(Pokemon("Kadabra", 5, "Psychic", 100, 64))
    Pokedex.append(Pokemon("Alakazam", 5, "Psychic", 100, 65))
    Pokedex.append(Pokemon("Machoc", 5, "Fighting", 100, 66))
    Pokedex.append(Pokemon("Machopeur", 5, "Fighting", 100, 67))
    Pokedex.append(Pokemon("Mackogneur", 5, "Fighting", 100, 68))
    Pokedex.append(Pokemon("Chétiflor", 5, "Plante", 100, 69))
    Pokedex.append(Pokemon("Boustiflor", 5, "Plante", 100, 70))
    Pokedex.append(Pokemon("Empiflor", 5, "Plante", 100, 71))
    Pokedex.append(Pokemon("Tentacool", 5, "Water", 100, 72))
    Pokedex.append(Pokemon("Tentacruel", 5, "Water", 100, 73))
    Pokedex.append(Pokemon("Racaillou", 5, "Rock", 100, 74))
    Pokedex.append(Pokemon("Gravalanch", 5, "Rock", 100, 75))
    Pokedex.append(Pokemon("Grolem", 5, "Rock", 100, 76))
    Pokedex.append(Pokemon("Ponyta", 5, "Fire", 100, 77))
    Pokedex.append(Pokemon("Galopa", 5, "Fire", 100, 78))
    Pokedex.append(Pokemon("Ramoloss", 5, "Water", 100, 79))
    Pokedex.append(Pokemon("Flagadoss", 5, "Water", 100, 80))
    Pokedex.append(Pokemon("Magnéti", 5, "Electric", 100, 81))
    Pokedex.append(Pokemon("Magnéton", 5, "Electric", 100, 82))
    Pokedex.append(Pokemon("Canarticho", 5, "Normal", 100, 83))
    Pokedex.append(Pokemon("Doduo", 5, "Normal", 100, 84))
    Pokedex.append(Pokemon("Dodrio", 5, "Normal", 100, 85))
    Pokedex.append(Pokemon("Otaria", 5, "Water", 100, 86))
    Pokedex.append(Pokemon("Lamantine", 5, "Water", 100, 87))
    Pokedex.append(Pokemon("Tadmorv", 5, "Poison", 100, 88))
    Pokedex.append(Pokemon("Grotadmorv", 5, "Poison", 100, 89))
    Pokedex.append(Pokemon("Kokiyas", 5, "Water", 100, 90))
    Pokedex.append(Pokemon("Crustabri", 5, "Water", 100, 91))
    Pokedex.append(Pokemon("Fantominus", 5, "Ghost", 100, 92))
    Pokedex.append(Pokemon("Spectrum", 5, "Ghost", 100, 93))
    Pokedex.append(Pokemon("Ectoplasma", 5, "Ghost", 100, 94))
    Pokedex.append(Pokemon("Onix", 5, "Rock", 100, 95))
    Pokedex.append(Pokemon("Soporifik", 5, "Psychic", 100, 96))
    Pokedex.append(Pokemon("Hypnomade", 5, "Psychic", 100, 97))
    Pokedex.append(Pokemon("Krabby", 5, "Water", 100, 98))
    Pokedex.append(Pokemon("Krabboss", 5, "Water", 100, 99))
    Pokedex.append(Pokemon("Voltorbe", 5, "Electric", 100, 100))
    Pokedex.append(Pokemon("Électrode", 5, "Electric", 100, 101))
    Pokedex.append(Pokemon("Nœunœuf", 5, "Electric", 100, 102))
    Pokedex.append(Pokemon("Noadkoko", 5, "Electric", 100, 103))
    Pokedex.append(Pokemon("Osselait", 5, "Ground", 100, 104))
    Pokedex.append(Pokemon("Ossatueur", 5, "Ground", 100, 105))
    Pokedex.append(Pokemon("Kicklee", 5, "Fighting", 100, 106))
    Pokedex.append(Pokemon("Tygnon", 5, "Fighting", 100, 107))
    Pokedex.append(Pokemon("Excelangue", 5, "Normal", 100, 108))
    Pokedex.append(Pokemon("Smogo", 5, "Poison", 100, 109))
    Pokedex.append(Pokemon("Smogogo", 5, "Poison", 100, 110))
    Pokedex.append(Pokemon("Rhinocorne", 5, "Ground", 100, 111))
    Pokedex.append(Pokemon("Rhinoféros", 5, "Ground", 100, 112))
    Pokedex.append(Pokemon("Leveinard", 5, "Ground", 100, 113))
    Pokedex.append(Pokemon("Saquedeneu", 5, "Ground", 100, 114))
    Pokedex.append(Pokemon("Kangourex", 5, "Normal", 100, 115))
    Pokedex.append(Pokemon("Hypotrempe", 5, "Water", 100, 116))
    Pokedex.append(Pokemon("Hypocéan", 5, "Water", 100, 117))
    Pokedex.append(Pokemon("Poissirène", 5, "Water", 100, 118))
    Pokedex.append(Pokemon("Poissoroy", 5, "Water", 100, 119))
    Pokedex.append(Pokemon("Stari", 5, "Water", 100, 120))
    Pokedex.append(Pokemon("Staross", 5, "Water", 100, 121))
    Pokedex.append(Pokemon("M. Mime", 5, "Psychic", 100, 122))
    Pokedex.append(Pokemon("Insécateur", 5, "Bug", 100, 123))
    Pokedex.append(Pokemon("Lippoutou", 5, "Normal", 100, 124))
    Pokedex.append(Pokemon("Élektek", 5, "Electric", 100, 125))
    Pokedex.append(Pokemon("Magmar", 5, "Fire", 100, 126))
    Pokedex.append(Pokemon("Scarabrute", 5, "Bug", 100, 127))
    Pokedex.append(Pokemon("Tauros", 5, "Normal", 100, 128))
    Pokedex.append(Pokemon("Magicarpe", 5, "Water", 100, 129))
    Pokedex.append(Pokemon("Léviator", 5, "Water", 100, 130))
    Pokedex.append(Pokemon("Lokhlass", 5, "Water", 100, 131))
    Pokedex.append(Pokemon("Métamorph", 5, "Normal", 100, 132))
    Pokedex.append(Pokemon("Évoli", 5, "Normal", 100, 133))
    Pokedex.append(Pokemon("Aquali", 5, "Water", 100, 134))
    Pokedex.append(Pokemon("Voltali", 5, "Electric", 100, 135))
    Pokedex.append(Pokemon("Pyroli", 5, "Fire", 100, 136))
    Pokedex.append(Pokemon("Porygon", 5, "Normal", 100, 137))
    Pokedex.append(Pokemon("Amonita", 5, "Rock", 100, 138))
    Pokedex.append(Pokemon("Amonistar", 5, "Rock", 100, 139))
    Pokedex.append(Pokemon("Kabuto", 5, "Rock", 100, 140))
    Pokedex.append(Pokemon("Kabutops", 5, "Rock", 100, 141))
    Pokedex.append(Pokemon("Ptéra", 5, "Rock", 100, 142))
    Pokedex.append(Pokemon("Ronflex", 5, "Normal", 100, 143))
    Pokedex.append(Pokemon("Artikodin", 5, "Ice", 100, 144))
    Pokedex.append(Pokemon("Électhor", 5, "Electric", 100, 145))
    Pokedex.append(Pokemon("Sulfura", 5, "Fire", 100, 146))
    Pokedex.append(Pokemon("Minidraco", 5, "Dragon", 100, 147))
    Pokedex.append(Pokemon("Draco", 5, "Dragon", 100, 148))
    Pokedex.append(Pokemon("Dracolosse", 5, "Dragon", 100, 149))
    Pokedex.append(Pokemon("Mewtwo", 5, "Psychic", 100, 150))
    Pokedex.append(Pokemon("Mew", 5, "Psychic", 100, 151))



#Affichage Pokedex
def PokedexDisplay():
    print("Pokedex")
    for pokemon in Pokedex:
        print(pokemon.number,".", pokemon.name, pokemon.type)


#Menu init
def Menu():
    print("Menu")
    print("1 - Pokedex")
    print("2 - Exit")
    choice = input("Choice : ")
    if choice == "1":
        PokedexDisplay()
    elif choice == "2":
        exit()



initGame()

