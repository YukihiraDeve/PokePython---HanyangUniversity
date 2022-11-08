#Projet Game Pokemon in Python. No use Graphic librairys




#Variable Globale

from turtle import speed
from typing import Set
import json


team = 0
Pokedex = []
PokemonTeam = []
MAX_POKEMON_TEAM = 6
MIN_POKEMON_TEAM = 1
global Player




def initGame():
    InitPokedex()
    Player = main()
    MovePlayer(Player)




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
    #    print("Vous avez choisis", Starter.name)
   #     print("Attaque " , Starter.attacks)
    if choise == "2":
        Starter = Pokedex[4]
    if choise == "3":
        Starter = Pokedex[7]
    PositionX = 5
    PositionY = 5
    Player = Dresseur(name, sexe, Starter, Pokemon2, Pokemon3, Pokemon4, Pokemon5, Pokemon6, PositionX, PositionY)

    return Player


#Pokemon class
class Pokemon():
    def __init__(self, name, level, type, life, id, attack, defense, speed, attacks):
        self.name = name
        self.level = level
        self.type = type
        self.life = life
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.id = id
        self.attacks = {}
    
    def Moves(self ,moveID1 , move_1,damage_1,moveID2,move_2,damage_2, type1, type2): 
        self.attacks[moveID1] = move_1, damage_1, type1
        self.attacks[moveID2] = move_2, damage_2, type2

    def MovesDisplay(self, idnum):
        if idnum == 1:
            return self.attacks["name1"]
        elif idnum == 2:
            return self.attacks["name2"]

    def MoveDamage(self, idnum):
        if idnum == 1:
            return self.attacks["damage1"]
        elif idnum == 2:
            return self.attacks["damage2"]
    
    def MoveType(self, idnum):
        if idnum == 1:
            return self.attacks["type1"]
        elif idnum == 2:
            return self.attacks["type2"]

    def Moves(self, moveID1 , move_1, damage_1, moveID2, move_2, damage_2, type1, type2):
        self.attacks = {
         'id1' : moveID1,
         'name1': move_1,
         'damage1': damage_1,
         'type1': type1,
         'id2' : moveID2,
         'name2': move_2,
         'damage2': damage_2,
         'type2': type2}
        
        y = json.dumps(self.attacks)
        y = json.loads(y)
       #print(y["name2"])


#Init Pokemon

def InitPokedex():
    Any = Pokemon("None", 0, "None", 0, 0, 0, 0, 0, 0)
    Bulbizare = Pokemon("Bulbizarre", 5, "Grass", 100, 1, 13, 9, 5, {})
    Bulbizare.Moves(1, "Tackle", 10, 2, "Vine Whip", 20, "Normal", "Grass")
    Herbizare = Pokemon("Herbizarre", 5, "Feu", 100, 2, 14, 12, 23, {})
    Herbizare.Moves(1, "Tackle", 10, 2, "Vine Whip", 20, "Normal", "Grass")
    Florizare = Pokemon("Florizarre", 5, "Eau", 100, 3, 12, 13, 23, {})
    Florizare.Moves(1, "Tackle", 10, 2, "Vine Whip", 20, "Normal", "Grass")
    Salameche = Pokemon("Salameche", 5, "Fire", 100, 4, 14, 13, 12, {})
    Salameche.Moves(1, "Scratch", 10, 2, "Ember", 20, "Normal", "Fire")
    Reptincel = Pokemon("Reptincel", 5, "Fire", 100, 5, 15, 18, 13, {})
    Reptincel.Moves(1, "Scratch", 10, 2, "Ember", 20, "Normal", "Fire")
    Dracaufeu = Pokemon("Dracaufeu", 5, "Fire", 100, 6, 34, 21, 12, {})
    Dracaufeu.Moves(1, "Scratch", 10, 2, "Ember", 20, "Normal", "Fire")
    Carapuce  = Pokemon("Carapuce", 5, "Water", 100, 7, 10, 9, 8, {})
    Carapuce.Moves(1, "Tackle", 10, 2, "Water Gun", 20, "Normal", "Water")
    Carabaffe = Pokemon("Carabaffe", 5, "Water", 100, 8, 20, 15, 16, {})
    Carabaffe.Moves(1, "Tackle", 10, 2, "Water Gun", 20, "Normal", "Water")
    Tortank   = Pokemon("Tortank", 5, "Water", 100, 9, 50, 30, 15, {})
    Tortank.Moves(1, "Tackle", 10, 2, "Water Gun", 20, "Normal", "Water")

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
    def __init__(self, name, sexe, Pokemon1, Pokemon2, Pokemon3, Pokemon4, Pokemon5, Pokemon6, PositionX, PositionY):
        self.name = name
        self.sexe = sexe
        self.Pokemon1 = Pokemon1
        self.Pokemon2 = Pokemon2
        self.Pokemon3 = Pokemon3
        self.Pokemon4 = Pokemon4
        self.Pokemon5 = Pokemon5
        self.Pokemon6 = Pokemon6
        self.PositionX = PositionX
        self.PositionY = PositionY


    def TeamPokemon(self, Player):
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
        Menu(Player)

    def PlayerInfo(self, Player):
        print("Name :", self.name
                , "Sexe :", self.sexe
                , "Pokemon1 :", self.Pokemon1.name
                , "Pokemon2 :", self.Pokemon2.name
                , "Pokemon3 :", self.Pokemon3.name
                , "Pokemon4 :", self.Pokemon4.name
                , "Pokemon5 :", self.Pokemon5.name
                , "Pokemon6 :", self.Pokemon6.name)
        Menu(Player)




