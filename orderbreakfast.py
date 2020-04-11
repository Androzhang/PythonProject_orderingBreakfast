
[V2]
import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print_pause("Sorry, I don't understand.")

def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")

def get_order():
    response = valid_input("Please place your order. Would you like waffles or pancakes?\n", ["waffles", "pancakes"])
    if "waffles" in response:
        print_pause("Waffles it is!")  
    elif "pancakes" in response: 
        print_pause("Pancakes it is!")
    print_pause("Your order will be ready shortly.")
    order_again()

def order_again():
    response2 = valid_input("Would you like to place another order? Please say 'yes' or 'no'.\n", ["no", "yes"])
    if "no" in response2:
        print_pause("OK, goodbye!")
    elif "yes" in response2:
        print_pause("Very good, I'm happy to take another order.")
        get_order()

def order_breakfast():
    intro()
    get_order()
       
order_breakfast()


————————————————————————————————————————————————————————————————————————
[V1]
import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)
    
print_pause("Hello! I am Bob, the Breakfast Bot.")
print_pause("Today we have two breakfasts available.")
print_pause("The first is waffles with strawberries and whipped cream.")
print_pause("The second is sweet potato pancakes with butter and syrup.")


while True:
    while True:
        response = input("Please place your order. "
                         "Would you like waffles or pancakes?\n").lower()
        if "waffles" in response:
            print_pause("Waffles it is!")
            break
        elif "pancakes" in response:
            print_pause("Pancakes it is!")
            break
        else:
            print_pause("Sorry, I don't understand.")
    print_pause("Your order will be ready shortly.")
    while True:
        order_again = input("Would you like to place another order? "
                            "Please say 'yes' or 'no'.\n").lower()
        if "no" in order_again:
            print_pause("OK, goodbye!")
            break
        elif "yes" in order_again:
            print_pause("Very good, I'm happy to take another order.")
            break
        else:
            print_pause("Sorry, I don't understand.")
    if "no" in order_again:
        break
