import random

'''Our main function where our game code runs'''
def main():
    #List of the possible ships the player can choose from when starting the game
    ship_list = ["Gunship", "Scout Ship", "Merchant Ship"]

    #Gets the players name and their ship's name 
    player_username = get_username()
    opening_sequence(player_username)
    player_ship_name = get_ship_name() 
    
    #Player chooses their ship and then their Player() class is initialized
    ship_stats = choose_ship()
    starting_health = ship_stats[0]
    starting_fuel = ship_stats[1]
    starting_money = ship_stats[2]
    starting_blaster_level = ship_stats[3]
    p1 = Player(starting_health, starting_fuel, starting_money, starting_blaster_level, player_ship_name)
    p1.check_resources()

    #Sets game to True in order for an infinite loop to repeat while the player is playing the game
    game = True
    turn_type = ""
    turn = 1
    p1.distance_traveled = 0
    
    #This while loop is everything that occurs once the player's ship is initialized. The player will input their action choices here
    while game == True:
        
        print("________________________________________________________________________________")
        print(f"Turn {turn} ({p1.distance_traveled} lightyears):")
        
        #Randomly chooses which turn type the player will encounter. (Asteroids, fight sequence, or unobstructed path)
        random_turn = randnum(1,8)
        
        #This checks if the player has traveled 100 lightyears and if so then they have won the game
        if p1.distance_traveled >= 100:
            win_game()
            game = False
         
        #The player will always encounter the shop on turn 5
        elif turn == 5:
            turn_type = "Shop"
            shop_event()
            
        #This will make the player encounter an unobstructed path turn
        elif random_turn == 1 or random_turn == 2 or random_turn == 3:
            turn_type = "Nothing"
            choosing_action = True
            print("You proceed unobstructed.")
            print(" ")
            
            #This while loop allows the player to choose to travel, ckeck stats, or leave game
            while choosing_action == True:
                #This part accounts for user error so if the user inputs something that throws an error, it will ask them to input an action again
                try: 
                    player_action = int(input("Actions:\n (1) Travel 10 lightyears \n (2) Check Ship Stats \n (3) Leave game \n"))
                except ValueError: 
                    print("Please input a valid option.")
                    print("________________________________________________________________________________")
                    continue 
                
                #This runs if the player chooses to travel
                if player_action == 1:
                    p1.travel(10,10)
                    p1.check_specific_resource("fuel")
                    choosing_action = False
                 
                #This runs if the player chooses to check stats
                elif player_action == 2:
                    p1.check_resources()
                    print("________________________________________________________________________________")
                
                #This runs if the player chooses to leave
                elif player_action == 3:
                    leave_game()
                    x = 11
                    choosing_action = False 
                    game = False 
                
                else: 
                    print("Please input a valid option.")
                    print("________________________________________________________________________________")

        #This turn will make the player encounter a fight sequence
        elif random_turn == 6 or random_turn == 7 or random_turn == 5:
            turn_type = "Enemy Ship"
            e1 = Enemy_Ship("Enemy Ship", randnum(10,15), 1)
            fight_sequence(p1, e1)
        
        #This will make the player encounter the asteroid event
        elif random_turn == 8 or random_turn == 4:
            turn_type = "Asteroid Belt"
            asteroid_event()
        
        turn += 1

        #Checks if the player's health is below zero. If so the player loses and the game stops
        if p1.check_lost() == False:
            game = False
        if out_of_fuel() == False:
            print("You ran out of fuel and got stranded in space")
            game = False
        
        
        
#dictionary storing the text for each event         
        
