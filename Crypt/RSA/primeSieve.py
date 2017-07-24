#!/usr/bin/python3

from math import *

def isPrime(num):
    if num < 2:return False
    for i in range(2 , int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def primeSieve(sieveSize):
    sieve = [True] * sieveSize
    sieve[0] = sieve[1] = False

    for i in range(2,int(sqrt(sieveSize)) + 1):
        point  = i * 2
        while point < sieveSize:
            sieveSize[point] = False
            pointer += 1

    primes = []
    for i in range(sieveSize):
        if sieveSize[i]:
            primes.append(i)
    return primes

