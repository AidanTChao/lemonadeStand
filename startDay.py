from customer_class import Customer
while True:
    try:
        def dayFunction(inventoryD, day, customers, price, recipe):
            if day < 7:
                day += 1
            else:
                if inventoryD["money"] >= 300:
                    print(f"Excelent job! you ended with: {inventoryD["lemons"]} lemon(s), {inventoryD["cupsOfIce"]} cup(s) of ice, {inventoryD["gramsOfSugar"]} gram(s) of sugar, and ${inventoryD["money"]}")
                    return -1
                else:
                    print("All of that work... for what? You didn't get the game. It's okay, you can try again next week.")
                    return -1
            
            print(f"--------------- DAY {day} ---------------")
            for x in range(10):
                customers.append(Customer())
            for customer in customers:
                attributes = customer.get_customer_attributes()
                customersBought = 0
                if attributes["price"] <= price:
                    if (attributes["sweetness"] == recipe["sugar"] and attributes["sweetness"] == recipe["lemons"]) or attributes["ice"] == recipe["ice"]:
                        print("You got a sale!")
                        customersBought += 1
                        # cupsOfLemonade -= 1
                        inventoryD["money"] += price
                        print(f"You made ${customersBought * price}")
            inventoryD["lemons"] = round(inventoryD["lemons"] / 2)
            inventoryD["cupsOfIce"] = round(inventoryD["cupsOfIce"] / 2)
            inventoryD["gramsOfSugar"] = round(inventoryD["gramsOfSugar"] / 2) 
            return day
    except ValueError, TypeError, ImportError:
        print("INVALID RESPONSE")
    else:
        break


# try:
#    int(input("eeeeeeeeeeeeeeeeeeeeeeeeeeeeee"))
# except ValueError:
#    print("Error")
     