text = {"introduction": [["The year is 20XX."], 
                         ["Twenty years ago, an unoccupied alien spaceship crash landed on Earth, bringing with it a technological revolution."], 
                         ["The landscape of the world was altered irrevocably."],
                         ["Yet, this change came too late."],
                         ["For all of humanity’s efforts, nothing they tried could forestall the events of The Calamity."],
                         ["All the creatures of the world began to die in droves as the very air became toxic:"],
                         ["Very soon the entire Earth became inhospitable."], 
                         ["Humanity was not spared from this fate: civilization crumbled as order became chaos. Cities crumbled and humans turned on each other for their own survival. Most of humanity was wiped out."], 
                         ["Those lucky enough to survive gathered together. You, as one of the chief engineers researching the alien spaceship, was appointed to lead the operation."], 
                         ["Boarding the spacecraft, you and everyone else donned space suits and headed into space."], 
                         ["You have one goal: to locate and inhabit a hospitable planet– to ensure the survival of humanity."]], 
        
              "ending": [["Upon getting close to a largely blue planet, you hear a notification emanate from your ship’s main screen."], 
                         ["You look over and read:"], 
                         ["SCANNING… THIS PLANET IS HOSPITABLE FOR HUMANS."], 
                         ["Your exhausted visage, worn from constant stress finally loosens into something resembling jubilation."], 
                         ["Reaching over to the PA system, you give your passengers the good news. Before you end the transmission, you hear cheering from the other side."], 
                         ["Ordering your ship to land on the planet, you take the time to ruminate on the past few months."], 
                         ["You can scarce believe it- after everything that happened back on Earth, and everything that’s happened since then in space."], 
                         ["As the ship draws ever closer to the surface of the planet, you think to yourself:"], 
                         ["You can finally look at the future with hope."], 
                         ["You’re finally home."]], 

          "shop_event": [["*Orbital Outfitters’ Spacecraft detected 10 light years ahead.*"], 
                         ["*Connection secured*"], 
                         ["The ship’s screen drops down before you, showing a lizard-like alien smiling with glee:"], 
                         ["'Welcome to the Orbital Outfitters:"],
                         ["The one-stop shop for everything you need to outfit yourself to survive out in orbit!'"],
                         ["'As I’m sure you know, my name is Jericho. It’s always a pleasure to meet a potential costomo!'"], 
                         ["'Here’s what we’re offering today:'"]]
        }

#use print_text(dictionary key name) to print the text for the event
def print_text(event_name):
    list_count = 0
    for lists in text[event_name]:
        print(text[event_name][list_count]) 
        print(" ")
        list_count += 1 

#Prints this string whenever the player leaves the game
def leave_game():
    print("You left the game. Sorry to see you go.")

#Prints the win_game text when the player wins the game
def win_game():
    print("________________________________________________________________________________")
    print_text("ending") #prints value for key "ending"  
    print("________________________________________________________________________________") 
    print("Congratulations, you won the game!")
    print(" ") 
 
 #Prints all the text needed for the introductory openingf sequence
def opening_sequence(player_name):
    print_text("introduction") #prints value for key "introduction"  
    print(f"Welcome to the game {player_name}! \nYour goal is to reach Turn 11, or 100 lightyears away. \nThere lies the planet your ship's system says is inhabitable. \nGood luck!")
    print("________________________________________________________________________________") 

#Returns a random number within the range of the parameters given
def randnum(num1,num2):
    return random.randint(num1,num2)

#Gets the user's input for their name
def get_username():
    username = str(input("Enter your name!"))
    print(f"Hello {username}!")
    print("________________________________________________________________________________")
    return username

#Gets the user's input for their ship name
def get_ship_name():
    ship_name = str(input("Enter your ship's name!"))
    print(" ")
    print(f"Welcome aboard {ship_name}")
    print("________________________________________________________________________________")
    return ship_name

#This is an infinite while loop asking the user which ship type they want to choose
def choose_ship():
    still_choosing = True
    while still_choosing == True:
        try: 
            chosen_ship = int(input("Choose your ship: \n(1) Gunship (+HP +Blasters) \n(2) Scout Ship (+Fuel) \n(3) Merchant Ship (+Money)"))
        except ValueError: 
            print("Please input a valid option.")
            print("________________________________________________________________________________")
            continue 
        if chosen_ship == 1:
            print("You chose the Gunship.")
            still_choosing = False
            #These are the values for each indexs in the returned list
            #health, fuel, money, blaster_level
            return [20, 100, 30, 2]
        if chosen_ship == 2:
            print("You chose the Scout Ship.")
            still_choosing = False
            #health, fuel, money, blaster_level
            return [15, 150, 30, 1]
        if chosen_ship == 3:
            print("You chose the Merchant Ship.")
            still_choosing = False
            #health, fuel, money, blaster_level
            return [15, 100, 50, 1]
        else:
            print("Your choice was not recognized by the game. Enter again.")
        
        print("________________________________________________________________________________")

