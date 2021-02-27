import checkconnection
import check_user_and_get_data
import main
import timeAndDate
import os
import time
import json
import threading
import load_animation
import Automation
import Password_Generator
import webbrowser

# this function fetches data from google calender API. For details check 
def runcommand1():

    if checkconnection.is_connected():
        user_data = check_user_and_get_data.CheckUser() # Storing an instance of fetched calendar data
        
        if len(user_data)==0:
            print("\t--> We found nothing from google calender server. You got a free day, I guess ;)") 
        
        if len(user_data)>0:
            id = 1
            print('\n----------------------------------------------------------------')
            for data in user_data:
                print()
                print(f"--> ID={id} => MEETING: {data['summary']}; FROM: {data['start_time']} TO: {data['end_time']}")
                id += 1
            print('\n----------------------------------------------------------------\n')
        
        # Asking to user if they want to add more events
        while True:

            s = input('\n--> Do you want to add any event(s) manually? (y/n): ')
            
            if s in 'Yy':
                try:
                    n = int(input("\n\t--> How many new events you want to add? : "))
                    for i in range(n):
                        start_time = input("\n\t--> Start time? (enter something like; 7 PM or 8 PM)  ")
                        duration = input("\t--> Duration? (In hh:mm formate, e.g. 01:30, 01:00)  ").split(':')
                        summary = input("\t--> What is this event about? ")
                        url = input("\t--> Related link (Please provide just 1): ")
                        user_data.append(timeAndDate.create_event(start_time, summary,int(duration[0]),int(duration[1]),url))
                    
                    id = 1
                    print('\n----------------------------------------------------------------')
                    print("\n--> NEW EVENT(S) HAS/HAVE BEEN ADDED")
                    for data in user_data:
                        
                        print(f"\t--> ID={id} => MEETING: {data['summary']}; FROM: {data['start_time']} TO: {data['end_time']}")
                        id += 1
                    print('\n----------------------------------------------------------------')
                    
                    break

                except IndexError:
                    print('\033[31m')
                    print('\t--> Unexpected user input')
                    print('\033[0m')
                
                except ValueError:
                    print('\033[31m')
                    print('\t--> Unexpected user input')
                    print('\033[0m')
                
            elif s in 'nN':
                break
            
            else:
                print('\033[31m')
                print('\t--> Unexpected user input')
                print('\033[0m')

        # Asking user if they want to delete events        

        while True and len(user_data)>0:

            s = input("\n--> Do you want to delete event(s)? (y/n): ")
            
            if s in 'Yy':
                
                try:
                    n = list(map(int,input("\t--> Enter ID(s) number with single space (e.g. 1 2 4 or 2): ").strip().split()))
                    for i in range(len(user_data)):
                        if i in n:
                            del user_data[i-1]
                    
                    id = 1
                    print('\n----------------------------------------------------------------')
                    print("\n--> REQUESTED EVENT(S) IS/ARE DELETED")
                    for data in user_data:
                        
                        print(f"\t--> ID={id} => MEETING: {data['summary']}; FROM: {data['start_time']} TO: {data['end_time']}")
                        id += 1
                    print('\n----------------------------------------------------------------')
                
                    break

                except IndexError:
                    print('\033[31m')
                    print('\t--> Unexpected user input')
                    print('\033[0m')
                
                except ValueError:
                    print('\033[31m')
                    print('\t--> Unexpected user input')
                    print('\033[0m')

            elif s in 'nN':
                break

            else:
                print('\033[31m')
                print('\t--> Unexpected user input')
                print('\033[0m')
        
        #sorting the event data start time wise
        user_data.sort(key=lambda x: x['start_time'].split(':')[0]*3600 + x['start_time'].split(':')[1]*60 + x['start_time'].split(':')[2])

        #storing the data in json file
        with open('events_today.json','w') as f:
            json.dump(user_data,f,indent=2)

        # Asking if user want to initiate automation
        while True:

            choice = input("--> Start events' automation? (y/n): ")

            if choice in 'Yy':

                thread = threading.Thread(target=Automation.events_automation) #making a thread
                thread.start() #running the tread
                print(" AUTOMATION STARTED SUCCESSFULLY.")
                # Loading menu back
                load_animation.load_animation(load_this_str = " Loading Menu...",color = '\033[37m',load_time = 50)
                main.main()
                break

            elif choice in 'Nn':

                load_animation.load_animation(load_this_str = " Loading Menu...",color = '\033[37m',load_time = 50)
                main.main()
                break

            else:
                print('\033[31m')
                print('\t--> Unexpected user input')
                print('\033[0m')

    else: # if there is no internet connection detected

        print('\033[31m')
        print("--> Unable to connect. Please check you connection. Redirecting to menu in 5 seconds.")
        time.sleep(5)
        print('\033[0m')
        os.system('cls')
        main.main()

