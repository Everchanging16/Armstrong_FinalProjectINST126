#Final Project: 
#Checklist 6.2
#In this program, several things will happen, which is all done to intentioanlly satisfy the many advanced items on the checklist for this INST class. 
#So while early on there was some semblance of cohesion with this program that relied on some user interaction, later on it dives into more exploration of the 
#python language itself (which is all done to satisfy the checklist for this course). 
#A more in dept description about the program and what it does is available within the README.
#
import requests

import re
from bs4 import BeautifulSoup
import numpy as np 
import pandas as pd

import matplotlib.pyplot as plt

introduction = input("""Introduce yourself in this order: 
Name, Age, Favorite Color, Favorite food
""")
#checklist 7.1 used a string method to split a string into a list of smaller strings. 
#the split function is a built-in string method.
introlist = introduction.split()

print(introlist)
#Checklist 7.4 use regular exprssion to see a string matches certain pattern.
if re.match(r"[A-Z]", introlist[0]):
    print(True)


print("This creator of this program has a message:")

#checklist 7.2 used a backslash in a string to 'escape' a special character
print("\"Hello user! I hope you find this program to your liking :)\"")

history = input("Would you like the chance to look at a list of all recorded civilizations past and present? (Y/N): ")
#checklist 10.1 Found a simple web page and described what data you wanted to scrape from it
#get url
if history == "y".lower():
    print("\n")
    print("Note: This is a list of all documented civilizations (from Wikipedia) [https://en.wikipedia.org/wiki/Ancient_history])")
    civilization_page = requests.get("https://en.wikipedia.org/wiki/Ancient_history")
    #scrape website
    civilization_soup = BeautifulSoup(civilization_page.content, "html.parser") #checklist 10.2
    type(civilization_page)
    #10.1 I want to scrape the names of all ancient civilizations and people for the user to look at if they say yes
    #10.3 I went about scraping this webpage, by looking for the tables and rows, which should give me a long list of civilizations, when looking at 
    #the webpage in particular this list can be seen off to the side, and alot of this code has guided by similar code given during lecture, so recalling 
    #what that code was meant to do, I wanted to do something similar in mind for this. 
    civilization_table = civilization_soup.find("table")
    civilization_table
    civilization_th = civilization_table.find_all("th")
    civilization_th
    civilization_header = []
    for table in civilization_table:
        civilization_header.append(table.get_text().strip())
    header_string = ",".join(civilization_header)
    print(header_string)

    table_rows = civilization_table.find_all("tr")
    table_rows
    civilization_rows = [header_string]
    for row in table_rows:
        row_list = []
    #print(row)
        for cell in row.find_all("td"):
            cell_text = cell.get_text().strip()
            row_list.append(cell_text)
        row_string = ",".join(row_list)
        civilization_rows.append(row_string)
    print(header_string)

else:
    "Ignore this :)"
print("\n")


pythonquiz = input("Would you like to test you python knowledge? (Y/N): ")
if pythonquiz == "y".lower():
    #checklist 7.3
    rawstring = r"Python\nis\so\hard\to\figure\out"
    print("\nrawstring")
    print("""
          \n What causes the string to print out like this:
          a. raw string (r)
          b. backslash (\)
          c. split method (split())

          """)
    useranswer = input("Select any of the three answers: ")
    if useranswer == "a".lower():
        print("Congrats, you got that question right!")
    else:
        print("Sorry, looks like you got it wrong.")

print("\n")
#Checklist: 8.2
csvoption = input("Would you like to look at some famous locations from a readily available CSV file? (Y/N): ")
if csvoption == "y".lower():
    pathfile = input("Enter the location of the location.csv file that came with the folder for this program: ")
    pathfile
    path = pathfile.replace(r"\\", "/")
    print(path)
    data = pd.read_csv(path, index_col= "Location")
    print(data.head())
    #Checklist 8.3
    #Let's try to use booleans on to see which latitude of each popular location is greater than 0.
    print("Let's see which latitude of each popular location is greater than 0.")
    print(data['Latitude / Longitude'] > "0")


continue_check = input("press enter to continue: ")
if continue_check == "":
    "You have chosen to continue."
else:
    exit()

print("\n")

#Checklist: 8.1
print("\nHere's an ndarray being used to perform a vectorized computation")
print("The first array has the values [1,2,3]")
array1 = np.array([1, 2, 3])
print(array1)
print("While the second has values [5,6,7]")
array2 = np.array([5, 6, 7])
print(array2)
print("In usual instances, we would use a loop to add these values togther, but by using Numpy, we are able to avoid that all together.")
added_array = array1 + array2
print(added_array)

print("\n")

continue_check = input("press enter to continue: ")
if continue_check == "":
    "You have chosen to continue."
else:
    exit()

#Checklist: 8.4
print("Lets watch this data about some famous cars be changed into an CSV.")
#Checklist 5.15 create a dictionary manually
dict_famouscars = {
"Brand": ["Honda", "Mercedes", "Toyota", "Audi", "McLaren"],
"Model": ["Accord","W124", "FJ60", "Quattro", "F1"],
"Year": ["1976","1985", "1980", "1983", "1992"] }
#checklist 5.17 acess keys of a dictionary
dictkeys = dict_famouscars.keys()
print(dictkeys)
print(dict_famouscars)
dictioncsv = pd.DataFrame(dict_famouscars)
filecsv = input("Enter the location of the empty csv file that came with this program: ")
path = filecsv.replace(r"\\", "/")
dictioncsv.to_csv(path)

######
#Checklist 5.7: create list manually
newlist = ["Apple", "Banana", "Grape", "Kiwi", "Orange","Pineapple"]
print(newlist)
#Checklist 5.8: append item to a list.
newlist.append("Mango")
print(newlist)
#checklist 5.10 remove item from a list
newlist.remove("Banana")
print(newlist)


########
randomdict = ({"Apple": 10, "Grapes": 3, "Oranges": 7})
#checklist 5.18
[(key, value) for key, value in randomdict.items()]
#Checklist 5.19
testdictlist = ({"Apple": 20}, {"Mango": 3}, {"PineApple": 12})
for i in testdictlist:
    randomdict.update(i)
print(randomdict)

#####
#Checklist 5.12
newtuple = ("Sophia", "Tyler", "Jamie")
#checklist 5.13 (assigns each name to a individual variable, so x = "Sophia", etc.) 
(x,y,z) = newtuple
print(x)
print(y)
print(z)

#Checklist 5.14
def test():
    return 'Sophie', 22

a, b = test()
print(a)
print(b)