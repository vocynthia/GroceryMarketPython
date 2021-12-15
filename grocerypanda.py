#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Cynthia Vo,  Wendy Vo, Deepthi Vasudevan, Cynthia Vo
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
def greet_user():
    print('bye')
    
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
    elif vegpick == "Carrots":
        cashier("Carrots",6,"You have added Carrots!" )
    elif vegpick == "Tomatoes":
        cashier("Tomatoes",5,"You have added Tomatoes!" )
    else:
        print("Sorry, this isn't a choice.")

#Deepthi - Fruit Function
def fruits():
    print('fruit')

# Deepthi - Dairy Function
def dairy():
    print('dairy)')

# Jerry - Cashier Function
def cashier():
    print('bye')





#gui area
def press(btn):
    if btn == "Exit":
        app.stop()
    elif btn == "Greeting":
        greet_user()
    elif btn == "Vegetables":
        vegetables("Welcome to our Vegetables section! Here are your choices:",veglist,"Which vegetables would you like? If you want to leave enter None ")
    elif btn == "Fruits":
          fruits()    
    elif btn == "Dairy":
          dairy()    
    elif btn == "Cashier":
        cashier()      
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