################################################################################################################################

# adds and deletes events locally. 
def runcommand2():

    user_data = [] #Data structure
    while True:
            
        try:
            
            n = int(input("\n\t--> How many new events you want to add? : "))
            
            for i in range(n):
                
                start_time = input("\n\t--> Start time? (enter something like; 7 PM or 8 PM)  ")
                duration = input("\t--> Duration? (In hh:mm formate, e.g. 01:30, 01:00)  ").split(':')
                summary = input("\t--> What is this event about? ")
                url = input("\t--> Related link (Please provide just 1): ")
                user_data.append(timeAndDate.create_event(start_time, summary,int(duration[0]),int(duration[1]),url))
                    
            id = 1
            print('\n----------------------------------------------------------------')
            print("\n--> NEW EVENT(S) HAS/HAVE BEEN ADDED")
            for data in user_data:
                        
                print(f"\t--> ID={id} => MEETING: {data['summary']}; FROM: {data['start_time']} TO: {data['end_time']}")
                id += 1
            print('\n----------------------------------------------------------------')
                    
            break

        except IndexError:
            print('\033[31m')
            print('\t--> Unexpected user input')
            print('\033[0m')
                
        except ValueError:
            print('\033[31m')
            print('\t--> Unexpected user input')
            print('\033[0m')
                

    while True:

        s = input("\n--> Do you want to delete event(s)? (y/n): ")
            
        if s in 'Yy':
                
            try:
                n = list(map(int,input("\t--> Enter ID(s) number with single space (e.g. 1 2 4 or 2): ").strip().split()))
                for i in range(len(user_data)):
                    if i in n:
                        del user_data[i-1]
                    
                id = 1
                print('\n----------------------------------------------------------------')
                print("\n--> REQUESTED EVENT(S) IS/ARE DELETED")
                for data in user_data:
                    print(f"\t--> ID={id} => MEETING: {data['summary']}; FROM: {data['start_time']} TO: {data['end_time']}")
                    id += 1
                
                print('\n----------------------------------------------------------------')
                
                break

            except IndexError:
                print('\033[31m')
                print('\t--> Unexpected user input')
                print('\033[0m')
                
            except ValueError:
                print('\033[31m')
                print('\t--> Unexpected user input')
                print('\033[0m')

        elif s in 'nN':
            break

        else:
            print('\033[31m')
            print('\t--> Unexpected user input')
            print('\033[0m')    
        
        
    user_data.sort(key=lambda x: x['start_time'].split(':')[0]*3600 + x['start_time'].split(':')[1]*60 + x['start_time'].split(':')[2])

    with open('events_today.json','w') as f:
        json.dump(user_data,f,indent=2)

    while True:

        choice = input("--> Start events' automation? (y/n): ")

        if choice in 'Yy':

            thread = threading.Thread(target=Automation.events_automation)
            thread.start()
            print(" AUTOMATION STARTED SUCCESSFULLY.")
            load_animation.load_animation(load_this_str = " Loading Menu...",color = '\033[37m',load_time = 50)
            main.main()   
            break

        elif choice in 'Nn':

            load_animation.load_animation(load_this_str = " Loading Menu...",color = '\033[37m',load_time = 50)
            main.main()
            break

        else:
            print('\033[31m')
            print('\t--> Unexpected user input')
            print('\033[0m')
