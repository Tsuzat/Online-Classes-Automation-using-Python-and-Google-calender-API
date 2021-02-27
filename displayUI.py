import time
import main

class style():

    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def menu():
    print(style.GREEN)
    print("\t\t*******************************************************************")
    time.sleep(0.075)
    print("\t\t*                         MENU                                    *")
    time.sleep(0.075)
    print("\t\t*******************************************************************")
    time.sleep(0.075)
    print("\t\t* Please select the task you want to perform                      *")
    time.sleep(0.075)
    print("\t\t*                                                                 *")
    time.sleep(0.075)
    print("\t\t*             1. Get today's schedule from google calender.       *")
    time.sleep(0.075)
    print("\t\t*             2. Add an event in your schedule locally.           *")
    time.sleep(0.075)
    print("\t\t*             3. Quick google calender events' automation         *")
    time.sleep(0.075)
    print("\t\t*             4. Generate a strong password                       *")
    time.sleep(0.075)
    print("\t\t*             5. Add an event in your google calender             *")
    time.sleep(0.075)
    print("\t\t*             6. Bug Report and Feedback                          *")
    time.sleep(0.075)
    print("\t\t*             7. Exit                                             *")
    time.sleep(0.075)
    print("\t\t*******************************************************************")
    time.sleep(0.1)
    print("\n\t--> ENTER YOUR CHOICE (1-7): ",end = " ")
    #print(style.RESET)

if __name__ == "__main__":
    pass