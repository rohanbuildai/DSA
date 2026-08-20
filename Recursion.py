# count=0
# def increase():
#     global count
#     if count==7:
#         return
#     print(count)
#     count+=1
#     increase()

# increase()

#print name 5 times
# count=0
# def Name(name):
#       global count
#       if count>4:
#         return 
      
#       print(name)
#       count+=1

#       Name("rohan")

# Name("rohan")

#print linearly from 1 to n

def linearly(n):
   
    if n<1:
        return
    
    n-=1
    linearly(n)
    print(n)
    

    

linearly(200)