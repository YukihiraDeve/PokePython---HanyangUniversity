#Projet Game Pokemon in Python. No use Graphic librairys




#Variable Globale

from turtle import speed
from typing import Set
import json
import random


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

    BagPack = Bag(0,0,0)
    BagPack.AddPokeball(5)

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

    Player = Dresseur(name, sexe, Starter, PositionX, PositionY , BagPack)
    
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
    Herbizare = Pokemon("Herbizarre", 5, "Grass", 100, 2, 14, 12, 5, {})
    Herbizare.Moves(1, "Tackle", 10, 2, "Vine Whip", 20, "Normal", "Grass")
    Florizare = Pokemon("Florizarre", 5, "Grass", 100, 3, 12, 13, 23, {})
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
    #other pokemon
    Caterpie = Pokemon("Caterpie", 5, "Bug", 100, 10, 10, 10, 10, {})
    Caterpie.Moves(1, "Tackle", 10, 2, "Bug Bite", 20, "Normal", "Bug")
    Metapod = Pokemon("Metapod", 5, "Bug", 100, 11, 10, 10, 10, {})
    Metapod.Moves(1, "Tackle", 10, 2, "Bug Bite", 20, "Normal", "Bug")
    Butterfree = Pokemon("Butterfree", 5, "Bug", 100, 12, 10, 10, 10, {})
    Butterfree.Moves(1, "Tackle", 10, 2, "Bug Bite", 20, "Normal", "Bug")
    Weedle = Pokemon("Weedle", 5, "Bug", 100, 13, 10, 10, 10, {})
    Weedle.Moves(1, "Tackle", 10, 2, "Bug Bite", 20, "Normal", "Bug")
    Kakuna = Pokemon("Kakuna", 5, "Bug", 100, 14, 10, 10, 10, {})
    Kakuna.Moves(1, "Tackle", 10, 2, "Bug Bite", 20, "Normal", "Bug")
    Beedrill = Pokemon("Beedrill", 5, "Bug", 100, 15, 10, 10, 10, {})
    Beedrill.Moves(1, "Tackle", 10, 2, "Bug Bite", 20, "Normal", "Bug")
    Pidgey = Pokemon("Pidgey", 5, "Flying", 100, 16, 10, 10, 10, {})
    Pidgey.Moves(1, "Tackle", 10, 2, "Gust", 20, "Normal", "Flying")
    Pidgeotto = Pokemon("Pidgeotto", 5, "Flying", 100, 17, 10, 10, 10, {})
    Pidgeotto.Moves(1, "Tackle", 10, 2, "Gust", 20, "Normal", "Flying")
    Pidgeot = Pokemon("Pidgeot", 5, "Flying", 100, 18, 10, 10, 10, {})
    Pidgeot.Moves(1, "Tackle", 10, 2, "Gust", 20, "Normal", "Flying")
    Rattata = Pokemon("Rattata", 5, "Normal", 100, 19, 10, 10, 10, {})
    Rattata.Moves(1, "Tackle", 10, 2, "Bite", 20, "Normal", "Dark")
    Raticate = Pokemon("Raticate", 5, "Normal", 100, 20, 10, 10, 10, {})
    Raticate.Moves(1, "Tackle", 10, 2, "Bite", 20, "Normal", "Dark")
    Spearow = Pokemon("Spearow", 5, "Flying", 100, 21, 10, 10, 10, {})
    Spearow.Moves(1, "Tackle", 10, 2, "Peck", 20, "Normal", "Flying")
    Fearow = Pokemon("Fearow", 5, "Flying", 100, 22, 10, 10, 10, {})
    Fearow.Moves(1, "Tackle", 10, 2, "Peck", 20, "Normal", "Flying")
    Ekans = Pokemon("Ekans", 5, "Poison", 100, 23, 10, 10, 10, {})
    Ekans.Moves(1, "Tackle", 10, 2, "Poison Sting", 20, "Normal", "Poison")
    Arbok = Pokemon("Arbok", 5, "Poison", 100, 24, 10, 10, 10, {})
    Arbok.Moves(1, "Tackle", 10, 2, "Poison Sting", 20, "Normal", "Poison")
    Pikachu = Pokemon("Pikachu", 5, "Electric", 100, 25, 10, 10, 10, {})
    Pikachu.Moves(1, "Tackle", 10, 2, "Thunder Shock", 20, "Normal", "Electric")
    Raichu = Pokemon("Raichu", 5, "Electric", 100, 26, 10, 10, 10, {})
    Raichu.Moves(1, "Tackle", 10, 2, "Thunder Shock", 20, "Normal", "Electric")
    Sandshrew = Pokemon("Sandshrew", 5, "Ground", 100, 27, 10, 10, 10, {})
    Sandshrew.Moves(1, "Tackle", 10, 2, "Scratch", 20, "Normal", "Normal")
    Sandslash = Pokemon("Sandslash", 5, "Ground", 100, 28, 10, 10, 10, {})
    Sandslash.Moves(1, "Tackle", 10, 2, "Scratch", 20, "Normal", "Normal")
    Nidoran = Pokemon("Nidoran", 5, "Poison", 100, 29, 10, 10, 10, {})
    Nidoran.Moves(1, "Tackle", 10, 2, "Poison Sting", 20, "Normal", "Poison")
    Nidorina = Pokemon("Nidorina", 5, "Poison", 100, 30, 10, 10, 10, {})
    Nidorina.Moves(1, "Tackle", 10, 2, "Poison Sting", 20, "Normal", "Poison")
    Nidoqueen = Pokemon("Nidoqueen", 5, "Poison", 100, 31, 10, 10, 10, {})
    Nidoqueen.Moves(1, "Tackle", 10, 2, "Poison Sting", 20, "Normal", "Poison")
    Nidoran = Pokemon("Nidoran", 5, "Poison", 100, 32, 10, 10, 10, {})
    Nidoran.Moves(1, "Tackle", 10, 2, "Poison Sting", 20, "Normal", "Poison")
    Nidorino = Pokemon("Nidorino", 5, "Poison", 100, 33, 10, 10, 10, {})
    Nidorino.Moves(1, "Tackle", 10, 2, "Poison Sting", 20, "Normal", "Poison")
    Nidoking = Pokemon("Nidoking", 5, "Poison", 100, 34, 10, 10, 10, {})
    Nidoking.Moves(1, "Tackle", 10, 2, "Poison Sting", 20, "Normal", "Poison")
    Clefairy = Pokemon("Clefairy", 5, "Fairy", 100, 35, 10, 10, 10, {})
    Clefairy.Moves(1, "Pound", 10, 2, "Double Slap", 20, "Normal", "Normal")
    Clefable = Pokemon("Clefable", 5, "Fairy", 100, 36, 10, 10, 10, {})
    Clefable.Moves(1, "Pound", 10, 2, "Double Slap", 20, "Normal", "Normal")
    Vulpix = Pokemon("Vulpix", 5, "Fire", 100, 37, 10, 10, 10, {})
    Vulpix.Moves(1, "Ember", 10, 2, "Quick Attack", 20, "Fire", "Normal")
    Ninetales = Pokemon("Ninetales", 5, "Fire", 100, 38, 10, 10, 10, {})
    Ninetales.Moves(1, "Ember", 10, 2, "Quick Attack", 20, "Fire", "Normal")
    Jigglypuff = Pokemon("Jigglypuff", 5, "Normal", 100, 39, 10, 10, 10, {})
    Jigglypuff.Moves(1, "Pound", 10, 2, "Double Slap", 20, "Normal", "Normal")
    Wigglytuff = Pokemon("Wigglytuff", 5, "Normal", 100, 40, 10, 10, 10, {})
    Wigglytuff.Moves(1, "Pound", 10, 2, "Double Slap", 20, "Normal", "Normal")
    Zubat = Pokemon("Zubat", 5, "Poison", 100, 41, 10, 10, 10, {})
    Zubat.Moves(1, "Tackle", 10, 2, "Bite", 20, "Normal", "Dark")
    Golbat = Pokemon("Golbat", 5, "Poison", 100, 42, 10, 10, 10, {})
    Golbat.Moves(1, "Tackle", 10, 2, "Bite", 20, "Normal", "Dark")
    Oddish = Pokemon("Oddish", 5, "Grass", 100, 43, 10, 10, 10, {})
    Oddish.Moves(1, "Absorb", 10, 2, "Acid", 20, "Grass", "Poison")
    Gloom = Pokemon("Gloom", 5, "Grass", 100, 44, 10, 10, 10, {})
    Gloom.Moves(1, "Absorb", 10, 2, "Acid", 20, "Grass", "Poison")
    Vileplume = Pokemon("Vileplume", 5, "Grass", 100, 45, 10, 10, 10, {})
    Vileplume.Moves(1, "Absorb", 10, 2, "Acid", 20, "Grass", "Poison")
    Paras = Pokemon("Paras", 5, "Bug", 100, 46, 10, 10, 10, {})
    Paras.Moves(1, "Scratch", 10, 2, "Stun Spore", 20, "Normal", "Grass")
    Parasect = Pokemon("Parasect", 5, "Bug", 100, 47, 10, 10, 10, {})
    Parasect.Moves(1, "Scratch", 10, 2, "Stun Spore", 20, "Normal", "Grass")
    Venonat = Pokemon("Venonat", 5, "Bug", 100, 48, 10, 10, 10, {})
    Venonat.Moves(1, "Tackle", 10, 2, "Poison Powder", 20, "Normal", "Poison")
    Venomoth = Pokemon("Venomoth", 5, "Bug", 100, 49, 10, 10, 10, {})
    Venomoth.Moves(1, "Tackle", 10, 2, "Poison Powder", 20, "Normal", "Poison")
    Diglett = Pokemon("Diglett", 5, "Ground", 100, 50, 10, 10, 10, {})
    Diglett.Moves(1, "Scratch", 10, 2, "Dig", 20, "Normal", "Ground")
    Dugtrio = Pokemon("Dugtrio", 5, "Ground", 100, 51, 10, 10, 10, {})
    Dugtrio.Moves(1, "Scratch", 10, 2, "Dig", 20, "Normal", "Ground")
    Meowth = Pokemon("Meowth", 5, "Normal", 100, 52, 10, 10, 10, {})
    Meowth.Moves(1, "Scratch", 10, 2, "Bite", 20, "Normal", "Dark")
    Persian = Pokemon("Persian", 5, "Normal", 100, 53, 10, 10, 10, {})
    Persian.Moves(1, "Scratch", 10, 2, "Bite", 20, "Normal", "Dark")
    Psyduck = Pokemon("Psyduck", 5, "Water", 100, 54, 10, 10, 10, {})
    Psyduck.Moves(1, "Scratch", 10, 2, "Water Gun", 20, "Normal", "Water")
    Golduck = Pokemon("Golduck", 5, "Water", 100, 55, 10, 10, 10, {})
    Golduck.Moves(1, "Scratch", 10, 2, "Water Gun", 20, "Normal", "Water")
    Mankey = Pokemon("Mankey", 5, "Fighting", 100, 56, 10, 10, 10, {})
    Mankey.Moves(1, "Scratch", 10, 2, "Karate Chop", 20, "Normal", "Fighting")
    Primeape = Pokemon("Primeape", 5, "Fighting", 100, 57, 10, 10, 10, {})
    Primeape.Moves(1, "Scratch", 10, 2, "Karate Chop", 20, "Normal", "Fighting")
    Growlithe = Pokemon("Growlithe", 5, "Fire", 100, 58, 10, 10, 10, {})
    Growlithe.Moves(1, "Ember", 10, 2, "Bite", 20, "Fire", "Dark")
    Arcanine = Pokemon("Arcanine", 5, "Fire", 100, 59, 10, 10, 10, {})
    Arcanine.Moves(1, "Ember", 10, 2, "Bite", 20, "Fire", "Dark")
    Poliwag = Pokemon("Poliwag", 5, "Water", 100, 60, 10, 10, 10, {})
    Poliwag.Moves(1, "Bubble", 10, 2, "Water Gun", 20, "Water", "Water")
    Poliwhirl = Pokemon("Poliwhirl", 5, "Water", 100, 61, 10, 10, 10, {})
    Poliwhirl.Moves(1, "Bubble", 10, 2, "Water Gun", 20, "Water", "Water")
    Poliwrath = Pokemon("Poliwrath", 5, "Water", 100, 62, 10, 10, 10, {})
    Poliwrath.Moves(1, "Bubble", 10, 2, "Water Gun", 20, "Water", "Water")
    Abra = Pokemon("Abra", 5, "Psychic", 100, 63, 10, 10, 10, {})
    Abra.Moves(1, "Confusion", 10, 2, "Psybeam", 20, "Psychic", "Psychic")
    Kadabra = Pokemon("Kadabra", 5, "Psychic", 100, 64, 10, 10, 10, {})
    Kadabra.Moves(1, "Confusion", 10, 2, "Psybeam", 20, "Psychic", "Psychic")
    Alakazam = Pokemon("Alakazam", 5, "Psychic", 100, 65, 10, 10, 10, {})
    Alakazam.Moves(1, "Confusion", 10, 2, "Psybeam", 20, "Psychic", "Psychic")
    Machop = Pokemon("Machop", 5, "Fighting", 100, 66, 10, 10, 10, {})
    Machop.Moves(1, "Karate Chop", 10, 2, "Low Kick", 20, "Fighting", "Fighting")
    Machoke = Pokemon("Machoke", 5, "Fighting", 100, 67, 10, 10, 10, {})
    Machoke.Moves(1, "Karate Chop", 10, 2, "Low Kick", 20, "Fighting", "Fighting")
    Machamp = Pokemon("Machamp", 5, "Fighting", 100, 68, 10, 10, 10, {})
    Machamp.Moves(1, "Karate Chop", 10, 2, "Low Kick", 20, "Fighting", "Fighting")
    Bellsprout = Pokemon("Bellsprout", 5, "Grass", 100, 69, 10, 10, 10, {})
    Bellsprout.Moves(1, "Vine Whip", 10, 2, "Acid", 20, "Grass", "Poison")
    Weepinbell = Pokemon("Weepinbell", 5, "Grass", 100, 70, 10, 10, 10, {})
    Weepinbell.Moves(1, "Vine Whip", 10, 2, "Acid", 20, "Grass", "Poison")
    Victreebel = Pokemon("Victreebel", 5, "Grass", 100, 71, 10, 10, 10, {})
    Victreebel.Moves(1, "Vine Whip", 10, 2, "Acid", 20, "Grass", "Poison")
    Tentacool = Pokemon("Tentacool", 5, "Water", 100, 72, 10, 10, 10, {})
    Tentacool.Moves(1, "Poison Sting", 10, 2, "Water Gun", 20, "Poison", "Water")
    Tentacruel = Pokemon("Tentacruel", 5, "Water", 100, 73, 10, 10, 10, {})
    Tentacruel.Moves(1, "Poison Sting", 10, 2, "Water Gun", 20, "Poison", "Water")
    Geodude = Pokemon("Geodude", 5, "Rock", 100, 74, 10, 10, 10, {})
    Geodude.Moves(1, "Tackle", 10, 2, "Rock Throw", 20, "Normal", "Rock")
    Graveler = Pokemon("Graveler", 5, "Rock", 100, 75, 10, 10, 10, {})
    Graveler.Moves(1, "Tackle", 10, 2, "Rock Throw", 20, "Normal", "Rock")
    Golem = Pokemon("Golem", 5, "Rock", 100, 76, 10, 10, 10, {})
    Golem.Moves(1, "Tackle", 10, 2, "Rock Throw", 20, "Normal", "Rock")
    Ponyta = Pokemon("Ponyta", 5, "Fire", 100, 77, 10, 10, 10, {})
    Ponyta.Moves(1, "Ember", 10, 2, "Fire Spin", 20, "Fire", "Fire")
    Rapidash = Pokemon("Rapidash", 5, "Fire", 100, 78, 10, 10, 10, {})
    Rapidash.Moves(1, "Ember", 10, 2, "Fire Spin", 20, "Fire", "Fire")
    Slowpoke = Pokemon("Slowpoke", 5, "Water", 100, 79, 10, 10, 10, {})
    Slowpoke.Moves(1, "Confusion", 10, 2, "Water Gun", 20, "Psychic", "Water")
    Slowbro = Pokemon("Slowbro", 5, "Water", 100, 80, 10, 10, 10, {})
    Slowbro.Moves(1, "Confusion", 10, 2, "Water Gun", 20, "Psychic", "Water")
    Magnemite = Pokemon("Magnemite", 5, "Electric", 100, 81, 10, 10, 10, {})
    Magnemite.Moves(1, "Thunder Shock", 10, 2, "Thunder Wave", 20, "Electric", "Electric")
    Magneton = Pokemon("Magneton", 5, "Electric", 100, 82, 10, 10, 10, {})
    Magneton.Moves(1, "Thunder Shock", 10, 2, "Thunder Wave", 20, "Electric", "Electric")
    Farfetch = Pokemon("Farfetch'd", 5, "Normal", 100, 83, 10, 10, 10, {})
    Farfetch.Moves(1, "Peck", 10, 2, "Fury Attack", 20, "Flying", "Normal")
    Doduo = Pokemon("Doduo", 5, "Normal", 100, 84, 10, 10, 10, {})
    Doduo.Moves(1, "Peck", 10, 2, "Fury Attack", 20, "Flying", "Normal")
    Dodrio = Pokemon("Dodrio", 5, "Normal", 100, 85, 10, 10, 10, {})
    Dodrio.Moves(1, "Peck", 10, 2, "Fury Attack", 20, "Flying", "Normal")
    Seel = Pokemon("Seel", 5, "Water", 100, 86, 10, 10, 10, {})
    Seel.Moves(1, "Headbutt", 10, 2, "Ice Beam", 20, "Normal", "Ice")
    Dewgong = Pokemon("Dewgong", 5, "Water", 100, 87, 10, 10, 10, {})
    Dewgong.Moves(1, "Headbutt", 10, 2, "Ice Beam", 20, "Normal", "Ice")
    Grimer = Pokemon("Grimer", 5, "Poison", 100, 88, 10, 10, 10, {})
    Grimer.Moves(1, "Pound", 10, 2, "Sludge", 20, "Normal", "Poison")
    Muk = Pokemon("Muk", 5, "Poison", 100, 89, 10, 10, 10, {})
    Muk.Moves(1, "Pound", 10, 2, "Sludge", 20, "Normal", "Poison")
    Shellder = Pokemon("Shellder", 5, "Water", 100, 90, 10, 10, 10, {})
    Shellder.Moves(1, "Tackle", 10, 2, "Ice Beam", 20, "Normal", "Ice")
    Cloyster = Pokemon("Cloyster", 5, "Water", 100, 91, 10, 10, 10, {})
    Cloyster.Moves(1, "Tackle", 10, 2, "Ice Beam", 20, "Normal", "Ice")
    Gastly = Pokemon("Gastly", 5, "Ghost", 100, 92, 10, 10, 10, {})
    Gastly.Moves(1, "Lick", 10, 2, "Night Shade", 20, "Ghost", "Ghost")
    Haunter = Pokemon("Haunter", 5, "Ghost", 100, 93, 10, 10, 10, {})
    Haunter.Moves(1, "Lick", 10, 2, "Night Shade", 20, "Ghost", "Ghost")
    Gengar = Pokemon("Gengar", 5, "Ghost", 100, 94, 10, 10, 10, {})
    Gengar.Moves(1, "Lick", 10, 2, "Night Shade", 20, "Ghost", "Ghost")
    Onix = Pokemon("Onix", 5, "Rock", 100, 95, 10, 10, 10, {})
    Onix.Moves(1, "Tackle", 10, 2, "Rock Throw", 20, "Normal", "Rock")
    Drowzee = Pokemon("Drowzee", 5, "Psychic", 100, 96, 10, 10, 10, {})
    Drowzee.Moves(1, "Pound", 10, 2, "Confusion", 20, "Normal", "Psychic")
    Hypno = Pokemon("Hypno", 5, "Psychic", 100, 97, 10, 10, 10, {})
    Hypno.Moves(1, "Pound", 10, 2, "Confusion", 20, "Normal", "Psychic")
    Krabby = Pokemon("Krabby", 5, "Water", 100, 98, 10, 10, 10, {})
    Krabby.Moves(1, "Bubble", 10, 2, "Vice Grip", 20, "Water", "Normal")
    Kingler = Pokemon("Kingler", 5, "Water", 100, 99, 10, 10, 10, {})
    Kingler.Moves(1, "Bubble", 10, 2, "Vice Grip", 20, "Water", "Normal")
    Voltorb = Pokemon("Voltorb", 5, "Electric", 100, 100, 10, 10, 10, {})
    Voltorb.Moves(1, "Tackle", 10, 2, "Spark", 20, "Normal", "Electric")
    Electrode = Pokemon("Electrode", 5, "Electric", 100, 101, 10, 10, 10, {})
    Electrode.Moves(1, "Tackle", 10, 2, "Spark", 20, "Normal", "Electric")
    Exeggcute = Pokemon("Exeggcute", 5, "Grass", 100, 102, 10, 10, 10, {})
    Exeggcute.Moves(1, "Confusion", 10, 2, "Poison Powder", 20, "Psychic", "Poison")
    Exeggutor = Pokemon("Exeggutor", 5, "Grass", 100, 103, 10, 10, 10, {})
    Exeggutor.Moves(1, "Confusion", 10, 2, "Poison Powder", 20, "Psychic", "Poison")
    Cubone = Pokemon("Cubone", 5, "Ground", 100, 104, 10, 10, 10, {})
    Cubone.Moves(1, "Bone Club", 10, 2, "Growl", 20, "Ground", "Normal")
    Marowak = Pokemon("Marowak", 5, "Ground", 100, 105, 10, 10, 10, {})
    Marowak.Moves(1, "Bone Club", 10, 2, "Growl", 20, "Ground", "Normal")
    Hitmonlee = Pokemon("Hitmonlee", 5, "Fighting", 100, 106, 10, 10, 10, {})
    Hitmonlee.Moves(1, "Mega Kick", 10, 2, "Mega Punch", 20, "Fighting", "Fighting")
    Hitmonchan = Pokemon("Hitmonchan", 5, "Fighting", 100, 107, 10, 10, 10, {})
    Hitmonchan.Moves(1, "Mega Kick", 10, 2, "Mega Punch", 20, "Fighting", "Fighting")
    Lickitung = Pokemon("Lickitung", 5, "Normal", 100, 108, 10, 10, 10, {})
    Lickitung.Moves(1, "Lick", 10, 2, "Wrap", 20, "Ghost", "Normal")
    Koffing = Pokemon("Koffing", 5, "Poison", 100, 109, 10, 10, 10, {})
    Koffing.Moves(1, "Tackle", 10, 2, "Smog", 20, "Normal", "Poison")
    Weezing = Pokemon("Weezing", 5, "Poison", 100, 110, 10, 10, 10, {})
    Weezing.Moves(1, "Tackle", 10, 2, "Smog", 20, "Normal", "Poison")
    Rhyhorn = Pokemon("Rhyhorn", 5, "Ground", 100, 111, 10, 10, 10, {})
    Rhyhorn.Moves(1, "Horn Attack", 10, 2, "Stomp", 20, "Normal", "Ground")
    Rhydon = Pokemon("Rhydon", 5, "Ground", 100, 112, 10, 10, 10, {})
    Rhydon.Moves(1, "Horn Attack", 10, 2, "Stomp", 20, "Normal", "Ground")
    Chansey = Pokemon("Chansey", 5, "Normal", 100, 113, 10, 10, 10, {})
    Chansey.Moves(1, "Pound", 10, 2, "Double Slap", 20, "Normal", "Normal")
    Tangela = Pokemon("Tangela", 5, "Grass", 100, 114, 10, 10, 10, {})
    Tangela.Moves(1, "Constrict", 10, 2, "Absorb", 20, "Normal", "Grass")
    Kangaskhan = Pokemon("Kangaskhan", 5, "Normal", 100, 115, 10, 10, 10, {})
    Kangaskhan.Moves(1, "Bite", 10, 2, "Dizzy Punch", 20, "Dark", "Normal")
    Horsea = Pokemon("Horsea", 5, "Water", 100, 116, 10, 10, 10, {})
    Horsea.Moves(1, "Bubble", 10, 2, "Smokescreen", 20, "Water", "Normal")
    Seadra = Pokemon("Seadra", 5, "Water", 100, 117, 10, 10, 10, {})
    Seadra.Moves(1, "Bubble", 10, 2, "Smokescreen", 20, "Water", "Normal")
    Goldeen = Pokemon("Goldeen", 5, "Water", 100, 118, 10, 10, 10, {})
    Goldeen.Moves(1, "Peck", 10, 2, "Horn Attack", 20, "Flying", "Normal")
    Seaking = Pokemon("Seaking", 5, "Water", 100, 119, 10, 10, 10, {})
    Seaking.Moves(1, "Peck", 10, 2, "Horn Attack", 20, "Flying", "Normal")
    Staryu = Pokemon("Staryu", 5, "Water", 100, 120, 10, 10, 10, {})
    Staryu.Moves(1, "Tackle", 10, 2, "Water Gun", 20, "Normal", "Water")
    Starmie = Pokemon("Starmie", 5, "Water", 100, 121, 10, 10, 10, {})
    Starmie.Moves(1, "Tackle", 10, 2, "Water Gun", 20, "Normal", "Water")
    MrMime = Pokemon("MrMime", 5, "Psychic", 100, 122, 10, 10, 10, {})
    MrMime.Moves(1, "Confusion", 10, 2, "Barrier", 20, "Psychic", "Psychic")
    Scyther = Pokemon("Scyther", 5, "Bug", 100, 123, 10, 10, 10, {})
    Scyther.Moves(1, "Quick Attack", 10, 2, "Leer", 20, "Normal", "Normal")
    Jynx = Pokemon("Jynx", 5, "Ice", 100, 124, 10, 10, 10, {})
    Jynx.Moves(1, "Pound", 10, 2, "Lick", 20, "Normal", "Ghost")
    Electabuzz = Pokemon("Electabuzz", 5, "Electric", 100, 125, 10, 10, 10, {})
    Electabuzz.Moves(1, "Quick Attack", 10, 2, "Thunder Punch", 20, "Normal", "Electric")
    Magmar = Pokemon("Magmar", 5, "Fire", 100, 126, 10, 10, 10, {})
    Magmar.Moves(1, "Ember", 10, 2, "Karate Chop", 20, "Fire", "Fighting")
    Pinsir = Pokemon("Pinsir", 5, "Bug", 100, 127, 10, 10, 10, {})
    Pinsir.Moves(1, "Vice Grip", 10, 2, "Seismic Toss", 20, "Normal", "Fighting")
    Tauros = Pokemon("Tauros", 5, "Normal", 100, 128, 10, 10, 10, {})
    Tauros.Moves(1, "Tackle", 10, 2, "Rage", 20, "Normal", "Normal")
    Magikarp = Pokemon("Magikarp", 5, "Water", 100, 129, 10, 10, 10, {})
    Magikarp.Moves(1, "Splash", 10, 2, "Tackle", 20, "Normal", "Normal")
    Gyarados = Pokemon("Gyarados", 5, "Water", 100, 130, 10, 10, 10, {})
    Gyarados.Moves(1, "Bite", 10, 2, "Hydro Pump", 20, "Dark", "Water")
    Lapras = Pokemon("Lapras", 5, "Water", 100, 131, 10, 10, 10, {})
    Lapras.Moves(1, "Water Gun", 10, 2, "Ice Beam", 20, "Water", "Ice")
    Ditto = Pokemon("Ditto", 5, "Normal", 100, 132, 10, 10, 10, {})
    Ditto.Moves(1, "Transform", 10, 2, "Transform", 20, "Normal", "Normal")
    Eevee = Pokemon("Eevee", 5, "Normal", 100, 133, 10, 10, 10, {})
    Eevee.Moves(1, "Tackle", 10, 2, "Tail Whip", 20, "Normal", "Normal")
    Vaporeon = Pokemon("Vaporeon", 5, "Water", 100, 134, 10, 10, 10, {})
    Vaporeon.Moves(1, "Water Gun", 10, 2, "Aurora Beam", 20, "Water", "Ice")
    Jolteon = Pokemon("Jolteon", 5, "Electric", 100, 135, 10, 10, 10, {})
    Jolteon.Moves(1, "Thunder Shock", 10, 2, "Quick Attack", 20, "Electric", "Normal")
    Flareon = Pokemon("Flareon", 5, "Fire", 100, 136, 10, 10, 10, {})
    Flareon.Moves(1, "Ember", 10, 2, "Quick Attack", 20, "Fire", "Normal")
    Porygon = Pokemon("Porygon", 5, "Normal", 100, 137, 10, 10, 10, {})
    Porygon.Moves(1, "Tackle", 10, 2, "Psybeam", 20, "Normal", "Psychic")
    Omanyte = Pokemon("Omanyte", 5, "Rock", 100, 138, 10, 10, 10, {})
    Omanyte.Moves(1, "Water Gun", 10, 2, "Withdraw", 20, "Water", "Water")
    Omastar = Pokemon("Omastar", 5, "Rock", 100, 139, 10, 10, 10, {})
    Omastar.Moves(1, "Water Gun", 10, 2, "Withdraw", 20, "Water", "Water")
    Kabuto = Pokemon("Kabuto", 5, "Rock", 100, 140, 10, 10, 10, {})
    Kabuto.Moves(1, "Scratch", 10, 2, "Harden", 20, "Normal", "Normal")
    Kabutops = Pokemon("Kabutops", 5, "Rock", 100, 141, 10, 10, 10, {})
    Kabutops.Moves(1, "Scratch", 10, 2, "Harden", 20, "Normal", "Normal")
    Aerodactyl = Pokemon("Aerodactyl", 5, "Rock", 100, 142, 10, 10, 10, {})
    Aerodactyl.Moves(1, "Wing Attack", 10, 2, "Agility", 20, "Flying", "Psychic")
    Snorlax = Pokemon("Snorlax", 5, "Normal", 100, 143, 10, 10, 10, {})
    Snorlax.Moves(1, "Tackle", 10, 2, "Amnesia", 20, "Normal", "Psychic")
    Articuno = Pokemon("Articuno", 5, "Ice", 100, 144, 10, 10, 10, {})
    Articuno.Moves(1, "Gust", 10, 2, "Ice Beam", 20, "Flying", "Ice")
    Zapdos = Pokemon("Zapdos", 5, "Electric", 100, 145, 10, 10, 10, {})
    Zapdos.Moves(1, "Peck", 10, 2, "Thunder", 20, "Flying", "Electric")
    Moltres = Pokemon("Moltres", 5, "Fire", 100, 146, 10, 10, 10, {})
    Moltres.Moves(1, "Wing Attack", 10, 2, "Fire Blast", 20, "Flying", "Fire")
    Dratini = Pokemon("Dratini", 5, "Dragon", 100, 147, 10, 10, 10, {})
    Dratini.Moves(1, "Wrap", 10, 2, "Thunder Wave", 20, "Normal", "Electric")
    Dragonair = Pokemon("Dragonair", 5, "Dragon", 100, 148, 10, 10, 10, {})
    Dragonair.Moves(1, "Wrap", 10, 2, "Thunder Wave", 20, "Normal", "Electric")
    Dragonite = Pokemon("Dragonite", 5, "Dragon", 100, 149, 10, 10, 10, {})
    Dragonite.Moves(1, "Wing Attack", 10, 2, "Hyper Beam", 20, "Flying", "Normal")
    Mewtwo = Pokemon("Mewtwo", 5, "Psychic", 100, 150, 10, 10, 10, {})
    Mewtwo.Moves(1, "Confusion", 10, 2, "Psychic", 20, "Psychic", "Psychic")
    Mew = Pokemon("Mew", 5, "Psychic", 100, 151, 10, 10, 10, {})
    Mew.Moves(1, "Pound", 10, 2, "Transform", 20, "Normal", "Normal")





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
    Pokedex.append(Caterpie)
    Pokedex.append(Metapod)
    Pokedex.append(Butterfree)
    Pokedex.append(Weedle)
    Pokedex.append(Kakuna)
    Pokedex.append(Beedrill)
    Pokedex.append(Pidgey)
    Pokedex.append(Pidgeotto)
    Pokedex.append(Pidgeot)
    Pokedex.append(Rattata)
    Pokedex.append(Raticate)
    Pokedex.append(Spearow)
    Pokedex.append(Fearow)
    Pokedex.append(Ekans)
    Pokedex.append(Arbok)
    Pokedex.append(Pikachu)
    Pokedex.append(Raichu)
    Pokedex.append(Sandshrew)
    Pokedex.append(Sandslash)
    Pokedex.append(Nidoran)
    Pokedex.append(Nidorina)
    Pokedex.append(Nidoqueen)
    Pokedex.append(Nidoran)
    Pokedex.append(Nidorino)
    Pokedex.append(Nidoking)
    Pokedex.append(Clefairy)
    Pokedex.append(Clefable)
    Pokedex.append(Vulpix)
    Pokedex.append(Ninetales)
    Pokedex.append(Jigglypuff)
    Pokedex.append(Wigglytuff)
    Pokedex.append(Zubat)
    Pokedex.append(Golbat)
    Pokedex.append(Oddish)
    Pokedex.append(Gloom)
    Pokedex.append(Vileplume)
    Pokedex.append(Paras)
    Pokedex.append(Parasect)
    Pokedex.append(Venonat)
    Pokedex.append(Venomoth)
    Pokedex.append(Diglett)
    Pokedex.append(Dugtrio)
    Pokedex.append(Meowth)
    Pokedex.append(Persian)
    Pokedex.append(Psyduck)
    Pokedex.append(Golduck)
    Pokedex.append(Mankey)
    Pokedex.append(Primeape)
    Pokedex.append(Growlithe)
    Pokedex.append(Arcanine)
    Pokedex.append(Poliwag)
    Pokedex.append(Poliwhirl)
    Pokedex.append(Poliwrath)
    Pokedex.append(Abra)
    Pokedex.append(Kadabra)
    Pokedex.append(Alakazam)
    Pokedex.append(Machop)
    Pokedex.append(Machoke)
    Pokedex.append(Machamp)
    Pokedex.append(Bellsprout)
    Pokedex.append(Weepinbell)
    Pokedex.append(Victreebel)
    Pokedex.append(Tentacool)
    Pokedex.append(Tentacruel)
    Pokedex.append(Geodude)
    Pokedex.append(Graveler)
    Pokedex.append(Golem)   
    Pokedex.append(Ponyta)
    Pokedex.append(Rapidash)
    Pokedex.append(Slowpoke)
    Pokedex.append(Slowbro)
    Pokedex.append(Magnemite)
    Pokedex.append(Magneton)
    Pokedex.append(Farfetch)
    Pokedex.append(Doduo)
    Pokedex.append(Dodrio)
    Pokedex.append(Seel)
    Pokedex.append(Dewgong)
    Pokedex.append(Grimer)
    Pokedex.append(Muk)
    Pokedex.append(Shellder)
    Pokedex.append(Cloyster)
    Pokedex.append(Gastly)
    Pokedex.append(Haunter)
    Pokedex.append(Gengar)
    Pokedex.append(Onix)
    Pokedex.append(Drowzee)
    Pokedex.append(Hypno)
    Pokedex.append(Krabby)
    Pokedex.append(Kingler)
    Pokedex.append(Voltorb)
    Pokedex.append(Electrode)
    Pokedex.append(Exeggcute)
    Pokedex.append(Exeggutor)
    Pokedex.append(Cubone)
    Pokedex.append(Marowak)
    Pokedex.append(Hitmonlee)
    Pokedex.append(Hitmonchan)
    Pokedex.append(Lickitung)
    Pokedex.append(Koffing)
    Pokedex.append(Weezing)
    Pokedex.append(Rhyhorn)
    Pokedex.append(Rhydon)
    Pokedex.append(Chansey)
    Pokedex.append(Tangela)
    Pokedex.append(Kangaskhan)
    Pokedex.append(Horsea)
    Pokedex.append(Seadra)
    Pokedex.append(Goldeen)
    Pokedex.append(Seaking)
    Pokedex.append(Staryu)
    Pokedex.append(Starmie)
    Pokedex.append(MrMime)
    Pokedex.append(Scyther)
    Pokedex.append(Jynx)
    Pokedex.append(Electabuzz)
    Pokedex.append(Magmar)
    Pokedex.append(Pinsir)
    Pokedex.append(Tauros)
    Pokedex.append(Magikarp)
    Pokedex.append(Gyarados)
    Pokedex.append(Lapras)
    Pokedex.append(Ditto)
    Pokedex.append(Eevee)
    Pokedex.append(Vaporeon)
    Pokedex.append(Jolteon)
    Pokedex.append(Flareon)
    Pokedex.append(Porygon)
    Pokedex.append(Omanyte)
    Pokedex.append(Omastar)
    Pokedex.append(Kabuto)
    Pokedex.append(Kabutops)
    Pokedex.append(Aerodactyl)
    Pokedex.append(Snorlax)
    Pokedex.append(Articuno)
    Pokedex.append(Zapdos)
    Pokedex.append(Moltres)
    Pokedex.append(Dratini)
    Pokedex.append(Dragonair)
    Pokedex.append(Dragonite)
    Pokedex.append(Mewtwo)
    Pokedex.append(Mew)









