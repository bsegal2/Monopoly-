import Draw
import random

#Set up the monopoly board
def monopolyBoard():
    Draw.setCanvasSize(1000, 800)
    game()    
    
#Set up user interaction     
def waitForKey(waitingForYN = False):
    while True:
        if Draw.hasNextKeyTyped():
            newKey = Draw.nextKeyTyped()
            if waitingForYN == True:
                if newKey.upper() == 'Y':
                    return True
                elif newKey.upper() == 'N':
                    return False
            else:
                if newKey == 'Return' or newKey == 'Enter':
                    return
                
#function to move around players            
def reDrawScreen(Draw, locations, players):
    #Draw player one
    Draw.setColor(Draw.RED)
    Draw.filledOval((locations[(players[0][0])][1]), \
                    (locations[(players[0][0])][2]), \
                    15, 15) 
    Draw.show()
    
    #Draw player two          
    Draw.setColor(Draw.BLUE)
    Draw.filledOval((locations[(players[1][0])][1]), \
                    (locations[(players[1][0])][2]), \
                    15, 15)
    Draw.show()
    
#Function to refresh balances   
def refreshBalances(Draw, currentPlayer, currentPlayerBalance, currentPlayerOwned):
    #Display new balance for both players:  
    if currentPlayer == 0: 
        #Clear Old Balances
        Draw.setColor(Draw.WHITE)
        Draw.filledRect(750, 70, 250, 79)    
        #New Balance
        Draw.setFontSize(18)
        Draw.setColor(Draw.RED)
        Draw.string("Player 1:", 770, 70)
        Draw.string("Balance: " + "$" + \
                    str(currentPlayerBalance),\
                    770, 100)
        Draw.string("Owned Properties: " + str(currentPlayerOwned), 770, 130)
        Draw.show()
        
    #Display new balance for player 1
    elif currentPlayer == 1: 
        #Clear Old Balances
        Draw.setColor(Draw.WHITE)
        Draw.filledRect(750, 170, 250, 79)    
        #New Balance
        Draw.setFontSize(18)
        Draw.setColor(Draw.BLUE)
        Draw.string("Player 2:", 770, 170)
        Draw.string("Balance: " + "$" + \
                    str(currentPlayerBalance),\
                    770, 200)
        Draw.string("Owned Properties: " + str(currentPlayerOwned), 770, 230)
        Draw.show()
        
#Function to clear the user interaction
def clearUserInteraction():
    Draw.setColor(Draw.WHITE)
    Draw.filledRect(0, 750, 1000, 50)
    
