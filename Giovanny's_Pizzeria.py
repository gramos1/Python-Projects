import os
from time import sleep
os.system("cls")
from random import randint

# menu dictionaries
ingredientsPrice = {
    "Mushrooms": 1.99,
    "Green Peppers": 0.99,
    "Anchovies": 2.99,
    "Tomatoes": 0.99,
    "Sausage": 2.99
}
pizzas = {
    "Thin Crust": 8.99,
    "Regular Crust": 10.99,
    "Deep Dish" : 14.99
}

print()
print("Welcome to Giovanny's Pizzeria".center(100, ' '))
print()
sleep(1)


print()
ing = input("Would you like to see our available pizza crusts and ingredients (y/n)? ")
ing = ing.strip().lower()
print()

if ing == "y":
    print("We offer the following prices for the ingredients:")
    sleep(1)

    # GOOD EXAMPLE ON HOW TO PRINT KEYS AND VALUES FROM A DICTIONARY
    for key, value in ingredientsPrice.items():
        print(key,value)

    sleep(1)
    print()
    print("And the prices for the pizza crusts are: ")
    for key, value in pizzas.items():
        print(key, value)
else:
    print("Ok, Bye!")
    sleep(2)
    quit()

# THESE VARIABLES ARE DECLARED ON THE GLOBAL SCOPE

total = [] # The total cost so far
request = [] # The requested pizza crust and ingredients.
toppings = 3 # The amount of toppings ou can add to the pizza. Global Scope
crust = None
orderNum = randint(1,100)

def CustomCrust(): # First function

    global total
    global request
    global crust
    print()
    crust = input("Which crust would you like? ")
    crust = crust.strip().title()
    print()

    if crust in pizzas:
        request = request + [crust]
        total.append(pizzas[crust]) # Appeding to total list
        tcost = sum(total)
        print("Ok, you want {}. ".format(crust))
        print("Your total is {} so far".format(tcost))
        print()
        crust = crust
        CustomIngredients()

    else:
        print()
        print("Sorry we don't have that crust, please choose something available.")
        print()
        sleep(2)
        CustomCrust()


def CustomIngredients(): # Second Function
    global total
    global request
    global crust
    global toppings

    while toppings != 0:
        top = input("Which ingredients would you like on your {} pizza? (Maximum of 3): ".format(crust))
        top = top.strip().title()
        
        if top in ingredientsPrice:
            toppings = toppings - 1
            print("Ok, {} has been added. You can add {} more.".format(top, toppings))
            print()
            request = request + [top]
            total.append(ingredientsPrice[top]) # Appending to total list
        else:
            print("Sorry we dont have that ingredient, please choose one from the menu")
            sleep(1)

    # End of While loop

CustomCrust() # Calling the first function
CustomIngredients() # Calling the second function

total_cost = "${:,.2f}".format(sum(total))
print(f"Ok so you want {request[1]}, {request[2]} and {request[3]} on a {request[0]} pizza.")
sleep(3)
print(f"The cost for the ingredients is ${str(sum(total[1:3]))} and the cost for the crust is ${str(total[0])} which brings the total cost to {total_cost}.")
print(f"Your order number is #00{orderNum}")
sleep(4)
print()
print("Making pizza.. please wait.".center(100, ' '))
sleep(7)
print()
print(f"Order #00{orderNum} is ready! ")
sleep(2)
print("Thank you for your business and enjoy your pizza!")
print()
input("Press Enter to quit: ")
exit



 



