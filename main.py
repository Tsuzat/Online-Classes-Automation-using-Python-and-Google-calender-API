import webbrowser
import os
import load_animation
import time
import sys
import commands
import displayUI

# System call
os.system("")

# for clearing the screen
def clrscr():
    
    if os.name =="nt": 
        os.system("cls") 
          
    # for linux / Mac OS 
    else: 
        os.system("clear") 

# Basic user commands associated with displayUI
def UsersCommand():
    
    command = input()
    if command == '1':
        clrscr()
        commands.runcommand1()
    
    elif command == '2':
        clrscr()
        commands.runcommand2()
    
    elif command == '3':
        clrscr()
        commands.runcommand3()
    
    elif command == '4':
        clrscr()
        commands.runcommand4()
    
    elif command == '5':
        clrscr()
        commands.runcommand5()

    elif command == '6':
        clrscr()
        commands.runcommand6()
    
    elif command == '7':
        clrscr()
        print('\033[31m')
        print("--> ALERT! EXITING WILL SHUT DOWN BACKGROUND AUTOMATION PROCESSES (if any process is running). YOU CAN MINIMISE THE WINDOW INSTEAD.")
        print('\033[32m')
        
        while True:
            
            inp = input("--> Exit anyway (y/n) : ")
            
            if inp in 'Yy': # exit anyway
                sys.exit()
                break
            
            elif inp in 'Nn': # Reload the menu
                load_animation.load_animation(load_this_str = " Loading Menu...",color = '\033[32m',load_time = 50)
                main()
            
            else:  # Unexpected command
                print('\033[31m')
                print('\t--> Unexpected user input')
                print('\033[32m')

    else: # adding some additional features 
        print('\033[31m')
        print('\t--> Unexpected user input')
        print('\033[32m')
        time.sleep(1)
        clrscr()
        main()


def WelcomeMessage(): # Will run just once.
    clrscr()
    print('\033[32m')

    print('''
        .----------------------. 
        |        WELCOME       |
        '----------------------'
                ^      (\_/)
                '----- (O.o)
                       (> <)
             
            Press ENTER to continue ''',end = ' ')
    input()
    load_animation.load_animation(load_this_str = "please wait, loading application.....",color = displayUI.style.CYAN, load_time= 25)
    os.system('cls')

def main():
    displayUI.menu()
    UsersCommand()

if __name__ == "__main__":
    WelcomeMessage()
    main()