#This is the turn type, fight_sequence. player attacks enemy_ship either until one dies or the player chooses to flee
def fight_sequence(player, enemy_ship):
    fight = True
    engage_or_flee = True
    while engage_or_flee == True:
        try: 
            #Asks the user to either engage the enemy ship or flee
            player_choice = int(input("You see an enemy ship in the distance do you choose to engage or flee? \n(1) Engage \n(2) Flee"))
        except ValueError: 
            print("Please input a valid option.")
            print("________________________________________________________________________________")
            continue 
        if player_choice == 1:
            engage_or_flee = False
            print("You have engaged the enemy ship.")
            while fight == True:
                print("________________________________________________________________________________")
                try: 
                    player_input = int(input("Would you like to attack or flee? \n(1) Attack \n(2) Flee"))
                except ValueError: 
                    print("Please input a valid option.")
                    print("________________________________________________________________________________")
                    continue
                if player_input == 1:
                    print("________________________________________________________________________________")
                    #The enemy takes damage based on the player's self.damage variable.
                    enemy_ship.take_damage(player.attack())
                    enemy_ship.check_specific_resource("health")
                    #This runs if the enemy_ship was killed
                    if enemy_ship.health <= 0: 
                        print("________________________________________________________________________________")
                        player.enemy_ship_killed(randnum(0,2)*10, randnum(0,5), randnum(0,1), randnum(0,10))
                        fight = False 
                        player.travel(10,10)
                    else:
                        #The player takes damage based on the enemy ship's self.damage variable
                        player.take_damage(enemy_ship.attack())
                        player.check_specific_resource("health")
                        if player.health <= 0:
                            game = player.lost_game()
                            fight = False
                #Runs if the player chooses to flee
                if player_input == 2:
                    player.travel(10,10)
                    player.check_specific_resource("fuel")
                    fight = False
        #Runs if the player chooses to flee
        elif player_choice == 2:
            engage_or_flee = False
            player.travel(10, 10)
            player.check_specific_resource("fuel")
        else:
            print(f"Your input, {player_choice} was not recognized by the game. Please type either 'Engage' or 'Flee'.")

#The player encounters an asteroid field and either goes around for 20 fuel or goes through with a 50% chance to take 5 damage
def asteroid_event(): 
    print("You spot an asteroid belt ahead of your ship.")
    print(" ")
    choosing_action = True 
    while choosing_action == True: 
        try: 
            player_choice = int(input(print("What do you choose to do? \n(1) Go through it (50% chance of -5HP) \n(2) Go around (-20 fuel)")))
        except ValueError: 
            print("Please input a valid option.")
            print("________________________________________________________________________________")
            continue 
        #Runs if the player chose to go through the asteroids
        if player_choice == 1: 
            choosing_action = False 
            #50/50 chance if the randnum returns 0 or 1
            randnum_result = randnum(0,1)
            p1.travel(10,10)
            #Player doesn't take damage
            if randnum_result == 0: 
                print("You navigate through the asteroid belt with precision. \nYou make it through with your ship unharmed.")

            #Player takes damage
            if randnum_result == 1: 
                p1.take_damage(5) 
                print("As you navigate through the asteroid belt, you feel a sudden impact. \nA stray asteroid hit your ship! \n-5HP")
                if p1.health <= 0:
                    game = p1.lost_game()
        #Player chose to go around    
        elif player_choice == 2: 
            choosing_action = False 
            p1.travel(10, 20) #I stuck with the travel function because travel also adds to self.distance_traveled
            print("You choose to go around the asteroid belt, spending 20 fuel but avoiding potential ruin.")                                
         
        #Player inputed something that threw an error
        else: 
            print("Please input a valid option.")
            print("________________________________________________________________________________")

