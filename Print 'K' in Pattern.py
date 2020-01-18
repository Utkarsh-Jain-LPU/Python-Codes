result=''
for i in range(0,7):
    for j in range(0,5):
        if(j==0 or i+j==4 or i==j+2):
            result=result+'*'
        else:
            result=result+' '
    result=result+'\n'
print(result)    
