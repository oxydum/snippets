import re, sys



def mul(x, y):
    return x * y

def add(x, y):
    return x + y
    
def inc(x):
    return x + 1
    
def dec(x):
    return x - 1


def isPrime(x):
    return re.match(r'^1?$|^(11+?)\1+$', '1' * x) == None