#redraw pieces around the board
def game():    
    #locations = [place on board, x coordinate, y coordinate, owner, rent, money add/substract]
    locations = [["Go", 692.5, 692.5, None, 0, 200], 
                 ["Mediterranean Avenue", 611.945, 692.5, None, 2, 60],
                 ["Community Chest",550.825, 692.5, None, None, None],
                 ["Baltic Avenue", 489.715, 692.5, None, 4, 60],
                 ["Income Tax", 428.605, 692.5, None, None, 200], 
                 ["Reading Railroad", 367.495, 692.5, None, 25, 200],
                 ["Oriental Avenue", 306.385, 692.5, None, 6, 100],
                 ["Chance", 245.275, 692.5, None, None, None],
                 ["Vermont Avenue", 184.165, 692.5, None, 6, 100],
                 ["Connecticut Avenue", 123.055, 692.5, None, 8, 120], 
                 ["Just Visiting", 42.5, 692.5, None, None, None],
                 ["St. Charles Place", 42.5, 611.945, None, 10, 140],
                 ["Electric Company", 42.5, 550.825, None, 50, 150],
                 ["States Avenue", 42.5, 489.715, None, 10, 140], 
                 ["Virginia Avenue", 42.5, 428.605, None, 12, 160],
                 ["Pennsylvania Railroad", 42.5, 367.495, None, 25, 200],
                 ["St. James Place", 42.5, 306.385, None, 14, 180],
                 ["Community Chest", 42.5, 245.275, None, None, None],
                 ["Tennessee Ave", 42.5, 184.165, None, 14, 180],
                 ["New York Avenue", 42.5, 123.055, None, 16, 200], 
                 ["Free Parking", 42.5, 42.5, None, None, None],
                 ["Kentucky Avenue",123.055, 42.5, None, 18, 220], 
                 ["Chance", 184.165, 42.5, None, None, None], 
                 ["Indiana Avenue", 245.275, 42.5, None, 18, 220],
                 ["Illinois Avenue", 306.385, 42.5, None, 20, 240], 
                 ["B.&O. Railroad", 367.495, 42.5, None, 25, 200], 
                 ["Atlantic Avenue", 428.605, 42.5, None, 22, 260],
                 ["Ventnor Avenue", 489.715, 42.5, None, 22, 260], 
                 ["Water Works", 550.825, 42.5, None, 50, 150], 
                 ["Marvin Gardens", 611.945, 42.5, None, 24, 280], 
                 ["Go To Jail", 692.5, 42.5, None, None, None], 
                 ["Pacific Avenue", 692.5, 123.055, None, 26, 300], 
                 ["North Carolina Avenue", 692.5, 184.165, None, 26, 300], 
                 ["Community Chest", 692.5, 245.275, None, None, None], 
                 ["Pennsylvania Avenue", 692.5, 306.385, None, 28, 320], 
                 ["Short Line", 692.5, 367.495, None, 25, 200], 
                 ["Chance", 692.5, 428.605, None, None, None], 
                 ["Park Place", 692.5, 489.715, None, 35, 350], 
                 ["Luxury Tax", 692.5, 550.825, None, None, 100], 
                 ["Boardwalk", 692.5, 611.945, None, 50, 400]] 
  
    #all of the locations that can't be bought
    unbuyable = ["Go", "Community Chest", "Chance", "Go To Jail", "Free Parking",\
                 "Just Visiting", "Income Tax", "Luxury Tax"]    
   
   
   ##Setting up initial values 
   #Initial balance for each player
    balance = 1500
    
    #Initial amount of properties
    amountOfOwnedProperties = 0
    
    #Initial Players' position and balance
    players = [[0, balance, amountOfOwnedProperties], 
               [0, balance, amountOfOwnedProperties]] 
    #First Player
    currentPlayer = 0 
    
    #While Game Not Over
    #While each player's balance is more than zero
    while players[0][1] > 0 and players[1][1] > 0:
        #Roll The Dice On a Blank Board
        dice = random.randint(2, 12)  
        clearUserInteraction()     
        #Tell user what number has been rolled and display it on the screen
        Draw.setColor(Draw.DARK_GREEN)
        Draw.setFontSize(20)
        Draw.string(("Player " + str(currentPlayer + 1) + " rolled "\
                    + str(dice)) + " Press Enter To Continue", 10, 760)
        Draw.show()
        #wait for user interactions
        waitForKey()
        #clear user interaction
        clearUserInteraction()  
        #Import Monopoly image board
        Draw.picture("MONOPOLY.gif", 0, 0)  
        #Import Price Chart
        Draw.picture("Price and Rent.gif", 750, 250)
        Draw.setFontSize(18)
        Draw.setColor(Draw.BLACK)
        #Tell player to press enter if want to continue 
        Draw.string("PRESS ENTER", 770, 10)
        Draw.string("TO CONTINUE", 770, 28)          
        #Move each piece one after the other
        currentPosition = players[currentPlayer][0] 
        
        #Position before
        beforePosition = players[currentPlayer][0]
        
        #amount of steps each player moves 
        players[currentPlayer][0] = (players[currentPlayer][0]\
                                     + dice) % 40
        #Position after dice roll
        afterPosition = players[currentPlayer][0]
        
        #draws players in new postions
        reDrawScreen(Draw, locations, players)
        
        #Player Balance
        currentPlayerBalance = players[currentPlayer][1] 
        
        #Current Player Number of Owned Properties
        currentPlayerOwned = players[currentPlayer][2] 
        
        #New Player Balance
        refreshBalances(Draw, currentPlayer, currentPlayerBalance, currentPlayerOwned)
        
        #Property 
        propertyName = locations[players[currentPlayer][0]][0]
        
        #Property X coordinate
        propertyX = locations[players[currentPlayer][0]][1]
        
        #Property Y coordinate
        propertyY = locations[players[currentPlayer][0]][2]
        
        #Property Owner
        propertyOwner = locations[players[currentPlayer][0]][3]
        
        #Property Rent
        propertyRent = locations[players[currentPlayer][0]][4]
        
        #PropertyPrice
        propertyPrice = locations[players[currentPlayer][0]][5]  
          
        #If Player passes GO
        if afterPosition < beforePosition: 
            #Add 200 to the player's balance
            currentPlayerBalance += locations[0][5]
            #Display that the player passed GO
            Draw.setFontSize(18)
            Draw.setColor(Draw.DARK_GREEN)
            Draw.string("Player " + str(currentPlayer + 1) + " passed Go and got $200", 10, 760) 
            Draw.show()  
            #Wait for the player to press enter
            waitForKey()
            #Refresh the balances
            refreshBalances(Draw, currentPlayer, \
                            currentPlayerBalance, currentPlayerOwned)
            #Clear user interaction
            clearUserInteraction()
            
        
        #Determine whether someone owns a certain property/utility
        if propertyOwner == None and propertyName not in unbuyable:
            #Display image asking player if they want to buy the property/utility
            Draw.setFontSize(20)
            Draw.setColor(Draw.DARK_GREEN)
            Draw.string("Player " + str(currentPlayer + 1) + \
                        ": Do You Want To Buy " + str(propertyName) \
                        + "? Y/N ", 10, 760) 
            Draw.show() 
            #See if the player pressed Y
            buy = waitForKey(True)
            #If the player types "Y"
            if buy:
                # Attempt to withdraw money:
                if currentPlayerBalance - propertyPrice > 0:
                    # buy it
                    currentPlayerBalance = currentPlayerBalance - propertyPrice 
                    #Add property to player's property list
                    currentPlayerOwned = currentPlayerOwned + 1
                       
                    # Set as owner
                    propertyOwner = currentPlayer
                    # Display that property has been bought
                    clearUserInteraction()
                    Draw.setFontSize(20)
                    Draw.setColor(Draw.DARK_GREEN)                    
                    Draw.string("Purchased Successfully!!", 10, 760)
                    Draw.show(1000)   
    
                else:
                    #cant buy it
                    #Display that user cannot buy it
                    clearUserInteraction()
                    Draw.setFontSize(20)
                    Draw.setColor(Draw.DARK_GREEN)                     
                    Draw.string("Not Enough Funds :-(", 10, 760)
                    Draw.show(1000) 
                    
        elif propertyOwner == 1 - currentPlayer:
            # pay rent
            currentPlayerBalance -= propertyRent
            #Tell player that they paid rent
            Draw.setFontSize(12)
            Draw.setColor(Draw.DARK_GREEN)
            Draw.string("Player " + str(currentPlayer + 1) + \
                        " Rent paid on " + str(propertyName) + " successfully!!", 10, 760) 
            Draw.show()
           
            #add rent value to owner
            players[1 - currentPlayer][1] += propertyRent 
            Draw.string("Player " + str((1 - currentPlayer) + 1) + \
                        " recieved rent for " + str(propertyName) +  " successfully!!", 10, 775)  
            Draw.show()
            #wait for enter
            waitForKey()
          
        #If the place on the board can't be bought
        if propertyName in unbuyable: 
            #if player lands on Just Visiting, do nothing
            if propertyName == "Just Visiting":
                pass
            #If player lands on free parking, do nothing
            elif propertyName == "Free Parking": 
                pass
            
            #if player needs to pay taxes
            #The Tax Amount
            tax = locations[players[currentPlayer][0]][5] 
            #If it is the luxury tax
            if propertyName == "Luxury Tax": 
                #Pay the tax
                currentPlayerBalance -= tax
                
                #Tell user that luxury tax was paid successfully
                Draw.setFontSize(18)
                Draw.setColor(Draw.DARK_GREEN)
                Draw.string(("Player " + str(currentPlayer + 1) + \
                             " Paid Luxury Tax Successfully"), 10, 760)
                Draw.show()  
                waitForKey()
             #If it is the income tax
            elif propertyName == "Income Tax": 
                currentPlayerBalance -= tax
               #Tell user that income tax was paid successfully
                Draw.setFontSize(18)
                Draw.setColor(Draw.DARK_GREEN)
                Draw.string(("Player " + str(currentPlayer + 1) + \
                             " Paid Income Tax Successfully"), 10, 760)
                Draw.show()  
                waitForKey()              
                    
            #If player lands on Community Chest  
            elif propertyName == "Community Chest" : 
                communityChest = [["Income Tax Refund: Collect $20", 20],
                                  ["Bank Error In Your Favor: Collect $200", 200],
                                  ["Doctor's Fees: Pay $50", -50],
                                  ["School Fees: Pay $50", -50], 
                                  ["You have won second prize in " + \
                                   "a beauty contest: Collect $10", 10]]
                #Choose a card
                card = random.choice(communityChest)
                Draw.setFontSize(18)
                Draw.setColor(Draw.DARK_GREEN)
                #Tell player to choose a card
                Draw.string(("Player " + str(currentPlayer + 1) + " Landed on Community Chest: Press Enter To Pick A Card"), 10, 760)
                Draw.show() 
                #Wait for player to choose a card
                waitForKey()
                clearUserInteraction()
                
                #add value on card to player balance
                currentPlayerBalance += card[1] 
                    
                #Let Player know of what card they got
                #If Value of card is positive, and money is being addded
                if card[1] > 0:
                    #Tell player that money is being added
                    Draw.setFontSize(18)
                    Draw.setColor(Draw.DARK_GREEN)
                    Draw.string("Player " + str(currentPlayer + 1) +  " " +\
                                card[0] + ","  + " $" + str(card[1]) + " Has been added to your balance!", 10, 760)
                    Draw.show()
                    waitForKey()
                    
                #If Value of card is negative, and money is being subtracted             
                elif card[1] < 0: 
                     #Tell player that money is being subtracted
                    Draw.setFontSize(18)
                    Draw.setColor(Draw.DARK_GREEN)
                    Draw.string("Player " + str(currentPlayer + 1) + " " + card[0]\
                                + ","  + " $" + str(abs(card[1])) + " Has been subtracted from your balance", 10, 760)
                    Draw.show()
                    waitForKey()
            
            #If player lands on Chance
            elif propertyName == "Chance": 
                #chance = [“You inherit $100” , “It’s your birthday: Collect $10 from every 
                #player”, “Bank pays you a dividend of $50”, “Hospital Fees: pay $100”, 
                #“Collect Stock dividend of $50”]
                chance = [["You inherit $100", 100],
                          ["It's your birthday: Collect $10 from every player", 10],
                          ["Bank pays you a dividend of $50", 50],
                          ["Hospital Fees: pay $100", -100],
                          ["Collect Stock dividend of $50", 50]]
                
               #Choose a card
                card = random.choice(chance)
                Draw.setFontSize(18)
                Draw.setColor(Draw.DARK_GREEN)
                Draw.string(("Player " + str(currentPlayer + 1) + \
                             " Landed on Chance: Press Enter To Pick A Card"), 10, 760)
                Draw.show()
                #Wait for player to choose
                waitForKey()   
                
                #Add value of card to player balance
                currentPlayerBalance += card[1] 
                
                #Special card case where player has to collect from the other player
                if card[0] == \
                   "It's your birthday: Collect $10 from every player": 
                    #deduct money from other player
                    players[1 - currentPlayer][1] -= card[1]
                    if 1 - currentPlayer == 0:
                        #Clear Old Balances
                        Draw.setColor(Draw.WHITE)
                        Draw.filledRect(750, 70, 250, 79)    
                        #New Balance
                        Draw.setFontSize(18)
                        Draw.setColor(Draw.RED)
                        Draw.string("Player 1:", 780, 70)
                        Draw.string("Balance: " + "$" + \
                                    str(players[1 - currentPlayer][1]),\
                                    780, 100)
                        Draw.string("Owned Properties: " + str(currentPlayerOwned), 770, 130)
                        
                        Draw.show()
                    #Display new balance for player 1
                    elif 1 - currentPlayer == 1: 
                        #Clear Old Balances
                        Draw.setColor(Draw.WHITE)
                        Draw.filledRect(750, 170, 250, 79)    
                        #New Balance
                        Draw.setFontSize(18)
                        Draw.setColor(Draw.BLUE)
                        Draw.string("Player 2:", 780, 170)
                        Draw.string("Balance: " + "$" + \
                                    str(players[1 - currentPlayer][1]),\
                                    780, 200)
                        Draw.string("Owned Properties: " + str(currentPlayerOwned), 770, 230)
                        Draw.show() 
                        
                #Text to display if money was added
                if card[1] > 0: 
                    clearUserInteraction()
                    Draw.setFontSize(18)
                    Draw.setColor(Draw.DARK_GREEN)
                    Draw.string("Player " + str(currentPlayer + 1) + " " + card[0]\
                                + ","  + " $" + str(card[1]) + " Has been added to your balance!", 10, 760) 
                    waitForKey()
               
                #Text to display if money was subtracted   
                elif card[1] < 0: 
                    clearUserInteraction()
                    Draw.setFontSize(18)
                    Draw.setColor(Draw.DARK_GREEN)
                    Draw.string("Player " + str(currentPlayer + 1) + " " + card[0]\
                                + ","  + " $" + str(abs(card[1])) + " Has been subtracted from your balance", 10, 760) 
                    Draw.show()
                    waitForKey()     
            
        #Save Changes                                         
        locations[players[currentPlayer][0]][3] = propertyOwner
        players[currentPlayer][1] = currentPlayerBalance 
        players[currentPlayer][2] = currentPlayerOwned 
        refreshBalances(Draw, currentPlayer, currentPlayerBalance, currentPlayerOwned)   
        reDrawScreen(Draw, locations, players) 
        currentPlayer = 1 - currentPlayer     
        Draw.show()
    Draw.clear()
   
    #Display Image of winner
    if  players[0][1] > 0: 
        #player 1
        Draw.setColor(Draw.GREEN)
        Draw.filledRect(185, 210, 385, 315)   
        Draw.setColor(Draw.BLUE)
        Draw.filledRect(195, 220, 365, 295)
        Draw.setFontSize(24)
        Draw.setColor(Draw.WHITE)
        Draw.string("Game Over:\n"+ "Player " + str(1) + " Wins!!!", 235, 240)
        Draw.show()
                 
    else: 
        #player 2
        Draw.setColor(Draw.GREEN)
        Draw.filledRect(185, 210, 385, 315)   
        Draw.setColor(Draw.BLUE)
        Draw.filledRect(195, 220, 365, 295)
        Draw.setFontSize(24)
        Draw.setColor(Draw.WHITE)
        Draw.string("Game Over:\n"+ "Player " + str(2) + " Wins!!!", 235, 240)  
        Draw.show()

      
def main():
    monopolyBoard()  

main()
