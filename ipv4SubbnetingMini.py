#now make it the page for ipv4 practice
#this could be a nice app that can help kids when working on their studies

#"so lets start with a basic idea, this will start off as a terminal game but when i get back
# and can get the old terminal library from home PC i will spruce it up but for now lets start with the basic mechanics
# 
# 1. it will be rapid fire with a 1, 3, 5 minute timelimit and the goal will be to get the highscore"
# 2. actually make it a combo system with ascii art and all the fun stuff, idk if it would work on linux since i use flush for the 
# animation#

#lets start with the basic inputs needed

#NOW ITS TIME TO ADD A SCORE COUNTER AND A TIMER INSTEAD OF A SINGLE THING
#next is to add a time and have timers be diffrent depennding on how the user wants things to go down


import random as rdm
import methodMadness as mad
import time
import collections

# the dictionary that is meant for the 
#subs and hosts in the system
#also find a way to make this an SQL table as to make my life easier when working with datas


#now to add it to a function / def as to be able to more easily sort it in the main menu and when i add more stuff
#create a clas that will then in further use the obj's in the thing, eh remember to do that later
class menu():
    print("piss")

def prefix():
    sub_hosts = {
    "255.255.0.0": "16",
    "255.255.128": "17",
    "255.255.192.0": "18",
    "255.255.224.0": "19",
    "255.255.240.0": "20",
    "255.255.248.0": "21",
    "255.255.252.0": "22",
    "255.255.254.0": "23",
    "255.255.255.0" : "24",
    "255.255.255.128": "25",
    "255.255.255.192": "26",
    "255.255.255.224": "27",
    "255.255.255.240": "28",
    "255.255.255.248": "29",
    "255.255.255.252" : "30"}

    counter = 0
    restart = "yes"
    while restart != "no":
        #now that we have the restart ill do a basic what is the subnet for 255.255.255.0
        #the answer will be /24 and if the answer is not either 24 or /24 then it  will return an error and nothing will be added to the points system
        random_sub = (rdm.choice(list(sub_hosts)))
        #how about get the key and from there get the following value
        mad.textCrawlNoWait(random_sub)
        prefix = sub_hosts.get(random_sub)
        answer = input("\n")
        
        while answer != prefix:
            mad.textCrawlNoWait("try again\n") 
            answer = input()
        if answer == prefix:
            counter += 1 
            mad.textCrawlNoWait(f"CORRECT! : {counter}\n")
            
        mad.textCrawlNoWait("would you like to try again? yes / no\n")
        restart = input()

def hosts():
    sub_Hosts = {
    "255.255.0.0": "65,534",
    "255.255.128": "32,766",
    "255.255.192.0": "16,382",
    "255.255.224.0": "8,190",
    "255.255.240.0": "4,094",
    "255.255.248.0": "2,046",
    "255.255.252.0": "1,022",
    "255.255.254.0": "510",
    "255.255.255.0" : "254",
    "255.255.255.128": "126",
    "255.255.255.192": "62",
    "255.255.255.224": "30",
    "255.255.255.240": "14",
    "255.255.255.248": "6",
    "255.255.255.252" : "2"}
    
    counter = 0
    restart = "yes"
    while restart != "no":
        #now that we have the restart ill do a basic what is the subnet for 255.255.255.0
        #the answer will be /24 and if the answer is not either 24 or /24 then it  will return an error and nothing will be added to the points system
        random_Host = (rdm.choice(list(sub_Hosts)))
        #how about get the key and from there get the following value
        mad.textCrawlNoWait(random_Host)
        prefix = sub_Hosts.get(random_Host)
        answer = input("\n")
        
        while answer != prefix:
            mad.textCrawlNoWait("try again\n") 
            answer = input()
        if answer == prefix:
            counter += 1 
            mad.textCrawlNoWait(f"CORRECT! : {counter}\n")
            
        mad.textCrawlNoWait("would you like to try again? yes / no\n")
        restart = input()
#alright got the basics down now time to make tables that ask for a subnet and then are required to get the prefix,
# in the future potentially add how many hosts it can have
#pretty sure 254 is the max for 255.255.255.0 subnets

#alright so 2 tuples or or maybe 2d arrays with the subnett and the coresponding answer

#get a random subnet, this will be done by getting a random number, and making sure its an odd number as to maintain the