class Bag():
    def __init__(self  ,pokeball , potion , rappel):
        self.pokeball = pokeball
        self.potion = potion
        self.rappel = rappel

    
    def AddPokeball(self, number):
        self.pokeball += number
        print("Vous avez", self.pokeball, "pokeball")
    
    def AddPotion(self, number):
        self.potion += number
        print("Vous avez", self.potion, "potion")
    
    def AddRappel(self, number):
        self.rappel += number
        print("Vous avez", self.rappel, "rappel")
    
    def Display(self):
        print("Vous avez", self.pokeball, "pokeball")
        print("Vous avez", self.potion, "potion")
        print("Vous avez", self.rappel, "rappel")

    def Use(self, item, Player):
        if item == 1:
            self.pokeball -= 1
            return 1
        elif item == 2:
            self.potion -= 1
            return 2

        elif item == "rappel":
            self.rappel -= 1
            print("Vous avez", self.rappel, "rappel")
            return 3
    def ItemDisplay(self, choice):
        if choice == 1:
            print("pokeball")
        elif choice == 2:
            print("potion")
        elif choice == 3:
            print("rappel")
            

    



class Dresseur:
    def __init__(self, name, sexe, Pokemon, PositionX, PositionY, Bag ,ID = 1):
        self.name = name
        self.sexe = sexe
        self.Pokemon = {}
        self.PositionX = PositionX
        self.PositionY = PositionY
        self.ID = ID
        self.Bag = Bag




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
        print("Nom:", self.name)
        print("Sexe:", self.sexe)
        print("PositionX:", self.PositionX)
        print("PositionY:", self.PositionY)
        print("ID:", self.ID)
        print("Pokemon1:", self.Pokemon["Pokemon1"].name)
        print("Pokemon2:", self.Pokemon["Pokemon2"].name)
        print("Pokemon3:", self.Pokemon["Pokemon3"].name)
        print("Pokemon4:", self.Pokemon["Pokemon4"].name)
        print("Pokemon5:", self.Pokemon["Pokemon5"].name)
        print("Pokemon6:", self.Pokemon["Pokemon6"].name)
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
    randomPokemon = random.randint(1,10)
    randomSavage = random.randint(1,151)
    

    if Player.PositionX % 5 == 1 :
        print("=----- DUEL -----=")
        Kid = Fight("Kid", Pokedex[4])
        print("Kid want to fight")
        Kid.Setup(Player)
    if randomPokemon == 1 or randomPokemon == 5  or randomPokemon == 15 or randomPokemon == 18:
        print("=----- DUEL -----=")

        Savage = Fight("Savage", Pokedex[randomSavage])
        print("Savage", Pokedex[randomSavage].name, "appears")
        Savage.Setup(Player)
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
        

        

        print(PokemonEnemy.name,"Life:", "#" * PokemonEnemy.life)
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



                print(PokemonAlly.name, "use", PokemonAlly.MovesDisplay(choice), "on" , PokemonEnemy.name) #joueur qui attaque en deuxieme
                CheckEfficacity = TypeEffectiveness(PokemonAlly.MoveType(choice), PokemonEnemy.type ) #changer choice par rando
                print(CheckEfficacity)

                lifeEnn = (PokemonEnemy.life - PokemonAlly.MoveDamage(choice)) / CheckEfficacity
                lifeEnn = int(lifeEnn)
                PokemonEnemy.life = lifeEnn




            if PokemonEnemy.life <= 0:
                print("You win")
                MovePlayer(Player)
            if PokemonAlly.life <= 0:
                print("You lose")
                MovePlayer(Player)


                print(PokemonEnemy.name, "use", PokemonEnemy.MovesDisplay(choice), "on" ,PokemonAlly.name) #Adversaire qui attaque
                CheckEfficacity = TypeEffectiveness(PokemonEnemy.type , PokemonAlly.type)
                print(CheckEfficacity)

                life = (PokemonAlly.life - PokemonEnemy.MoveDamage(choice)) / CheckEfficacity
                life = int(life)
                PokemonAlly.life = life
                


   



            if PokemonAlly.speed < PokemonEnemy.speed:
                print(PokemonEnemy.name, "use", PokemonEnemy.MovesDisplay(choice), "on" ,PokemonAlly.name) #Adversaire qui attaque
                CheckEfficacity = TypeEffectiveness(PokemonEnemy.type , PokemonAlly.type)
                print(CheckEfficacity)

                life = (PokemonAlly.life - PokemonEnemy.MoveDamage(choice)) / CheckEfficacity
                life = int(life)
                PokemonAlly.life = life



            if PokemonEnemy.life <= 0:
                print("You win")
                MovePlayer(Player)
            if PokemonAlly.life <= 0:
                print("You lose")
                MovePlayer(Player)
                


   
                print(PokemonAlly.name, "use", PokemonAlly.MovesDisplay(choice), "on" , PokemonEnemy.name) #joueur qui attaque en deuxieme
                CheckEfficacity = TypeEffectiveness(PokemonAlly.MoveType(choice), PokemonEnemy.type ) #changer choice par rando
                print(CheckEfficacity)

                lifeEnn = (PokemonEnemy.life - PokemonAlly.MoveDamage(choice)) / CheckEfficacity
                lifeEnn = int(lifeEnn)
                PokemonEnemy.life = lifeEnn
      
    


            if PokemonEnemy.life <= 0:
                print("You win")
                MovePlayer(Player)
            if PokemonAlly.life <= 0:
                print("You lose")
                MovePlayer(Player)
            else:
                self.Setup(Player)
            

        elif choice == "2":
            print("Item")
            Player.Bag.Display()
            choice = input("Choice : ")
            choice = int(choice)
            Use = Player.Bag.Use(choice, Player)
            print(Use)
            if Use == 1:
                if self.name != "Savage":
                        print("You can't use this item on this pokemon")
                if self.name == "Savage":
                    print("You use", Player.Bag.ItemDisplay(choice), "on", self.Openent.name)
                    check = random.randint(1,10)
                    if check == 2  or check == 4 or check == 8:
                        print("You have catch the pokemon !")
                        Player.TeamAdd(self.Openent)
                        MovePlayer(Player)
                    self.Setup(Player)

                self.Setup(Player)
            elif Use == 2:
                print("temp")
                #heal
            elif Use == 3:
                print("test")
                #Rappel
            
            self.Setup(Player)

            

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

    elif Type1 == "Normal" and Type2 == "Normal":
        print("It's not very effective")
        return 1
    elif Type1 == "Normal" and Type2 == "Fire":
        print("It's not very effective")
        return 1
    elif Type1 == "Normal" and Type2 == "Water":
        print("It's not very effective")
        return 1
    elif Type1 == "Normal" and Type2 == "Grass":
        print("It's not very effective")
        return 
    elif Type1 == "Normal" and Type2 == "Electric":
        print("It's not very effective")
        return 1
    elif Type1 == "Normal" and Type2 == "Ice":
        print("It's not very effective")
        return 1
    elif Type1 == "Normal" and Type2 == "Fighting":
        print("It's not very effective")
        return 1
    elif Type1 == "Normal" and Type2 == "Poison":
        print("It's not very effective")
        return 1
    elif Type1 == "Normal" and Type2 == "Ground":
        print("It's not very effective")
        return 1
    elif Type1 == "Normal" and Type2 == "Flying":
        print("It's not very effective")
        return 1
    elif Type1 == "Normal" and Type2 == "Psychic":
        print("It's not very effective")
        return 1
    elif Type1 == "Normal" and Type2 == "Bug":
        print("It's not very effective")
        return 1
    elif Type1 == "Normal" and Type2 == "Rock":
        print("It's not very effective")
        return 1
    elif Type1 == "Normal" and Type2 == "Ghost":
        print("It's not very effective")
        return 1
    elif Type1 == "Normal" and Type2 == "Dragon":
        print("It's not very effective")
        return 1
    elif Type1 == "Normal" and Type2 == "Dark":
        print("It's not very effective")
        return 1
    elif Type1 == "Normal" and Type2 == "Steel":
        print("It's not very effective")
        return 1
    elif Type1 == "Normal" and Type2 == "Fairy":
        print("It's not very effective")
        return 1
    elif Type1 == "Fire" and Type2 == "Electric":
        print("It's not very effective")
        return 1
    elif Type1 == "Fire" and Type2 == "Ice":
        print("It's super effective")
        return 3
    elif Type1 == "Fire" and Type2 == "Fighting":
        print("It's not very effective")
        return 1
    elif Type1 == "Fire" and Type2 == "Poison":
        print("It's not very effective")
        return 1
    elif Type1 == "Fire" and Type2 == "Ground":
        print("It's super effective")
        return 3
    elif Type1 == "Fire" and Type2 == "Flying":
        print("It's not very effective")
        return 1
    elif Type1 == "Fire" and Type2 == "Psychic":
        print("It's not very effective")
        return 1
    elif Type1 == "Fire" and Type2 == "Bug":
        print("It's super effective")
        return 3
    elif Type1 == "Fire" and Type2 == "Rock":
        print("It's not very effective")
        return 1
    elif Type1 == "Fire" and Type2 == "Ghost":
        print("It's not very effective")
        return 1
    elif Type1 == "Fire" and Type2 == "Dragon":
        print("It's super effective")
        return 3
    elif Type1 == "Fire" and Type2 == "Dark":
        print("It's not very effective")
        return 1
    elif Type1 == "Fire" and Type2 == "Steel":
        print("It's super effective")
        return 3
    elif Type1 == "Fire" and Type2 == "Fairy":
        print("It's not very effective")
        return 1
    elif Type1 == "Water" and Type2 == "Electric":
        print("It's super effective")
        return 3
    elif Type1 == "Water" and Type2 == "Ice":
        print("It's not very effective")
        return 1
    elif Type1 == "Water" and Type2 == "Fighting":
        print("It's not very effective")
        return 1
    elif Type1 == "Water" and Type2 == "Poison":
        print("It's not very effective")
        return 1
    elif Type1 == "Water" and Type2 == "Ground":
        print("It's not very effective")
        return 1
    elif Type1 == "Water" and Type2 == "Flying":
        print("It's not very effective")
        return 1
    elif Type1 == "Water" and Type2 == "Psychic":
        print("It's not very effective")
        return 1
    elif Type1 == "Water" and Type2 == "Bug":
        print("It's not very effective")
        return 1
    elif Type1 == "Water" and Type2 == "Rock":
        print("It's super effective")
        return 3
    elif Type1 == "Water" and Type2 == "Ghost":
        print("It's not very effective")
        return 1
    elif Type1 == "Water" and Type2 == "Dragon":
        print("It's not very effective")
        return 1
    elif Type1 == "Water" and Type2 == "Dark":
        print("It's not very effective")
        return 1
    elif Type1 == "Water" and Type2 == "Steel":
        print("It's not very effective")
        return 1
    elif Type1 == "Water" and Type2 == "Fairy":
        print("It's not very effective")
        return 1
    elif Type1 == "Grass" and Type2 == "Electric":
        print("It's not very effective")
        return 1
    elif Type1 == "Grass" and Type2 == "Ice":
        print("It's super effective")
        return 3
    elif Type1 == "Grass" and Type2 == "Fighting":
        print("It's not very effective")
        return 1
    elif Type1 == "Grass" and Type2 == "Poison":
        print("It's super effective")
        return 3
    elif Type1 == "Grass" and Type2 == "Ground":
        print("It's super effective")
        return 3
    elif Type1 == "Grass" and Type2 == "Flying":
        print("It's super effective")
        return 3
    elif Type1 == "Grass" and Type2 == "Psychic":
        print("It's not very effective")
        return 1
    elif Type1 == "Grass" and Type2 == "Bug":
        print("It's not very effective")
        return 1
    elif Type1 == "Grass" and Type2 == "Rock":
        print("It's super effective")
        return 3
    elif Type1 == "Grass" and Type2 == "Ghost":
        print("It's not very effective")
        return 1
    elif Type1 == "Grass" and Type2 == "Dragon":
        print("It's not very effective")
        return 1
    elif Type1 == "Grass" and Type2 == "Dark":
        print("It's not very effective")
        return 1
    elif Type1 == "Grass" and Type2 == "Steel":
        print("It's not very effective")
        return 1
    elif Type1 == "Grass" and Type2 == "Fairy":
        print("It's not very effective")
        return 1
    elif Type1 == "Electric" and Type2 == "Electric":
        print("It's not very effective")
        return 1
    elif Type1 == "Electric" and Type2 == "Ice":
        print("It's not very effective")
        return 1
    elif Type1 == "Electric" and Type2 == "Fighting":
        print("It's not very effective")
        return 1
    elif Type1 == "Electric" and Type2 == "Poison":
        print("It's not very effective")
        return 1
    elif Type1 == "Electric" and Type2 == "Ground":
        print("It's super effective")
        return 3
    elif Type1 == "Electric" and Type2 == "Flying":
        print("It's super effective")
        return 3
    elif Type1 == "Electric" and Type2 == "Psychic":
        print("It's not very effective")
        return 1
    elif Type1 == "Electric" and Type2 == "Bug":
        print("It's not very effective")
        return 1
    elif Type1 == "Electric" and Type2 == "Rock":
        print("It's not very effective")
        return 1
    elif Type1 == "Electric" and Type2 == "Ghost":
        print("It's not very effective")
        return 1
    elif Type1 == "Electric" and Type2 == "Dragon":
        print("It's not very effective")
        return 1
    elif Type1 == "Electric" and Type2 == "Dark":
        print("It's not very effective")
        return 1
    elif Type1 == "Electric" and Type2 == "Steel":
        print("It's not very effective")
        return 1
    elif Type1 == "Electric" and Type2 == "Fairy":
        print("It's not very effective")
        return 1
    elif Type1 == "Ice" and Type2 == "Electric":
        print("It's super effective")
        return 3
    elif Type1 == "Ice" and Type2 == "Ice":
        print("It's not very effective")
        return 1
    elif Type1 == "Ice" and Type2 == "Fighting":
        print("It's not very effective")
        return 1
    elif Type1 == "Ice" and Type2 == "Poison":
        print("It's not very effective")
        return 1
    elif Type1 == "Ice" and Type2 == "Ground":
        print("It's super effective")
        return 3
    elif Type1 == "Ice" and Type2 == "Flying":
        print("It's super effective")
        return 3
    elif Type1 == "Ice" and Type2 == "Psychic":
        print("It's not very effective")
        return 1
    elif Type1 == "Ice" and Type2 == "Bug":
        print("It's not very effective")
        return 1
    elif Type1 == "Ice" and Type2 == "Rock":
        print("It's super effective")
        return 3
    elif Type1 == "Ice" and Type2 == "Ghost":
        print("It's not very effective")
        return 1
    elif Type1 == "Ice" and Type2 == "Dragon":
        print("It's not very effective")
        return 1
    elif Type1 == "Ice" and Type2 == "Dark":
        print("It's not very effective")
        return 1
    elif Type1 == "Ice" and Type2 == "Steel":
        print("It's not very effective")
        return 1
    elif Type1 == "Ice" and Type2 == "Fairy":
        print("It's not very effective")
        return 1
    elif Type1 == "Fighting" and Type2 == "Electric":
        print("It's super effective")
        return 3
    elif Type1 == "Fighting" and Type2 == "Ice":
        print("It's super effective")
        return 3
    elif Type1 == "Fighting" and Type2 == "Fighting":
        print("It's not very effective")
        return 1
    elif Type1 == "Fighting" and Type2 == "Poison":
        print("It's not very effective")
        return 1
    elif Type1 == "Fighting" and Type2 == "Ground":
        print("It's not very effective")
        return 1
    elif Type1 == "Fighting" and Type2 == "Flying":
        print("It's super effective")
        return 3
    elif Type1 == "Fighting" and Type2 == "Psychic":
        print("It's not very effective")
        return 1
    elif Type1 == "Fighting" and Type2 == "Bug":
        print("It's super effective")
        return 3
    elif Type1 == "Fighting" and Type2 == "Rock":
        print("It's not very effective")
        return 1
    elif Type1 == "Fighting" and Type2 == "Ghost":
        print("It's not very effective")
        return 1
    elif Type1 == "Fighting" and Type2 == "Dragon":
        print("It's not very effective")
        return 1
    elif Type1 == "Fighting" and Type2 == "Dark":
        print("It's not very effective")
        return 1
    elif Type1 == "Fighting" and Type2 == "Steel":
        print("It's super effective")
        return 3
    elif Type1 == "Fighting" and Type2 == "Fairy":
        print("It's super effective")
        return 3
    elif Type1 == "Poison" and Type2 == "Electric":
        print("It's not very effective")
        return 1
    elif Type1 == "Poison" and Type2 == "Ice":
        print("It's not very effective")
        return 1
    elif Type1 == "Poison" and Type2 == "Fighting":
        print("It's super effective")
        return 3
    elif Type1 == "Poison" and Type2 == "Poison":
        print("It's not very effective")
        return 1
    elif Type1 == "Poison" and Type2 == "Ground":
        print("It's super effective")
        return 3
    elif Type1 == "Poison" and Type2 == "Flying":
        print("It's not very effective")
        return 1
    elif Type1 == "Poison" and Type2 == "Psychic":
        print("It's not very effective")
        return 1
    elif Type1 == "Poison" and Type2 == "Bug":
        print("It's not very effective")
        return 1
    elif Type1 == "Poison" and Type2 == "Rock":
        print("It's not very effective")
        return 1
    elif Type1 == "Poison" and Type2 == "Ghost":
        print("It's not very effective")
        return 1
    elif Type1 == "Poison" and Type2 == "Dragon":
        print("It's not very effective")
        return 1
    elif Type1 == "Poison" and Type2 == "Dark":
        print("It's not very effective")
        return 1
    elif Type1 == "Poison" and Type2 == "Steel":
        print("It's not very effective")
        return 1
    elif Type1 == "Poison" and Type2 == "Fairy":
        print("It's not very effective")
        return 1
    elif Type1 == "Ground" and Type2 == "Electric":
        print("It's not very effective")
        return 1
    elif Type1 == "Ground" and Type2 == "Ice":
        print("It's not very effective")
        return 1
    elif Type1 == "Ground" and Type2 == "Fighting":
        print("It's super effective")
        return 3
    elif Type1 == "Ground" and Type2 == "Poison":
        print("It's not very effective")
        return 1
    elif Type1 == "Ground" and Type2 == "Ground":
        print("It's not very effective")
        return 1
    elif Type1 == "Ground" and Type2 == "Flying":
        print("It's super effective")
        return 3
    elif Type1 == "Ground" and Type2 == "Psychic":
        print("It's not very effective")
        return 1
    elif Type1 == "Ground" and Type2 == "Bug":
        print("It's super effective")
        return 3
    elif Type1 == "Ground" and Type2 == "Rock":
        print("It's super effective")
        return 3
    elif Type1 == "Ground" and Type2 == "Ghost":
        print("It's not very effective")
        return 1
    elif Type1 == "Ground" and Type2 == "Dragon":
        print("It's not very effective")
        return 1
    elif Type1 == "Ground" and Type2 == "Dark":
        print("It's not very effective")
        return 1
    elif Type1 == "Ground" and Type2 == "Steel":
        print("It's super effective")
        return 3
    elif Type1 == "Ground" and Type2 == "Fairy":
        print("It's not very effective")
        return 1
    elif Type1 == "Flying" and Type2 == "Electric":
        print("It's super effective")
        return 3
    elif Type1 == "Flying" and Type2 == "Ice":
        print("It's not very effective")
        return 1
    elif Type1 == "Flying" and Type2 == "Fighting":
        print("It's not very effective")
        return 1
    elif Type1 == "Flying" and Type2 == "Poison":
        print("It's super effective")
        return 3
    elif Type1 == "Flying" and Type2 == "Ground":
        print("It's not very effective")
        return 1
    elif Type1 == "Flying" and Type2 == "Flying":
        print("It's not very effective")
        return 1
    elif Type1 == "Flying" and Type2 == "Psychic":
        print("It's not very effective")
        return 1
    elif Type1 == "Flying" and Type2 == "Bug":
        print("It's not very effective")
        return 1
    elif Type1 == "Flying" and Type2 == "Rock":
        print("It's super effective")
        return 3
    elif Type1 == "Flying" and Type2 == "Ghost":
        print("It's not very effective")
        return 1
    elif Type1 == "Flying" and Type2 == "Dragon":
        print("It's not very effective")
        return 1
    elif Type1 == "Flying" and Type2 == "Dark":
        print("It's not very effective")
        return 1
    elif Type1 == "Flying" and Type2 == "Steel":
        print("It's not very effective")
        return 1
    elif Type1 == "Flying" and Type2 == "Fairy":
        print("It's not very effective")
        return 1
    elif Type1 == "Psychic" and Type2 == "Electric":
        print("It's not very effective")
        return 1
    elif Type1 == "Psychic" and Type2 == "Ice":
        print("It's not very effective")
        return 1
    elif Type1 == "Psychic" and Type2 == "Fighting":
        print("It's super effective")
        return 3
    elif Type1 == "Psychic" and Type2 == "Poison":
        print("It's super effective")
        return 3
    elif Type1 == "Psychic" and Type2 == "Ground":
        print("It's not very effective")
        return 1
    elif Type1 == "Psychic" and Type2 == "Flying":
        print("It's super effective")
        return 3
    elif Type1 == "Psychic" and Type2 == "Psychic":
        print("It's not very effective")
        return 1
    elif Type1 == "Psychic" and Type2 == "Bug":
        print("It's not very effective")
        return 1
    elif Type1 == "Psychic" and Type2 == "Rock":
        print("It's not very effective")
        return 1
    elif Type1 == "Psychic" and Type2 == "Ghost":
        print("It's super effective")
        return 3
    elif Type1 == "Psychic" and Type2 == "Dragon":
        print("It's not very effective")
        return 1
    elif Type1 == "Psychic" and Type2 == "Dark":
        print("It's not very effective")
        return 1
    elif Type1 == "Psychic" and Type2 == "Steel":
        print("It's not very effective")
        return 1
    elif Type1 == "Psychic" and Type2 == "Fairy":
        print("It's not very effective")
        return 1
    elif Type1 == "Bug" and Type2 == "Electric":
        print("It's not very effective")
        return 1
    elif Type1 == "Bug" and Type2 == "Ice":
        print("It's not very effective")
        return 1
    elif Type1 == "Bug" and Type2 == "Fighting":
        print("It's not very effective")
        return 1
    elif Type1 == "Bug" and Type2 == "Poison":
        print("It's not very effective")
        return 1
    elif Type1 == "Bug" and Type2 == "Ground":
        print("It's not very effective")
        return 1
    elif Type1 == "Bug" and Type2 == "Flying":
        print("It's super effective")
        return 3
    elif Type1 == "Bug" and Type2 == "Psychic":
        print("It's super effective")
        return 3
    elif Type1 == "Bug" and Type2 == "Bug":
        print("It's not very effective")
        return 1
    elif Type1 == "Bug" and Type2 == "Rock":
        print("It's super effective")
        return 3
    elif Type1 == "Bug" and Type2 == "Ghost":
        print("It's not very effective")
        return 1
    elif Type1 == "Bug" and Type2 == "Dragon":
        print("It's not very effective")
        return 1
    elif Type1 == "Bug" and Type2 == "Dark":
        print("It's super effective")
        return 3
    elif Type1 == "Bug" and Type2 == "Steel":
        print("It's not very effective")
        return 1
    elif Type1 == "Bug" and Type2 == "Fairy":
        print("It's not very effective")
        return 1
    elif Type1 == "Rock" and Type2 == "Electric":
        print("It's not very effective")
        return 1
    elif Type1 == "Rock" and Type2 == "Ice":
        print("It's super effective")
        return 3
    elif Type1 == "Rock" and Type2 == "Fighting":
        print("It's not very effective")
        return 1
    elif Type1 == "Rock" and Type2 == "Poison":
        print("It's not very effective")
        return 1
    elif Type1 == "Rock" and Type2 == "Ground":
        print("It's super effective")
        return 3
    elif Type1 == "Rock" and Type2 == "Flying":
        print("It's not very effective")
        return 1
    elif Type1 == "Rock" and Type2 == "Psychic":
        print("It's not very effective")
        return 1
    elif Type1 == "Rock" and Type2 == "Bug":
        print("It's not very effective")
        return 1
    elif Type1 == "Rock" and Type2 == "Rock":
        print("It's not very effective")
        return 1
    elif Type1 == "Rock" and Type2 == "Ghost":
        print("It's not very effective")
        return 1
    elif Type1 == "Rock" and Type2 == "Dragon":
        print("It's not very effective")
        return 1
    elif Type1 == "Rock" and Type2 == "Dark":
        print("It's not very effective")
        return 1
    elif Type1 == "Rock" and Type2 == "Steel":
        print("It's super effective")
        return 3
    elif Type1 == "Rock" and Type2 == "Fairy":
        print("It's not very effective")
        return 1
    elif Type1 == "Ghost" and Type2 == "Electric":
        print("It's not very effective")
        return 1
    elif Type1 == "Ghost" and Type2 == "Ice":
        print("It's not very effective")
        return 1
    elif Type1 == "Ghost" and Type2 == "Fighting":
        print("It's not very effective")
        return 1
    elif Type1 == "Ghost" and Type2 == "Poison":
        print("It's not very effective")
        return 1
    elif Type1 == "Ghost" and Type2 == "Ground":
        print("It's not very effective")
        return 1
    elif Type1 == "Ghost" and Type2 == "Flying":
        print("It's not very effective")
        return 1
    elif Type1 == "Ghost" and Type2 == "Psychic":
        print("It's not very effective")
        return 1
    elif Type1 == "Ghost" and Type2 == "Bug":
        print("It's not very effective")
        return 1
    elif Type1 == "Ghost" and Type2 == "Rock":
        print("It's not very effective")
        return 1
    elif Type1 == "Ghost" and Type2 == "Ghost":
        print("It's super effective")
        return 3
    elif Type1 == "Ghost" and Type2 == "Dragon":
        print("It's not very effective")
        return 1
    elif Type1 == "Ghost" and Type2 == "Dark":
        print("It's not very effective")
        return 1
    elif Type1 == "Ghost" and Type2 == "Steel":
        print("It's not very effective")
        return 1
    elif Type1 == "Ghost" and Type2 == "Fairy":
        print("It's not very effective")
        return 1
    elif Type1 == "Dragon" and Type2 == "Electric":
        print("It's not very effective")
        return 1
    elif Type1 == "Dragon" and Type2 == "Ice":
        print("It's not very effective")
        return 1
    elif Type1 == "Dragon" and Type2 == "Fighting":
        print("It's not very effective")
        return 1
    elif Type1 == "Dragon" and Type2 == "Poison":
        print("It's not very effective")
        return 1
    elif Type1 == "Dragon" and Type2 == "Ground":
        print("It's not very effective")
        return 1
    elif Type1 == "Dragon" and Type2 == "Flying":
        print("It's not very effective")
        return 1
    elif Type1 == "Dragon" and Type2 == "Psychic":
        print("It's not very effective")
        return 1
    elif Type1 == "Dragon" and Type2 == "Bug":
        print("It's not very effective")
        return 1
    elif Type1 == "Dragon" and Type2 == "Rock":
        print("It's not very effective")
        return 1
    elif Type1 == "Dragon" and Type2 == "Ghost":
        print("It's not very effective")
        return 1
    elif Type1 == "Dragon" and Type2 == "Dragon":
        print("It's super effective")
        return 3
    elif Type1 == "Dragon" and Type2 == "Dark":
        print("It's not very effective")
        return 1
    elif Type1 == "Dragon" and Type2 == "Steel":
        print("It's not very effective")
        return 1
    elif Type1 == "Dragon" and Type2 == "Fairy":
        print("It's not very effective")
        return 1
    elif Type1 == "Dark" and Type2 == "Electric":
        print("It's not very effective")
        return 1
    elif Type1 == "Dark" and Type2 == "Ice":
        print("It's not very effective")
        return 1
    elif Type1 == "Dark" and Type2 == "Fighting":
        print("It's super effective")
        return 3
    elif Type1 == "Dark" and Type2 == "Poison":
        print("It's not very effective")
        return 1
    elif Type1 == "Dark" and Type2 == "Ground":
        print("It's not very effective")
        return 1
    elif Type1 == "Dark" and Type2 == "Flying":
        print("It's not very effective")
        return 1
    elif Type1 == "Dark" and Type2 == "Psychic":
        print("It's super effective")
        return 3
    elif Type1 == "Dark" and Type2 == "Bug":
        print("It's not very effective")
        return 1
    elif Type1 == "Dark" and Type2 == "Rock":
        print("It's not very effective")
        return 1
    elif Type1 == "Dark" and Type2 == "Ghost":
        print("It's super effective")
        return 3
    elif Type1 == "Dark" and Type2 == "Dragon":
        print("It's not very effective")
        return 1
    elif Type1 == "Dark" and Type2 == "Dark":
        print("It's not very effective")
        return 1
    elif Type1 == "Dark" and Type2 == "Steel":
        print("It's not very effective")
        return 1
    elif Type1 == "Dark" and Type2 == "Fairy":
        print("It's super effective")
        return 3
    elif Type1 == "Steel" and Type2 == "Electric":
        print("It's not very effective")
        return 1
    elif Type1 == "Steel" and Type2 == "Ice":
        print("It's super effective")
        return 3
    elif Type1 == "Steel" and Type2 == "Fighting":
        print("It's super effective")
        return 3
    elif Type1 == "Steel" and Type2 == "Poison":
        print("It's not very effective")
        return 1
    elif Type1 == "Steel" and Type2 == "Ground":
        print("It's super effective")
        return 3
    elif Type1 == "Steel" and Type2 == "Flying":
        print("It's not very effective")
        return 1
    elif Type1 == "Steel" and Type2 == "Psychic":
        print("It's not very effective")
        return 1
    elif Type1 == "Steel" and Type2 == "Bug":
        print("It's not very effective")
        return 1
    elif Type1 == "Steel" and Type2 == "Rock":
        print("It's super effective")
        return 3
    elif Type1 == "Steel" and Type2 == "Ghost":
        print("It's not very effective")
        return 1
    elif Type1 == "Steel" and Type2 == "Dragon":
        print("It's not very effective")
        return 1
    elif Type1 == "Steel" and Type2 == "Dark":
        print("It's not very effective")
        return 1
    elif Type1 == "Steel" and Type2 == "Steel":
        print("It's not very effective")
        return 1
    elif Type1 == "Steel" and Type2 == "Fairy":
        print("It's not very effective")
        return 1
    elif Type1 == "Fairy" and Type2 == "Electric":
        print("It's not very effective")
        return 1
    elif Type1 == "Fairy" and Type2 == "Ice":
        print("It's not very effective")
        return 1
    elif Type1 == "Fairy" and Type2 == "Fighting":
        print("It's not very effective")
        return 1
    elif Type1 == "Fairy" and Type2 == "Poison":
        print("It's not very effective")
        return 1
    elif Type1 == "Fairy" and Type2 == "Ground":
        print("It's not very effective")
        return 1
    elif Type1 == "Fairy" and Type2 == "Flying":
        print("It's not very effective")
        return 1
    elif Type1 == "Fairy" and Type2 == "Psychic":
        print("It's not very effective")
        return 1
    elif Type1 == "Fairy" and Type2 == "Bug":
        print("It's not very effective")
        return 1
    elif Type1 == "Fairy" and Type2 == "Rock":
        print("It's not very effective")
        return 1
    elif Type1 == "Fairy" and Type2 == "Ghost":
        print("It's not very effective")
        return 1
    elif Type1 == "Fairy" and Type2 == "Dragon":
        print("It's super effective")
        return 3
    elif Type1 == "Fairy" and Type2 == "Dark":
        print("It's not very effective")
        return 1
    elif Type1 == "Fairy" and Type2 == "Steel":
        print("It's super effective")
        return 3
    elif Type1 == "Fairy" and Type2 == "Fairy":
        print("It's not very effective")
        return 1
    else:
        print("Error")
        return 1

    
    #type comparais

initGame()

