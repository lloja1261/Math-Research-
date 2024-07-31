#Luis Loja


import math    #This wil be used to calculate the python value of the functions

def factorial(m): #This is for calculating factorials. This will be implemented in the different functions. 
 f=1
 for i in range(1,m+1): 
     f*=i
 return(f)

def sin(x):    
    s=0
    for i in range(0,n+1):
        s+= x**(2*i+1)*(-1)**i/((factorial(2*i+1))) 
    return (s)
def cos(r):
    h=0
    for i in range(0,n+1):
        h+=x**(2*i)* (-1)**i/factorial(2*i)
    return(h)
def e(f):
    g=0
    for i in range(0,n+1):
        g+= (x**i)/factorial(i)
    return(g)
def l(j):
    b=0
    for i in range(1,n+1): # 0 is not included because you can't divide by 0.
        b+=(x-1)**(i) *(-1)**(i-1)/(i)
    return(b)
def a(p):
    d=0
    for i in range(0,n+1):
        d+=((-1)**i)* (x**(2*i+1))/(2*i+1)
    return(d)
    
ans="y" #This is to ask the user if they want to do this again
while ans=="y":
    choice=input("what function value do you want to use? The (l)n,the (e), (c)osine, the (s)ine, or the (a)rctan?  :")
    n=int(input("how many terms of the Taylor approximation do you want to use: ")) #This is basically asking the user how accurate they want it to be. 


    if choice==("s"): #For sine function
        x=int(input("what value do you want to use the sine for:"))
        print("The approximate value is",sin(x))
        print("The python value is", math.sin(x))
        print("The percent error is", (((abs((sin(x))-(math.sin(x)))/math.sin(x))))*100) #Percent Error calculation

    elif choice==("c"): #For cosine function
        x=int(input("what value do you want to use the cosine for:"))
        print("The approximate value is", cos(x))
        print("The python value is",math.cos(x))
        print("The percent error is", ((abs(((cos(x))-(math.cos(x)))/math.cos(x))))*100)

    elif choice==("e"): #For euler function
        x=int(input("what value do you want to raise e to:"))
        print("The approximate value is",e(x))
        print("The python value is", math.exp(x))
        print("The percent error is", ((abs(((e(x))-(math.exp(x)))/math.exp(x))))*100)

    elif choice==("l"): #For natural logarithm function
        print("The Taylor series for the natural logarithm would only be accurate"
              "for numbers greater than 0 or less than or equal to 2."
              "So Try to plug in a value within this range.")
        x=float(input("what value do you want to find the ln of:"))
        print("The approximate value is",l(x))
        print("The python value is", math.log(x))
        print("The percent error is", ((abs(((l(x))-(math.log(x)))/math.log(x))))*100)
    elif choice==("a"): #For arctangent function
        print("The Taylor series for the arctangent would only be accurate for"
              "numbers between -1 and 1,inclusive, so try to plug in a value within this range.")
        x=float(input("what value do you want find the arctangent of:"))
        print("The approximate value is",a(x))
        print("The python value is", math.atan(x))
        print("The percent error is", ((abs(((a(x))-(math.atan(x)))/math.atan(x))))*100)
    else:
        print("ERROR! Please eneter another value")
        break
    print()
    ans=input("Would you like to do this agai? (y)es or (n)o: ")
else:
    print("Bye!!") #The end of the program 
          
            
      
      
      
      
    











