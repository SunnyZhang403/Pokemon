import time
import numpy as np
import sys
import random
import math
# Delay printing

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Create the class
class Pokemon:
    def __init__(self, name, types, moves, EVs, fightstatus, health='==================='):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # Amount of health bars
        self.status = fightstatus


    def fight(self, Pokemon2):
        # Allow two pokemon to fight each other

        # Print fight information
        print("-----POKEMONE BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))

        time.sleep(2)

        # Consider type advantages
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                # Both are same type
                if Pokemon2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # Pokemon2 is STRONG
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # Pokemon2 is WEAK
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'


        # Now for the actual fighting...
        # Continue while pokemon still have health
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # Print the health of each pokemon
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # Add back bars plus defense boost
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' fainted.')
                break

            # Pokemon2s turn

            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            self.bars -= Pokemon2.attack
            self.health = ""

            # Add back bars plus defense boost
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')
                break

        money = np.random.choice(5000)
        delay_print(f"\nOpponent paid you ${money}.\n")

    def capturefight(self, Pokemon2):
        fightstatus = "ongoing"
        # Allow two pokemon to fight each other

        # Print fight information
        print("-----POKEMONE BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))

        time.sleep(2)

        # Consider type advantages
        version = ['Fire', 'Water', 'Grass']

        for i,k in enumerate(version):
            if self.types == k:
                # Both are same type
                if Pokemon2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # Pokemon2 is STRONG
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # Pokemon2 is WEAK
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'


        # Now for the actual fighting...
        # Continue while pokemon still have health
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # Print the health of each pokemon
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # Add back bars plus defense boost
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon is low enough health to be taken
            if Pokemon2.bars <= 3:
                delay_print("\n..." + Pokemon2.name + ' can be captured!')
                print(" Do you want to use a pokeball to capture", Pokemon2.name + "?")
                if input() == "yes":
                    self.status = "captured"
                    print("Captured", Pokemon2.name)
                else:
                    self.status = "won"
    

                break

            # Pokemon2s turn

            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)
            index = random.randint(1,4)
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            self.bars -= Pokemon2.attack
            self.health = ""

            # Add back bars plus defense boost
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')
                self.status = "lost"

                break



class Trainer:
    def __init__ (self, name,XP,level, NumberOfPokemon, TeamPokemon, selectedPokemon, action):
        self.name = name
        self.xp = XP
        self.level = level
        self.number = NumberOfPokemon
        self.pokemon = TeamPokemon
        self.selected = selectedPokemon
        self.action = action

    #Checking Trainer XP
    def checkXP(self):
        print("You currently have", self.xp%10, "XP")

    #Checking Trainer level
    def checkLevel(self):

        print("You are level", math.floor(self.xp/10))

    #Choosing Starter Pokemon
    def chooseStarter (self):

        print("Please select your starter Pokemon:")
        print("Type Charmander, Squirtle, Bulbasaur, Treecko, Torchic, or Mudkip to select your starter")
        starter = input()
        if starter == "Charmander":
            self.pokemon.append(Charmander)

        elif starter == "Squirtle":
            self.pokemon.append(Squirtle)


        elif starter == "Bulbasaur":
            self.pokemon.append(Bulbasaur)

        elif starter == "Treecko":
            self.pokemon.append(Treecko)

        elif starter == "Torchic":
            self.pokemon.append(Torchic)

        elif starter == "Mudkip":
            self.pokemon.append(Mudkip)

        self.number = len(self.pokemon)

    #Checking owned Pokemon
    def checkPokemon (self):

        if self.number > 0:
            print("You currently have:")
            for i in range(len(self.pokemon)):
                print(i+1, self.pokemon[i].name, "Level:", 3*(1+np.mean([self.pokemon[i].attack, self.pokemon[i].defense])), "Attack:", self.pokemon[i].attack,"Defense:", self.pokemon[i].defense)
        else:
            print("No Pokemon currently")

    #Choosing Pokemon to fight
    def selectPokemon(self):

        print("Please select your pokemon. You currently have", len(self.pokemon), "pokemon. Type a number between 1 and", len(self.pokemon), "to select.")
        self.selected = self.pokemon[int(input())-1]
        print("You have selected", self.selected.name)
 
        
    #Capturing pokemon
    def catchPokemon (self):

        randomPokemon = random.choice(listOfPokemon)
        x = randomPokemon.attack
        y = randomPokemon.defense
        a, b = self.selected.attack, self.selected.defense
        if self.selected == "No Pokemon Selected":
            print("No Pokemon currently selected, please select a Pokemon before entering a fight.")
            exit
        elif self.selected != "No Pokemon Selected":
            print("You encountered a wild", randomPokemon.name)
            print("Would you like to try to capture it? (typ yes or no)")

        response = input()
        if response == "yes" and self.selected != "No Pokemon Selected":
            if self.level < 2:
                randomPokemon.attack = 2
                randomPokemon.defense = 2

            self.selected.capturefight(randomPokemon)
            if self.selected.status == "captured":
                randomPokemon.attack = x
                randomPokemon.defense = y
                self.pokemon.append(randomPokemon)
                listOfPokemon.remove(randomPokemon)
                self.number = len(self.pokemon)
                self.xp = self.xp+5
                self.selected.attack = a + 1
                self.selected.defense = b + 1

            elif self.selected.status == "won":
                self.xp = self.xp+5


    #Removing Pokemon

    def removePokemon(self):

        remove = input("Which Pokemon would you like to remove?")
        self.pokemon.remove(remove)
    def healPokemon (self):
        for i in range (len(self.pokemon)):
            self.pokemon[i].health = '==================='
            self.pokemon[i].bars = 20


    
                
    
            
