result=''
for i in range(0,7):
    for j in range(0,5):
        if((i==1 or i==2 or i==4 or i==5 or i==6)and(j>0)):
            result=result+' '
        else:
            result=result+'*'
    result=result+'\n'
print(result)     
