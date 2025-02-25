#do not Modify any code in Main in any way shape or form

import gMenu

mainMenuOptions = ("mens","womens","boys","girls","exit")

#Numerical Menu
print("Department store menu Numerical Options \n")
choice = gMenu.getMenuNumber(mainMenuOptions)
print ("Your choice returned the value:", choice)

if choice == "mens":print("You are in the Mens Department")
elif choice == "womens": print("You are in the Womens Department")
elif choice == "boys": print("You are in the Boys Department")
elif choice == "grils": print("You are in the Girls Department")
elif choice == "exit": print("Have a wonderful day")

# Capital Letter Menu
print('\n')
print("Department store menu Capital Letter Options \n")
choice = gMenu.getMenuCapLetters(mainMenuOptions)

print ("Your choice returned the value:", choice)

if choice == "mens":print("You are in the Mens Department")
elif choice == "womens": print("You are in the Womens Department")
elif choice == "boys": print("You are in the Boys Department")
elif choice == "girls": print("You are in the Girls Department")
elif choice == "exit": print("Have a wonderful day")




#Custom Letter Menu
print("\n")
print("Department store menu Custom Options \n")
choice = gMenu.getMenuCustomLetters(mainMenuOptions)
print ("Your choice returned the value:", choice,"\n")

if choice == "mens":print("You are in the Mens Department")
elif choice == "womens": print("You are in the Womens Department")
elif choice == "boys": print("You are in the Boys Department")
elif choice == "girls": print("You are in the Girls Department")
elif choice == "exit": print("Have a wonderful day")
