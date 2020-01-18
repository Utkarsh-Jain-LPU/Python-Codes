a=input("Enter a String = ")
for i in range(0,len(a)+1):
    for j in range(0,i):
        print(a[j],end=' ')
    print("\n")    
