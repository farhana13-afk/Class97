print("Can you use this platform?")

name = input("enter name")
age = int(input("enter age"))

if(age<10): 
    print("too young to use this platform")
else: 
    print("PERFECT AGE! continue with the questionare")
    color = input("enter favorite color ")

    if(color == "purple"):
        print("You have been accepted onto the platform.")
        gmail = input("enter gmail for congratulations letter")
    elif(color == "blue"):
        print("You have been accepted onto the platform.")
        gmail = input("enter gmail for congratulations letter")
    elif(color == "pink"):
        print("You have been accepted onto the platform.")
        gmail = input("enter gmail for congratulations letter")
    elif(color == "green"):
        print("You have been accepted onto the platform.")
        gmail = input("enter gmail for congratulations letter")
    elif(color == "red"):
        print("You have been accepted onto the platform.")
        gmail = input("enter gmail for congratulations letter")
    else:
        print("Application has been denied!")
        print("Try Again Another Day")
