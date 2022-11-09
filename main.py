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

    print("Welcome to the world of Pokemon !")
    sexe = input("What is your sexe ? (M/F) : ")
    
    name = input("What is your name ?")
    print("Nice to meet you", name )
    print("It's the time for chose your starter")
    choise = input("1.Bulbizare / 2.Salamèche / 3.Carapuce")
    if choise == "1" :
        Starter = Pokedex[1]
        print("Vous avez choisis", Starter.name)
    if choise == "2":
        Starter = Pokedex[4]
        print("Vous avez choisis", Starter.name)
    if choise == "3":
        Starter = Pokedex[7]
        print("Vous avez choisis", Starter.name)
    else :
        print("Veuillez choisir un Pokemon")
    PositionX = 5
    PositionY = 5
    Player = Dresseur(name, sexe, Starter, PositionX, PositionY)
    Player.TeamStarer(Starter)
    Player.TeamAdd(Pokedex[2])



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
    def __init__(self, name, sexe, Pokemon, PositionX, PositionY, ID = 1):
        self.name = name
        self.sexe = sexe
        self.Pokemon = {}
        self.PositionX = PositionX
        self.PositionY = PositionY
        self.ID = ID

    def TeamStarer(self, Pokemon):
        null = Pokedex[0]
        self.Pokemon = {
        'Pokemon1' : Pokemon,
        'Pokemon2' : null,
        'Pokemon3' : null,
        'Pokemon4' : null,
        'Pokemon5' : null,
        'Pokemon6' : null}

        
    def TeamAdd(self, Pokemon):
        if self.Pokemon["Pokemon2"].name == "None":
            self.Pokemon["Pokemon2"] = Pokemon
        elif self.Pokemon["Pokemon3"].name == "None":
            self.Pokemon["Pokemon3"] = Pokemon
        elif self.Pokemon["Pokemon4"].name == "None":
            self.Pokemon["Pokemon4"] = Pokemon
        elif self.Pokemon["Pokemon5"].name == "None":
            self.Pokemon["Pokemon5"] = Pokemon
        elif self.Pokemon["Pokemon6"].name == "None":
            self.Pokemon["Pokemon6"] = Pokemon
        else:
            print("Votre equipe est pleine")



    def TeamPokemon(self, Player):
        print("Pokemon1:", self.Pokemon["Pokemon1"].name)
        print("Pokemon2:", self.Pokemon["Pokemon2"].name)
        print("Pokemon3:", self.Pokemon["Pokemon3"].name)
        print("Pokemon4:", self.Pokemon["Pokemon4"].name)
        print("Pokemon5:", self.Pokemon["Pokemon5"].name)
        print("Pokemon6:", self.Pokemon["Pokemon6"].name)



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



    def PokemonDisplay(self, idnum):
        while True:
            if idnum == 1:
                Pokemon1 = self.Pokemon["Pokemon1"]

                Status = PokemonStatus(Pokemon1)
                if Status == "Alive":
                    return Pokemon1
                else: 
                    idnum = idnum + 1

            elif idnum == 2 :
                Pokemon2 = self.Pokemon["Pokemon2"]
                Status = PokemonStatus(Pokemon2)
                if Status == "Alive" and Pokemon2.name != "None":
                    return Pokemon2
                else: 
                    idnum = idnum + 1
                
            elif idnum == 3:
                Pokemon3 = self.Pokemon["Pokemon3"]
                Status = PokemonStatus(Pokemon3)
                if Status == "Alive" and Pokemon2.name != "None":
                    return Pokemon3
                else: 
                    idnum = idnum + 1

            elif idnum == 4:
                Pokemon4 = self.Pokemon["Pokemon4"]
                Status = PokemonStatus(Pokemon4)
                if Status == "Alive" and Pokemon2.name != "None":
                    return Pokemon4
                else: 
                    idnum = idnum + 1



            elif idnum == 5:
                Pokemon5 = self.Pokemon["Pokemon5"]
                Status = PokemonStatus(Pokemon5)
                if Status == "Alive" and Pokemon2.name != "None":
                    return Pokemon5
                else: 
                    idnum = idnum + 1


            elif idnum == 6:
                Pokemon6 = self.Pokemon["Pokemon6"]
                Status = PokemonStatus(Pokemon6)
                if Status == "Alive" and Pokemon2.name != "None":
                    return Pokemon6
                else: 
                    idnum = idnum + 1
            elif idnum == 7:
                print("You have no more Pokemon")
                exit()
                break




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

        
def PokemonStatus(Pokemon):
    if Pokemon.life <= 0:
        return "KO"
    elif Pokemon.life > 0:
        return "Alive"



