#this will be a test counter before i put it in the main page

#an if statement that will check if the correct value is there

answer = input()
prefix = "1"
counter = 0

while True:
    print("try again") 
    answer = input()
    if answer == prefix:
        print(f"CORRECT! {counter}")
        counter += 1
        print(f"CORRECT! {counter}")
        
