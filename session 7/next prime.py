def prime(a):
    is_prime=True
    if(a<=1):
       return not is_prime
    else:
        for i in range(2,int(a**0.5)+1):
            if(a%i==0):
                return not is_prime
          
    return is_prime
def next_prime(c):
    for i in range(c+1,2**31):
        a=prime(i)
        if(a==True):
            print("next prime is:",i)
            break
# div=int(input("Enter value to find divisors :"))
# divisors(div)
prime1=int(input("enter the number to check it is prime:"))
next_prime(prime1)