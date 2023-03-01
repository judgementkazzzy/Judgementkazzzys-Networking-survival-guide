import time
import sys
import random

def textCrawl(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        #modded to make it easier to read, should have a way to mod the speed tbh
        #welp another feature that had to be scraped bc of time restraits, really should in my free time mess around with some of the features or even just do some basic bug fixing
        # if keyboard.is_pressed("spacebar"):
        #     time.sleep(.00001)
        # if keyboard.is_pressed("c"):
        #     time.sleep(0)
        # else:
        time.sleep(.03)
    #if i still have this commented its just for debuging purposes and should be uncommented
    time.sleep(1.5)

# #more so for debuging and or if the dialog needs to move at a slower pace
#nvm didnt work just make a custom one or mod the og for now dont have time to mess around with it
# def textCrawlTime(text, time):
#     for char in text:
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         #modded to make it easier to read, should have a way to mod the speed tbh
#         time.sleep(time/100)
#     #if i still have this commented its just for debuging purposes and should be uncommented
#     time.sleep(2)

def textCrawlNoWait(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.01)

#get the number that the damage is and from there roll a dice thats that large to get the damage value        
def diceRoll(n):
    if n == 1:
        return 1
    else:
        return random.randrange(1,n)
    
    
# will have to return to this idea but for now back to the old method        
# def read(text):
#     f = open(f'{text}', 'r')
#     file_contents = f.read()
#     textCrawl(file_contents)
#     f.close

#this is more just a template, if just wanted to make it a method to look cool and maybe figure out how to get a more proper one working sometime
def dialogMenu(n):
    if n == '1':
        print("h")
    if n == '2':
        print("h")
    if n == '3':
        print("h")
    if n == '4':
        print("h")
        
#"gameover method, this will do 2 things, 1. its will check if the player still has over 0 hp and if yes it will print the health remaining as well as 
# an URGENT HEALTH LOW message if the total health pool is low
# 2. to give a game over and from there ask the player to restart from checkpoint or quit"

#health is just the health value and text is the text that will appear if the player dies at this check
def gameOver(health, text):
    if health <= 0:
        textCrawl(text)
        textCrawlNoWait("   _____          __  __ ______    ______      ________ _____  \n")
        textCrawlNoWait("  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ \n")
        textCrawlNoWait(" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |\n")
        textCrawlNoWait(" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / \n")
        textCrawlNoWait(" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ \n")
        textCrawlNoWait("  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ \n")
        sys.exit()