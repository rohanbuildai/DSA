def plusone(digits):
    n=len(digits)
    carry=0

    i=n-1

    while(i>=0):
        if digits[i]==9:
            digits[i]=0
            carry=1
            i-=1
        elif digits[i]<9:
            digits[i]+=1
            carry=0
            return digits
    new_array=[0]*(n+1)
    new_array[0]=carry
    return new_array
                                                                                                    

print(plusone([1,2,3]))          