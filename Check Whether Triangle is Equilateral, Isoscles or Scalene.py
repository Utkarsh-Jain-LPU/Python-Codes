a=int(input("Enter value of a = "))
b=int(input("Enter value of b = "))
c=int(input("Enter value of c = "))
if(a==b==c):
    print('Equilateral')
elif(a==b or b==c or a==c):
    print('Isoscles')
else:
    print('Scalene')
