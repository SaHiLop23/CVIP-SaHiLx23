def sum(x,y):
    return x+y 
def min(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x % y
def per(x,y):
    return x/y*100

print("Enter Number of arithmetic symbol")
print(" a Addition \n b Subtraction \n c Multiply \n d Divide \n e Module \n f Percentage")

choice = input("Please enter choice (a/ b/ c/ d/ e/ f): ")    
    
x=int (input ("Please enter the first number: "))    
y=int (input ("Please enter the second number: "))    
    
if choice == 'a':    
   print (x, " + ",y, " = ", sum(x,y))     
elif choice == 'b':    
   print (x, " - ", y, " = ", min(x,y))     
elif choice == 'c':    
   print (x, " * ", y, " = ", mul(x,y))    
elif choice == 'd':    
   print (x, " / ", y, " = ", div(x,y))  
elif choice == 'e':    
   print (x, " %", y, " = ", mod(x,y))  
elif choice == 'f':    
   print (x, "%(Percentage)", y, " = ", per(x,y))
else:    
   print ("This is an invalid input")    