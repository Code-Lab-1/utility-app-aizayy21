#Vending Machine

Total_stock = [3,6,4,2,1]

#function to take money input from user
def money_input():
    money = int(input("Enter your amount: "))
    menu(money)

#function to show menu and get user response
def menu(money):
    print("**** Menu ****")
    print("1: Chocolate Chip: $20")
    print("2: Energy drink: $50")
    print("3: Chips: $30")
    print("4: Waterbottle: $40")
    print("5: Jelly: $5")

    item = int(input("Select your item by entering its code: "))
    if item == 1:
        balance(money, 20,item)
    elif item == 2:
        balance(money, 50,item)
    elif item == 3:
        print("elif")
        balance(money, 30,item)
    elif item == 4:
        balance(money, 40,item)
    elif item == 5:
        balance(money, 5,item)
    else:
        print("Enter valid item code")
        menu(money)

#Function to keep track for Stock left
def stock(id,items):
    print("stock")
    stock_present = True
    if items[id] == 0:
        stock_present = False
    else:
        items[id] = items[id] - 1
    return stock_present,items

#Function make transaction
def balance(money_in,purchase,item):
    #if balance is not enough
    if money_in < purchase:
        print("Your balance is low")

        #ask user to add more money
        add_more = input("Do you want to add more money[Y/N]: ")
        if add_more == "Y" or add_more == "y":
            money = int(input("enter amount: "))
            money = money_in + money
            menu(money)
        elif add_more == "N" or add_more == "n":
            print("Collect your Balance: $" + str(money_in))
        else:
            print("Enter Valid Choice")
            balance(money_in,purchase,item)
    #make transaction
    else:
        #Check if Stock is available
        present,left = stock(item-1,Total_stock)
        if present == True:
            print("Selected item Stock left: " + str(left[item-1]))
            bal = money_in - purchase
            print("Item with code {} is dispatched. Kindly collect it".format(item))
            print("You have ${} balance left".format(bal))

            #ask user if he wants to buy more items
            further = input("Do you want to buy any thing else[Y/N]: ")
            if further == "Y" or further =="y":
                menu(bal)
            else:
                return "Collect your Balance: $" + str(bal)
        # If stock is not available
        else:
            print("No items left for this code")
            another = input("Do you want to Select another Item [Y/N]: ")
            if another == "Y" or another == "y":
                menu(money_in)
            else:
                return "Collect your Balance: $" + str(money_in)
        
# Main driver function
def main():
    print("Welcome to our Vending Machine\n\n")
    money_input()

main()