class Fight:
    def __init__(self, name , Openent):
        self.name = name
        self.Openent = Openent

    def Setup(self, Player):

        PokemonAlly = Player.PokemonDisplay(Player.ID)
        PokemonEnemy = self.Openent
        

        print(self.Openent.name,"Life:", "#" * self.Openent.life)
        print("Your :", PokemonAlly.name , "Life:", "#" * PokemonAlly.life)
        print("Fight")
        print("1 - Attack")
        print("2 - Item")
        print("3 - Switch")
        print("4 - Run")

        choice = input("Choice : ")
        if choice == "1":
            print("Attack")
            print("1- ", PokemonAlly.MovesDisplay(1))
            print("2- ", PokemonAlly.MovesDisplay(2))
            choice = input("Choice : ")
            choice = int(choice)
    

            if PokemonAlly.speed >= self.Openent.speed:

                print(PokemonAlly.name, "use", PokemonAlly.MovesDisplay(choice), "on" ,self.Openent.name) #joueur qui attaque en premier
                CheckEfficacity = TypeEffectiveness(self.Openent.MoveType(choice) , PokemonAlly.type) #changer choice par rando

                life  = (self.Openent.life - PokemonAlly.MoveDamage(choice)) /  CheckEfficacity
                life = int(life)
                PokemonAlly.life = life
                


                print(self.Openent.name, "use", self.Openent.MovesDisplay(choice), "on" ,PokemonAlly.name) #Adversaire qui attaque
                CheckEfficacity = TypeEffectiveness(PokemonAlly.MoveType(choice), self.Openent.type)

                life  = (PokemonAlly.life - self.Openent.MoveDamage(choice)) / CheckEfficacity
                life = int(life)
                PokemonAlly.life = life



            if PokemonAlly.speed < self.Openent.speed:
                print(self.Openent.name, "use", self.Openent.MovesDisplay(choice), "on" ,PokemonAlly.name) #Adversaire qui attaque
                CheckEfficacity = TypeEffectiveness(self.Openent.type , PokemonAlly.type)

                PlayerLife = (PokemonAlly.life - self.Openent.MoveDamage(choice)) / CheckEfficacity
                PokemonAlly.life = int(PlayerLife)



   
                print(PokemonAlly.name, "use", PokemonAlly.MovesDisplay(choice), "on" ,self.Openent.name) #joueur qui attaque en deuxieme
                CheckEfficacity = TypeEffectiveness(PokemonAlly.MoveType(choice),self.Openent.type ) #changer choice par rando

                lifeEnn = (self.Openent.life - PokemonAlly.MoveDamage(choice)) / CheckEfficacity
                lifeEnn = int(lifeEnn)
                self.Openent.life = lifeEnn


            if self.Openent.life <= 0:
                print("You win")
                MovePlayer(Player)
            if PokemonAlly.life <= 0:
                print("You lose")
                MovePlayer(Player)
            else:
                self.Setup(Player)
            

        elif choice == "2":
            print("Item")

        elif choice == "3":
            print("Switch")
            Player.TeamPokemon(Player)
            choice = input("Choice : ")
            choice = int(choice)
            Player.ID = choice
            PokemonAlly = Player.PokemonDisplay(Player.ID)
            self.Setup(Player)

        elif choice == "4":

            print("Run")
            MovePlayer(Player)
        else:
            print("Error")
            self.Setup()




def TypeEffectiveness(Type1, Type2):
    if Type1 == "Fire" and Type2 == "Water": #attaque de type Feu sur pokemon eau
        print("It's not very effective")
        return 1
    elif Type1 == "Fire" and Type2 == "Grass":
        print("It's super effective")
        return 3
    elif Type1 == "Fire" and Type2 == "Fire":
        print("It's not very effective")
        return 1
    elif Type1 == "Water" and Type2 == "Fire":
        print("It's super effective")
        return 3
    elif Type1 == "Water" and Type2 == "Grass":
        print("It's not very effective")
        return 1
    elif Type1 == "Water" and Type2 == "Water":
        print("It's not very effective")
        return 1
    elif Type1 == "Grass" and Type2 == "Fire":
        print("It's not very effective")
        return 1
    elif Type1 == "Grass" and Type2 == "Water":
        print("It's super effective")
        return 3
    elif Type1 == "Grass" and Type2 == "Grass":
        print("It's not very effective")
        return 1
    else:
        return 2

initGame()

