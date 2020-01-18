a=input("Enter your Phone No. = ")
length=len(a)
if(length==10 and a[0]!='0' and a.isdigit()):
    print("Valid Phone Number...")
else:
    print("Invalid Phone Number...")
