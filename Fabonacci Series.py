x=0
y=1
print(x,y,end=' ')
for i in range(2,50):
    x,y=y,x+y
    print(y,end=' ')