#Affichage Pokedex
def PokedexDisplay(Player):
    print("Pokedex")
    for pokemon in Pokedex:
        print(pokemon.id,".", pokemon.name, pokemon.type)
    Menu(Player)


#Menu init
def Menu(Player):
    
    print("Menu")
    print("1 - Pokedex")
    print("2 - Team")
    print("3 - Info Player")
    print("4 - Exit")
    choice = input("Choice : ")
    if choice == "1":
        PokedexDisplay(Player)
    elif choice == "2":
        Player.TeamPokemon(Player)
    elif choice == "3":
        Player.PlayerInfo(Player)
    elif choice == "4":
        MovePlayer(Player)


def MovePlayer(Player):
    print("Move")
    print("1 - Z")
    print("2 - S")
    print("3 - Q")
    print("4 - D")
    print("5 - Menu")
    choice = input("Choice : ")
    if choice == "Z":
        print("North")
        Player.PositionY = Player.PositionY + 1
        print(Player.PositionY)
        MapPose(Player)
    elif choice == "S":
        print("South")
        Player.PositionY = Player.PositionY - 1
        MapPose(Player)
    elif choice == "Q":
        print("West")
        Player.PositionX = Player.PositionX - 1
        MapPose(Player)
    elif choice == "D":
        print("East")
        Player.PositionX = Player.PositionX + 1
        MapPose(Player)
    elif choice == "5":
        Menu(Player)





def MapPose(Player):
    print("Map")
    print("X", Player.PositionX, "Y", Player.PositionY)
    if Player.PositionX % 5 == 1 :
        print("=----- DUEL -----=")
        Kid = Fight("Kid", Pokedex[4])
        Kid.Setup(Player)

    else : 
        MovePlayer(Player)



class Fight:
    def __init__(self, name , Openent):
        self.name = name
        self.Openent = Openent

    def Setup(self, Player):
        i = 0
        print(self.name, "want to fight with", self.Openent.name)
        print(self.Openent.name,"Life:", "#" * self.Openent.life)
        print("Your :", Player.Pokemon1.name, "Life:", "#" * Player.Pokemon1.life)
        print("Fight")
        print("1 - Attack")
        print("2 - Item")
        print("3 - Run")
        choice = input("Choice : ")
        if choice == "1":
            print("Attack")
            print("1- ", Player.Pokemon1.MovesDisplay(1))
            print("2- ", Player.Pokemon1.MovesDisplay(2))
            choice = input("Choice : ")
            choice = int(choice)
    

            if Player.Pokemon1.speed > self.Openent.speed:

                print(Player.Pokemon1.name, "use", Player.Pokemon1.MovesDisplay(choice), "on" ,self.Openent.name)
                CheckEfficacity = TypeEffectiveness(self.Openent.MoveType(choice) , Player.Pokemon1.type) #changer choice par rando

                life  = (self.Openent.life - Player.Pokemon1.MoveDamage(choice)) *  CheckEfficacity
                life = int(life)
                Player.Pokemon1.life = life
                


                print(self.Openent.name, "use", self.Openent.MovesDisplay(choice), "on" ,Player.Pokemon1.name)
                CheckEfficacity = TypeEffectiveness(Player.Pokemon1.MoveType(choice), self.Openent.type)

                life  = (Player.Pokemon1.life - self.Openent.MoveDamage(choice)) * CheckEfficacity
                life = int(life)
                Player.Pokemon1.life = life



            if Player.Pokemon1.speed < self.Openent.speed:
                print(self.Openent.name, "use", self.Openent.MovesDisplay(choice), "on" ,Player.Pokemon1.name)
                CheckEfficacity = TypeEffectiveness(self.Openent.type , Player.Pokemon1.type)

                life  = (Player.Pokemon1.life - self.Openent.MoveDamage(choice)) *  CheckEfficacity
                life = int(life)
                Player.Pokemon1.life = life

   
                print(Player.Pokemon1.name, "use", Player.Pokemon1.MovesDisplay(choice), "on" ,self.Openent.name)
                CheckEfficacity = TypeEffectiveness(Player.Pokemon1.MoveType(choice),self.Openent.type ) #changer choice par rando

                life = (self.Openent.life - Player.Pokemon1.MoveDamage(choice)) * CheckEfficacity
                life = int(life)
                self.Openent.life = life


            if self.Openent.life <= 0:
                print("You win")
                MovePlayer(Player)
            else:
                self.Setup(Player)
            

        elif choice == "2":
            print("Item")
        elif choice == "3":

            print("Run")
        else:
            print("Error")
            self.Setup()




def TypeEffectiveness(Type1, Type2):
    if Type1 == "Fire" and Type2 == "Water": #attaque de type Feu sur pokemon eau
        print("It's not very effective")
        return 0.5
    elif Type1 == "Fire" and Type2 == "Grass":
        print("It's super effective")
        return 2
    elif Type1 == "Fire" and Type2 == "Fire":
        print("It's not very effective")
        return 1
    elif Type1 == "Water" and Type2 == "Fire":
        print("It's super effective")
        return 2
    elif Type1 == "Water" and Type2 == "Grass":
        print("It's not very effective")
        return 0.5
    elif Type1 == "Water" and Type2 == "Water":
        print("It's not very effective")
        return 1
    elif Type1 == "Grass" and Type2 == "Fire":
        print("It's not very effective")
        return 0.5
    elif Type1 == "Grass" and Type2 == "Water":
        print("It's super effective")
        return 2
    elif Type1 == "Grass" and Type2 == "Grass":
        print("It's not very effective")
        return 1
    else:
        return 1

initGame()

