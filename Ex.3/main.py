import matplotlib.pyplot as plt
import numpy as np

def LeapYear(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("It is a Leap Year!") 
        return True
    else:
        print("It is not a Leap Year!")
        return False
    

def fibo(n):
    fibolist = list()
    prev = 0
    next = 1
    temp = 0 
    for i in range(1,n+1):        
        fibolist.append(next)
        temp = next
        next += prev
        prev = temp
    return fibolist

def prime(n):
    primelist = list()
    for i in range(1,n+1):
        isPrime = True
        for j in range(2,i):
            if (i % j == 0):
                isPrime = False
                break            
        if isPrime:
            primelist.append(i)
    return primelist




n  = 100
year = 1900
LeapYear(year)
fibo_list = list(fibo(n))
primelist = list(prime(n))
print(fibo_list)
print(primelist)