#Variables for the shop
shop_fuel = 50 
shop_fuel_price = 10
blasters_price = 30 
fix_ship_price = 10 

#Happens on turn 5 of the game
def shop_event(): 
    #More variables for shop function
    purchase = False 
    exit_shop = False 
    shop_1 = True 
    shop_2 = True 
    shop_3 = True 
    
    print_text("shop_event") #prints value for key "shop_event"  
    print("________________________________________________________________________________")
    
    #Prints shop inventory
    shop_inventory = [f"(1) Fuel {shop_fuel} | Price: {shop_fuel_price}", f"(2) Blasters Upgrade (+Dmg) | Price: {blasters_price}", f"(3) Fix ship (+10 HP)| Price: {fix_ship_price}"] 
    
    while exit_shop == False: 
        
        for string in shop_inventory: 
            print(string)
        print("(4) Leave shop")
        
        player_input = int(input("What would you like to purchase? (Enter the number of your purchase)"))
    
        #Player bought fuel only if fuel is still available stored as shop_1
        if player_input == 1:
            if shop_1 == True: 
                if p1.money >= shop_fuel_price: 
                    p1.money -= shop_fuel_price
                    purchase = True 
                    p1.gain_fuel(shop_fuel)
                    p1.spend_money(shop_fuel_price)
                    shop_inventory.remove(f"(1) Fuel {shop_fuel} | Price: {shop_fuel_price}")
                    shop_1 = False 
                else: 
                    print("You don't have enough money.")
            else: 
                print("Please input a valid option.")

        #Player bought blasters only if blaster is still available stored as shop_2
        elif player_input == 2: 
            if shop_2 == True: 
                if p1.money >= blasters_price: 
                    p1.money -= hyperdrive_price 
                    purchase = True 
                    blasters_upgrade() 
                    shop_inventory.remove(f"(2) Blasters Upgrade (+Dmg) | Price: {blasters_price}") 
                    shop_2 = False 
                else: 
                    print("You don't have enough money.")
            else: 
                print("Please input a valid option.")

        #Player bought a ship repair only if it is still available stored as shop_3
        elif player_input == 3: 
            if shop_3 == True: 
                if p1.money >= fix_ship_price: 
                    p1.money -= fix_ship_price 
                    purchase = True 
                    p1.repair_health(10)
                    shop_inventory.remove(f"(3) Fix ship (+10 HP)| Price: {fix_ship_price}") 
                    shop_3 = False 
                else: 
                    print("You don't have enough money.")
            else: 
                print("Please input a valid option.")

        #Player exits shop
        elif player_input == 4: 
            exit_shop = True 
        
        #Player travels another 10 light years after leaving shop
        if exit_shop == True: 
            p1.travel(10, 10)
            print()
            print("Hope to see you again!")
        
        #Checks if the player had purchased anything
        if purchase == True: 
            purchase = False 
            print("Thank you for your purchase!")
            print("Anything else tickle your fancy?") 
        
        print("________________________________________________________________________________")

        
        
