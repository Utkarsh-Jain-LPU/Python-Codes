i=0
while(i>=0):
    password=input("Enter Password = ")
    i=i+1
    if(password=="qwerty"):
        print("You are Successfully logged in.")
        break
    elif(i<=2):
        print("...Wrong Password... Try Again..")
    else:
        print("You have been Denied Access...")
        break
