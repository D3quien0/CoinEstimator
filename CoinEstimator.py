def coinPenny(x,y):
#penny weight    
    pennyWeight = 2.50
    pennyMass = 0.00551156
    pennyWrapper = 50
    if y == "g":
        numOfPennies = round(x / pennyWeight)
        print("You have about ", numOfPennies, " of pennies.")
        numOfWrappers = round(numOfPennies / pennyWrapper)
        print("You are able to fill ", numOfWrappers, " wrappers.")
        dollarAmount = .01 * numOfPennies
        print("Your dollar amount is: ", dollarAmount)
    elif y == "l":
        numOfPennies = round(x / pennyMass)
        print("You have about ", numOfPennies, " of pennies.")
        numOfWrappers = round(numOfPennies / dimeWrapper)
        print("You are able to fill ", numOfWrappers, " wrappers.")
        dollarAmount = .01 * numOfPennies
        print("Your dollar amount is: ", dollarAmount)
    return

def coinNickel(x,y):
#nickel weight    
    nickelWeight = 5
    nickelMass = 0.0110231
    nickelWrapper = 40
    if y == "g":
        numOfNickel = round(x / nickelWeight)
        print("You have about ", numOfNickel, " of nickels.")
        numOfWrappers = round(numOfNickel / nickelWrapper)
        print("You are able to fill ", numOfWrappers, " wrappers.")
        dollarAmount = .05 * numOfNickel
        print("Your dollar amount is: ", dollarAmount)
    elif y == "l":
        numOfNickel = round(x / nickelMass)
        print("You have about ", numOfNickel, " of nickels.")
        numOfWrappers = round(numOfNickel / nickelWrapper)
        print("You are able to fill ", numOfWrappers, " wrappers.")
        dollarAmount = .05 * numOfNickel
        print("Your dollar amount is: ", dollarAmount)
    return    
        
def coinDime(x,y):
#dime weight    
    dimeWeight = 2.268
    dimeMass = 0.0050000841
    dimeWrapper = 50
    if y == "g":
        numOfDime = round(x / dimeWeight)
        print("You have about ", numOfDime, " of dime.")
        numOfWrappers = round(numOfDime / dimeWrapper)
        print("You are able to fill ", numOfWrappers, " wrappers.")
        dollarAmount = .1 * numOfDime
        print("Your dollar amount is: ", dollarAmount)
    elif y == "l":
        numOfDime = round(x / dimeMass)
        print("You have about ", numOfDime, " of dime.")
        numOfWrappers = round(numOfDime / dimeWrapper)
        print("You are able to fill ", numOfWrappers, " wrappers.")
        dollarAmount = .1 * numOfDime
        print("Your dollar amount is: ", dollarAmount)
        
def coinQuarter(x,y):
#quarter weight
    quarterWeight = 5.67
    quarterMass = 0.01250021
    quarterWrapper = 40
    if y == "g":
        numOfQuarter = round(x / quarterWeight)
        print("You have about ", numOfQuarter, " of quarters.")
        numOfWrappers = round(numOfQuarter / quarterWrapper)
        print("You are able to fill ", numOfWrappers, " wrappers.")
        dollarAmount = .25 * numOfQuarter
        print("Your dollar amount is: ", dollarAmount)
    elif y == "l":
        numOfQuarter = round(x / quarterMass)
        print("You have about ", numOfQuarter, " of quarters.")
        numOfWrappers = round(numOfQuarter / quarterWrapper)
        print("You are able to fill ", numOfWrappers, " wrappers.")
        dollarAmount = .25 * numOfQuarter
        print("Your dollar amount is: ", dollarAmount)

decision = input("Would you like to use pounds(l) or grams(g): ")
print()
pennyAmount = float(input("How much do the pennies weigh: "))
coinPenny(pennyAmount,decision)
print()
nickelAmount = float(input("How much do the nickels weigh: "))
coinNickel(nickelAmount,decision)
print()
dimeAmount = float(input("How much do the dimes weigh: "))
coinDime(dimeAmount,decision)
print()
quarterAmount = float(input("How much do the quarters weigh: "))
coinQuarter(quarterAmount,decision)