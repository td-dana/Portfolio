# # #imports the ability to get a random number (we will learn more about this later!)
# from random import *
#
# #Create the list of words you want to choose from.
# aList = ["Sierra","Ahn Thu","Maria","Neerali","Helen","Ashna","Christina","Rosie","Reanna","Dana","Sonia","Melany","Amie","Cori","Cheyenne","Michelle","Betsy","Natalie","Era","Niralee","Audrey"]
# #Generates a random integer.
# aRandomIndex = randint(0, len(aList)-1)
# print(aList[aRandomIndex])


print("Your main course will be divided in to three meals...")
print("Here they AREEEEEEEE...")
from random import *
sushi = ["Sushi:CaliRoll","Sushi:PhillyRoll","Sushi:VeggieRoll"]
aRandomIndex = randint(0, len(sushi)-1)
print(sushi[aRandomIndex])

pizza = ["Pizza:Cheese","Pizza:Pepperoni","Pizza:HouseSpecial"]
aRandomIndex = randint(0, len(pizza)-1)
print(pizza[aRandomIndex])

sandwiches = ["Sandwich:Salami","Sandwhich:BLT","Sandwhich:Turkey"]
aRandomIndex = randint(0, len(sandwiches)-1)
print(sandwiches[aRandomIndex])

dessert = input("Are you ready for your dessert?")
dessert = ["CAKE","Cheesecake","Ice Cream"]
if "dessert" == "yes":
    aRandomIndex = randint(0, len(dessert)-1)
    print(dessert[aRandomIndex])
else:
    print("See you guys later then :)")