def selectAction(Player):
    if action == "xp":
        Player.checkXP()
    if action == "level":
        Player.checkLevel()
    if action == "pokemon":
        Player.checkPokemon()
    if action == "select":
        Player.selectPokemon()
    if action == "capture":
        Player.catchPokemon()
    if action == "heal":
        Player.healPokemon()
    if action == "exit":
        print("Exiting now! See you next time!")
        exit()

        
            
            



    

if __name__ == '__main__':
    #Create Pokemon
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE': 8},"none")
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK': 10, 'DEFENSE':10}, "none")
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':8, 'DEFENSE':12}, "none")

    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK':3, 'DEFENSE':4}, "none")
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],{'ATTACK': 3, 'DEFENSE':3}, "none")
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATTACK':2, 'DEFENSE':4}, "none")

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATTACK':6, 'DEFENSE':5},"none")
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ATTACK': 5, 'DEFENSE':5}, "none")
    Ivysaur = Pokemon('Ivysaurt', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':4, 'DEFENSE':6}, "none")

    Treecko = Pokemon('Treecko', 'Grass', ['Leer', 'Pound', 'Leafage', 'Quick Attack'],{'ATTACK':3, 'DEFENSE':4}, "none")
    Torchic = Pokemon('Torchic', 'Fire', ['Growl', 'Scratch', 'Ember', 'Quick Attack'],{'ATTACK': 3, 'DEFENSE':3}, "none")
    Mudkip = Pokemon('Mudkip', 'Water', ['Growl', 'Tackle', 'Water Gun', 'Rock Smash'],{'ATTACK':4, 'DEFENSE':2}, "none")



listOfPokemon = [Charizard, Blastoise, Venusaur, Charmander, Squirtle, Bulbasaur, Charmeleon, Wartortle, Ivysaur, Treecko, Torchic, Mudkip]


Player1 = Trainer(input("Welcome to Pokemon! What's your name? "), 0, 0, 0, [], "No Pokemon Selected", "none")
print("Hello", Player1.name + "!")
Player1.chooseStarter()
listOfPokemon.remove(Player1.pokemon[0])
while True:
    action = input("What would you like to do? Check your experience (xp), check your level (level),\ncheck your Pokemon (pokemon), select your Pokemon (select), heal your Pokemon(heal), or try to capture\na Pokemon (capture). Type 'exit'to exit ")

    selectAction(Player1)