##########################################################################################################################

def runcommand3():

    # Fetch google calneder and automate it.
    if checkconnection.is_connected():
        user_data = check_user_and_get_data.CheckUser()
        
        if user_data == None:
            print("\t--> We found nothing from google calender server. You got a free day, I guess ;)")
            time.sleep(2) 
            load_animation.load_animation(load_this_str = " Loading Menu...",color = '\033[37m',load_time = 50)
            main.main()


        elif user_data != None:
            id = 1
            print('\n----------------------------------------------------------------')
            for data in user_data:
                print()
                print(f"--> ID={id} => MEETING: {data['summary']}; FROM: {data['start_time']} TO: {data['end_time']}")
                id += 1
            print('\n----------------------------------------------------------------\n')

            user_data.sort(key=lambda x: x['start_time'].split(':')[0]*3600 + x['start_time'].split(':')[1]*60 + x['start_time'].split(':')[2])

            with open('events_today.json','w') as f:
                json.dump(user_data,f,indent=2)
            
            thread = threading.Thread(target=Automation.events_automation)
            thread.start()
            print(" AUTOMATION STARTED SUCCESSFULLY.")
            time.sleep(2)
            load_animation.load_animation(load_this_str = " Loading Menu...",color = '\033[37m',load_time = 50)
            main.main()   

    else: # if there is no internet connection 

        print('\033[31m')
        print("--> Unable to connect. Please check you connection. Redirecting to menu in 5 seconds.")
        time.sleep(5)
        print('\033[0m')
        os.system('cls')
        main.main()

#######################################################################################################################

def runcommand4():

    choicesBoolean = [True,True,True,True] # Default is 'all True'
	        
    Choices = ["Uppercase letters","Lowercase letters","Numbers","Special Characters"]
    
    while True:

        try:
            n = int(input("\n--> Enter the length of password you want to generate (recommended >10): "))
            break

        except ValueError:
            print('\033[31m')
            print('\t--> Unexpected user input')
            print('\033[0m')

    while True:


        choice = input("--> Do you want to change default setting ? (y/n): ")

        if choice in 'nN':
            print("--> Using default setting.")
            break
        
        elif choice in 'Yy':
            
            print("--> You must choose at least two of them, 'Uppercase letters, Lowercase letters, Numbers, Special Characters'.\n")
            
            for i in range(4):
                
                while True:
                    a = input(f"\t--> Do you want {Choices[i]} in it? (y/n): ")
                    if a in 'yY':
                        break
                    elif a in 'Nn':
                        choicesBoolean[i] = False
                        break
                    else:
                        print('\033[31m')
                        print('\t--> Unexpected user input')
                        print('\033[0m')
                if choicesBoolean.count(False) == 2:
                    break
            break

        else:
            print('\033[31m')
            print('\t--> Unexpected user input')
            print('\033[0m')

    Password = Password_Generator.GeneratePassword(n,*choicesBoolean)
    Automation.show_notification("Passwrd Generated", "Passwrd Generated and copied in your clipboard.")
    time.sleep(2)
    load_animation.load_animation(load_this_str = " Loading Menu...",color = '\033[37m',load_time = 50)
    main.main()   

#########################################################################################################################

def runcommand5():

    print("\n--> This area is still in under development. I recommend you to add/delete events via official google calender website. Opening website...")
    time.sleep(3)
    webbrowser.open("https://calendar.google.com/")
    load_animation.load_animation(load_this_str = " Loading Menu...",color = '\033[37m',load_time = 50)
    main.main()

def runcommand6():

    print("\n-->I really appreciate you for helping me to make this application better. You can report bugs or give us a feedback")
    time.sleep(3)
    webbrowser.open('https://forms.gle/mXW7eg1TvjbRVHJp8')
    webbrowser.open('https://github.com/Tsuzat/Online-Classes-Automation-using-Python-and-Google-calender-API/issues')
    load_animation.load_animation(load_this_str = " Loading Menu...",color = '\033[37m',load_time = 50)
    main.main()

if __name__ == "__main__":
    pass