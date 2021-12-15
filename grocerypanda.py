#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Cynthia Vo,  Wendy Vo, Deepthi Vasudevan, Jerry Tseng
"""
from appJar import gui
import pandas
app=gui("Main Menu","500x500")


# Cynthia - Overall Integration
grocery = pandas.read_csv("grocery.csv")
veglist = list(grocery.Vegetables)
fruitlist = list(grocery.Fruits)
dairylist  = list(grocery.Dairy)



# Wendy - Greeting Function
def greet_user(greeting,sentinel,categoryq,readyq):
    canswer = ' '
    ranswer = sentinel
    print(greeting)
    while ranswer == 'n':
        ranswer = input(readyq)
    canswer = input(categoryq)
       
    if canswer == "Vegetables":
        vegetables("Welcome to our Vegetables section! Here are your choices:",veglist,"Which vegetables would you like or enter None? ")
    elif canswer == "Fruits":
        fruits("Welcome to our Fruits section!  Here are your choices:",fruitlist,"Which fruits would you like or enter None? ")
    elif canswer == "Dairy":
        dairy("Welcome to our Dairy section!  Here are your choices:",dairylist,"Which dairy products would you like or enter None? ")
    else:
        print('Sorry, we do not carry that category.  See you next time!')
    
# Cynthia - Vegetable Function
def  vegetables(greeting,selection,pick):
    print(greeting)
    for item in selection:
        print(item)
    vegpick = input(pick)
    if vegpick == "None":
        print("Goodbye")
    elif vegpick == "Broccoli":
        cashier("Broccoli",5,"You have added Broccolli!" )
<<<<<<< HEAD
        cashier("Broccoli",5,"You have added Broccoli!" )
=======
>>>>>>> c608ac1 (Update grocerypanda.py)
    elif vegpick == "Carrots":
        cashier("Carrots",6,"You have added Carrots!" )
    elif vegpick == "Tomatoes":
        cashier("Tomatoes",5,"You have added Tomatoes!" )
    else:
        print("Sorry, this isn't a choice.")

#Deepthi - Fruit Function
def fruits(greeting,selection,pick):
    print(greeting)
    for item in selection:
        print(item)
    frupick = input(pick)
    if frupick == "None":
        print("Goodbye")
    elif frupick == "Apples":
        cashier("Apple",5, "You have added Apples!" )
    elif frupick == "Bananas":
        cashier("Bananas",6,"You have added Bananas!" )
    elif frupick == "Cherries":
        cashier("Cherries",5,"You have added Cherries!" )
    else:
        print("Sorry, this isn't a choice.")
        

# Deepthi - Dairy Function
def dairy(greeting,selection,pick):
    print(greeting)
    for item in selection:
        print(item)
    dairypick = input(pick)
    if dairypick == "None":
        print("Goodbye")
    elif dairypick == "Cheese":
        cashier("Cheese",5,"You have added Cheese!" )
    elif dairypick == "Eggs":
        cashier("Eggs",6, "You have added Eggs!" )
    elif dairypick == "Milk":
        cashier("Milk",5,"You have added Milk!" )
    else:
        print("Sorry, this is isn't a choice.")

# Jerry - Cashier Function
def cashier(pickeditem, price, closing):
    print("Your cost for the", pickeditem, "will be $"+str(price))
    x = input("Would you like to buy another item? (y / n)")
    print('bye')
    if x == "y":
        greet_user("Great!", "n", "What other category would you like to browse? (fruit / dairy / vegetable)", "Ready to browse? (y / n)")
    else: 
        for i in closing:
            print(i)
    





#gui area
def press(btn):
    if btn == "Exit":
        app.stop()
    elif btn == "Greeting":
        greet_user("Welcome to our Online Supermarket!\n", "n", "Which grocery product category would you like to browse (Vegetables, Fruits, Dairy)? ", "Ready to browse (y/n)? ")
    elif btn == "Vegetables":
        vegetables("Welcome to our Vegetables section! Here are your choices:",veglist,"Which vegetables would you like? If you want to leave enter None ")
    elif btn == "Fruits":
          fruits()    
    elif btn == "Dairy":
          dairy()    
    elif btn == "Cashier":
        cashier('Enjoy your groceries!')      
    else:
        print('Pick a valid option')

app.addLabel("title", "Welcome to Team 28's Online Supermarket!")
app.setLabelBg("title", "green")


app.addImage("decor","snoopy-love.gif")
app.setFont(18)
        
#buttons
app.addButton("Greeting", press)
app.addButton("Vegetables", press)
app.addButton("Fruits", press)
app.addButton("Dairy", press)
app.addButton("Cashier", press)
app.addButton("Exit",press)


#displays gui
app.go() 
