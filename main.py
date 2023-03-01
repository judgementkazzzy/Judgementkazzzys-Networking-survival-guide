#create a menu that can be traveresed by the users
#theyre tech nerds so who cares about UI

#"TODO:
# 1. add a saving feature to make sure we can keep track of highscores and add the notes eventually
# from the class and from other sources when reading
# 2. add a proper menu via the terminal because were programmers and it looks cooler, plus i dont need to make a GUI
# 3. "

import methodMadness as mad
import ipv4SubbnetingMini as ipv4

def main():
    
    #gonna have to make another while loop but for now just check for the 1 option is pressed
    #be sure to add a "are you sure?" option when doing this 
    
    mad.textCrawl("Networking Study Aid V.01\n")
    mad.textCrawlNoWait("1. IPV4 Subneting practice\n")
    mad.textCrawlNoWait("2. use\n")
    mad.textCrawlNoWait("3. inventory\n")
    mad.textCrawlNoWait("4. command\n")
    playerchoice = input()
    
    if playerchoice == '1':
        ipv4.prefix()
    

if __name__ == "__main__":
    main()