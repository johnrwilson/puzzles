#Define minimum number of coins 
#No matter how the coin array is arranged
def find_fewest_coins(coins, target):
    
    #Create variable to storage results 
    output = [0]*len(coins)
    
    #Define change left
    changeLeft = target
    
    while changeLeft>0:
        #Number of coins required for that ammount
        neededCoins=[changeLeft//i for i in coins]
        
        #Only if number of coins is positive
        RequiredCoins = [i for i in neededCoins if i>0]
        
        #How many of the biggest coin we require
        noBiggestCoin = min(RequiredCoins)
        
        #Retrieve coordinate
        biggestCoinIndex = neededCoins.index(noBiggestCoin)
        
        #Ammount paid in biggest coin
        Ammount = noBiggestCoin * coins[biggestCoinIndex]
        output[biggestCoinIndex] = noBiggestCoin
        
        #Whats left
        changeLeft = changeLeft-Ammount
        
    return(output)