#This is the class we will use for the player 
class Player:

    #The player has health, fuel, money, a blaster level correlated to damage, and a ship name
    def __init__(self, health, fuel, money, blasters_level, ship_name):
        self.ship_name = ship_name
        self.health = health
        self.fuel = fuel
        self.money = money
        self.blasters_level = blasters_level
        if blasters_level == 1:
            self.blasters_damage = 5
        elif blasters_level == 2:
            self.blasters_damage = 10
        elif blasters_level == 3:
            self.blasters_damage = 15
        self.hyperdrive = False
        self.distance_traveled = 0

    #Displays a resource given as a parameter and prints how much the player has left
    def check_specific_resource(self, resource):
        if resource == "health":
            print(f"{self.ship_name} has {self.health} health remaining")
        if resource == "fuel":
            print(f"{self.ship_name} has {self.fuel} fuel remaining")    
        if resource == "distance":
            print(f"{self.ship_name} has traveled {self.distance} lightyears")

    #Prints how much of all the resources the player has
    def check_resources(self):
        print("________________________________________________________________________________")
        print(f"{self.ship_name} stats: \n\nHealth: {self.health}")
        print(f"Fuel: {self.fuel} \nMoney: {self.money} \nBlaster Level: {self.blasters_level} \nBlaster damage: {self.blasters_damage} \nDistance Traveled: {self.distance_traveled}")

    #Returns the self.damage stat to be used in the fight sequence
    def attack(self):
        damage = self.blasters_damage
        return damage
    
    #Returns false if the player's health is below or equal to 0
    def check_lost(self): 
        if self.health <= 0: 
            return False

    #Prints that the player lost the game
    def lost_game(self):
        print("Sorry, you lost the game. :'(")
        return False

    #Returns false if the players fuel is at or below 0
    def out_of_fuel(self):
        if self.fuel <= 0:
            return False
    
    #Subtracts from self.health the amount given as a parameter
    def take_damage(self,damage):
        self.health -= damage

    #Adds to the players self.health variable
    def repair_health(self, repair):
        self.health += repair

    #Increases self.travel_distance while decreasing self.fuel
    def travel(self, travel_distance, used_fuel):
        self.distance_traveled += travel_distance
        self.fuel -= used_fuel
        print(f"You spent {used_fuel} fuel to travel {travel_distance} lightyears")

    #Adds to the players self.fuel variable the amount given as a parameter
    def gain_fuel(self, gained_fuel):
        self.fuel += gained_fuel

    #Decreases the player's money
    def spend_money(self, money_spent):
        self.money -= money_spent

    #Increases the player's money
    def gain_money(self, money_gained):
        self.money += money_gained

    #Adds another level to the players self.blasters_level variable
    def blasters_upgrade(self):
        self.blasters_level += 1
        calibrate_blaster_damage(self.blasters_level)

    #This method just adjusts the players damage based on what their guns level is (1,2,3)
    def calibrate_blaster_damage(self, new_blasters_level):
        if new_blasters_level == 1:
            self.blasters_damage = 5
        elif new_blasters_level == 2:
            self.blasters_damage = 10
        elif new_blasters_level == 3:
            self.blasters_damage = 15

    #Called whenever the enemy ship dies in the fight sequence. Adds a random amount of health, fuel, blaster upgrade, and money to the player
    def enemy_ship_killed(self, fuel_acquired, health_acquired, blaster_upgrade_acquired, money_acquired):
        print(f"You killed the enemy ship!")
        print(f"You acquired {fuel_acquired} fuel, {health_acquired} HP, {blaster_upgrade_acquired} blaster upgrade, and {money_acquired} money.")
        self.fuel = self.fuel + fuel_acquired
        self.money = self.fuel + money_acquired
        self.blaster_level = self.blasters_level + blaster_upgrade_acquired
        p1.calibrate_blaster_damage(self.blaster_level)
        self.health = self.health + health_acquired
        p1.check_resources()

#The loot parameter will be a list of the what the player will recieve if they kill an enemy ship (fuel, money)

#this class will create enemy ships that the player will have to fight. 
class Enemy_Ship():

    #The enemy has a name, health, and a blaster level for damage
    def __init__(self, name, health, enemy_blasters_level):
        if enemy_blasters_level == 1:
            self.blasters_damage = 5
        elif enemy_blasters_level == 2:
            self.blasters_damage = 10
        elif enemy_blasters_level == 3:
            self.blasters_damage = 15
        self.health = health
        self.name = name
        
    #Same as the attack method in Player
    def attack(self):
        damage = self.blasters_damage
        return damage
     
    #Same as the take_damage method in Player
    def take_damage(self,damage):
        self.health -= damage
        
    #Same as the check_specific_resource method in Player but used for the enemy ship's health in fight sequence
    def check_specific_resource(self, resource):
        if resource == "health":
            print(f"{self.name} has {self.health} health remaining")
        if resource == "fuel":
            print(f"{self.name} has {self.fuel} fuel remaining")    
        if resource == "distance":
            print(f"{self.name} has traveled {self.distance} lightyears")

#Initializes the player first thing so no errors are thrown for not recognizing p1
p1 = Player(0,0,0,0,"0")
main()     