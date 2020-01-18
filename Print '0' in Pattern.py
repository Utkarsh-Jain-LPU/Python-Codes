result=''
for i in range(0,7):
    for j in range(0,5):
        if((i>0 and i<6) and (j>0 and j<4)):
            result=result+' '
        else:
            result=result+'*'
    result=result+'\n'
print(result)
