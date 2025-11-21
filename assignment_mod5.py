def factorial(n):
    if  isinstance(n, int):
        pass
    else:
        print("Enter a valid input.factorial is only defined for integers.")
        exit()
    if(n<0):
        print("factorial is not defined for negative numbers.")
        exit()
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)   

def is_prime(n):
    if  isinstance(n, int):
        pass
    else:
        print("input must be an integer.")
        exit()
    if(n<0):
        print("negative numbers cannot be prime.")
        exit()
    if n<=1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a,b):
     if  (isinstance(a, int ) and isinstance(b, int )):
        pass
     else:
        print("input must be an integer.")
        exit()
     if a<0 or b<0:
         print("GCD inputs must be non negative.")
         exit()
     if b==0:
         return a
     return  gcd(b, a % b)