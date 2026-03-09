def shopFunction(inventoryD, shopF):
    while True:
        try:
            shop = shopF()
            if shop == 1:
                howManyLemons = int(input("How many lemons do you want to buy? "))
                if howManyLemons <= inventoryD['money']:
                    howManyLemonsClarify = input("Are you sure you want to buy that many? It will cost $"+ str(round(howManyLemons * 1.5))+ ". ")
                    if howManyLemonsClarify.lower() == "yes":
                        inventoryD['lemons'] += howManyLemons
                        inventoryD['money'] -= round(howManyLemons * 1.5)
                    else:
                        inventoryD["lemons"] = inventoryD["lemons"]
                        inventoryD["money"] = inventoryD["money"]
                        
            elif shop == 2:
                howManyIce = int(input("How many cups of ice do you want to buy?"))
                if howManyIce <= inventoryD['money']:
                    howManyIceClarify = input("Are you sure you want to buy that many? It will cost $"+ str(round(howManyIce * 0.75))+ ". ")
                    if howManyIceClarify.lower() == "yes":
                        inventoryD['cupsOfIce'] += howManyIce
                        inventoryD['money'] -= round(howManyIce * 0.75)
                    else:
                        inventoryD["cupsOfIce"] = inventoryD["cupsOfIce"]
                        inventoryD["money"] = inventoryD["money"]
            elif shop == 3:
                howManySugar = int(input("How many grams of sugar do you want to buy? "))
                if howManySugar <= inventoryD['money']:
                    howManySugarClarify = input("Are you sure you want to buy that many? It will cost $"+ str(round(howManySugar * 0.05))+ ". ")
                    if howManySugarClarify.lower() == "yes":
                        inventoryD['gramsOfSugar'] += howManySugar
                        inventoryD['money'] -= round(howManySugar * 0.05)
                    else:
                        inventoryD["lemons"] = inventoryD["lemons"]
                        inventoryD["money"] = inventoryD["money"]
                else:
                    print("Sorry, you don't have enough money.")
        except ValueError, TypeError, ImportError:
            print("INVALID RESPONSE")
        else:
            break
