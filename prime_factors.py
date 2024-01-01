import math

def divides(a,b): # if b is a factor of a
    if(a%b==0):
        return True
    return False

def prime(n):
    for i in range(2, math.floor(math.sqrt(n))+1):
        if divides(n,i):
            return False
    return True

def factors(n):
    factors = [1]
    for i in range(2, math.floor(n/2)+1):
        if divides(n,i):
            factors.append(i)
    factors.append(n)
    return factors

def prime_factorization(n):
    #[[prime,exponent],[prime,exponent],...]
    factors_list = factors(n)
    prime_factorization = []
    for i in range(1, len(factors_list)):
        if(prime(factors_list[i])):
            #find out no. of times i divides n
            exponent = 1
            counter = 2
            while True:
                if(divides(n,factors_list[i]**counter)):
                    exponent += 1
                    counter += 1
                else:
                    break
            prime_factorization.append([factors_list[i],exponent])
    return prime_factorization

def print_factorization(factorization):
    for prime_info in factorization:
        print(str(prime_info[0])+"^"+str(prime_info[1])) # had to use strings anyway

            
            
n = 24
print(factors(n))
print(prime_factorization(n))
print_factorization(prime_factorization(n))