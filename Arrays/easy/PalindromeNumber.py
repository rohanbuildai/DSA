def palindromenumber(x):

    if int(str(x)[::-1])==x:
        return True
    else:
        return False
    
print(palindromenumber(1333331))