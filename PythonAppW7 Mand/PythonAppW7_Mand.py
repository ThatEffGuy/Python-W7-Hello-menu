#import libs
import os

#declare variables
menuChoice = 0
name = ""

#define method/proced/func
def clearScreen():
    os.system("cls") #clears screen
    return
#end clear screen


def english(name):
    clearScreen()
    print("Hello", name)
    print("press return to return to menu")
    input()		  
    return

def french(name):
    clearScreen() 
    print("Bonjour", name)
    print("press return to return to menu")
    input()		  
    return        	
#end french

def italian(name):
    clearScreen()
    print("Ciao,", name)
    print("press return to return to menu")
    input()		  
    return        
#end italian

def german(name):
    clearScreen()
    print("Hallo", name)
    print("press return to return to menu")
    input()		  
    return        	
#end german

def exit():
	print("Goodbye, Au Revoir, Arrivederci (Ciao), Auf Wiedersehen") 
	print("Exiting..... Press return to Exit")
	input()
	return       	

def menu():
    print ("Hello in different languages")
    print ("1.  English   ")
    print ("2.  French    ")
    print ("3.  Italian   ")
    print ("4.  German    ")
    print ("5.  Exit      ")
    return
#finish menu


#main program code
name = input("Enter your name: ")
while menuChoice != 5:
    clearScreen()
    menu()
    menuChoice = int(input("Enter Choice : "))

    if menuChoice == 1:
        english(name)
    elif menuChoice == 2:
        french(name)
    elif menuChoice == 3:
        italian(name)
    elif menuChoice == 4:
        german(name)
    else:
        exit()
    #end if
#end while