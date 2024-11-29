'''
Created by Neda Topuz
Modified by Aziz Yildirim
'''

def findPrime(prime):
    if prime < 2:
        return False

    for i in range(2,int(prime**0.5)+1)  :
       if prime % i == 0:
        return False

    return True

def primeNeighbor(upperBound):
 if isinstance(upperBound, str):
        raise ValueError("Hata: upperBound bir sayı olmalı, string değeri kabul edilmez.")
 if upperBound < 1000:
    for prime in range(int(upperBound),1,-1):
        if findPrime(prime):
            print(prime)
            return prime


    return 0






