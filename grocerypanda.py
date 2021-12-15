#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code I modified of our team's code to also allow the customer to have a receipt of what they bought and the overall cost. - Cynthia
@author: Cynthia Vo,  Wendy Vo, Deepthi Vasudevan, Jerry Tseng
"""
from appJar import gui
import pandas
app=gui("Main Menu","500x500")


# Cynthia - Overall Integration and added calculations
grocery = pandas.read_csv("grocery.csv")
veglist = list(grocery.Vegetables)
fruitlist = list(grocery.Fruits)
dairylist  = list(grocery.Dairy)
itemlist = []
itemprice = []
# Wendy - Greeting Function
def greet_user(greeting,sentinel,categoryq,readyq):
    canswer = ' '
    ranswer = sentinel
    print(greeting)
    while ranswer == 'n':
        ranswer = input(readyq)
    canswer = input(categoryq)
       
    if canswer == "Vegetables":
        vegetables("Welcome to our Vegetables section! Here are your choices:",veglist,"Which vegetables would you like? If you want to leave enter None  ")
    elif canswer == "Fruits":
        fruits("Welcome to our Fruits section!  Here are your choices:",fruitlist,"Which fruits would you like? If you want to leave enter None  ")
    elif canswer == "Dairy":
        dairy("Welcome to our Dairy section!  Here are your choices:",dairylist,"Which dairy would you like? If you want to leave enter None ")
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
        itemlist.append(vegpick)
        itemprice.append(5)
        cashier("Broccoli",5,"Enjoy your groceries!" )
        
    elif vegpick == "Carrots":
        itemlist.append(vegpick)
        itemprice.append(6)
        cashier("Carrots",6,"Enjoy your groceries!" )
    
    elif vegpick == "Tomatoes":
        itemlist.append(vegpick)
        itemprice.append(5)
        cashier("Tomatoes",5,"Enjoy your groceries!" )
        
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
        itemlist.append(frupick)
        itemprice.append(5)
        cashier("Apple",5, "Enjoy your groceries!" )
    elif frupick == "Bananas":
        itemlist.append(frupick)
        itemprice.append(5)
        cashier("Bananas",5,"Enjoy your groceries!" )
    elif frupick == "Cherries":
        itemlist.append(frupick)
        itemprice.append(4)
        cashier("Cherries",4,"Enjoy your groceries!" )
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
        itemlist.append(dairypick)
        itemprice.append(3)
        cashier("Cheese",3,"Enjoy your groceries!" )
    elif dairypick == "Eggs":
        itemlist.append(dairypick)
        itemprice.append(6)
        cashier("Eggs",6, "Enjoy your groceries!" )
        
    elif dairypick == "Milk":
        itemlist.append(dairypick)
        itemprice.append(5)
        cashier("Milk",5,"Enjoy your groceries!" )
    else:
        print("Sorry, this is isn't a choice.")

# Jerry - Cashier Function
def cashier(pickeditem, price, closing):
    print("Your cost for the", pickeditem, "will be $"+str(price))
    x = input("Would you like to buy another item? (y/n)")
    if x == "y":
        greet_user("Great!", "n", "Which grocery product category would you like to browse (Vegetables, Fruits, Dairy)?", "Ready to browse? (y/n)")
    else: 
        print('Here is your receipt: ')
        for i in itemlist:
            print('-'+i) 
        print('your total is $'+str(sum(itemprice)))
        print()
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
          fruits("Welcome to our Fruits section! Here are your choices:",fruitlist,"Which fruits would you like? If you want to leave enter None ") 
    elif btn == "Dairy":
          dairy("Welcome to our Dairy section! Here are your choices:", dairylist, "Which dairy items would you like? If you want to leave enter None ")
    elif btn == "Cashier":
        closing = 'Enjoy your groceries!'
        print('Here is your receipt: ')
        for i in itemlist:
            print('-'+i) 
        print('your total is $'+str(sum(itemprice)))
        print()
        for i in closing:
            print(i)
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
