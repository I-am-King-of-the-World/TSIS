#ex1
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

list1 = [1, 2, 3]
print(multiplyList(list1))

#ex2
def string_test(s):
    
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    
   
    for c in s:
        
        if c.isupper():
            
            d["UPPER_CASE"] += 1
        
        elif c.islower():
            
            d["LOWER_CASE"] += 1
        else:
            
            pass
    
    
    print(s)
    print(d["UPPER_CASE"])
    print(d["LOWER_CASE"])

string_test('The quick Brown Fox') 

#ex3
def isPalindrome(s):
    return s == s[::-1]

s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")

#ex4
from time import sleep
import math


def delay(fn, ms, *args):
    
    sleep(ms / 1000)
    
    
    return fn(*args)

print("Square root after specific milliseconds:") 
print(delay(lambda x: math.sqrt(x), 100, 16))
print(delay(lambda x: math.sqrt(x), 1000, 100))
print(delay(lambda x: math.sqrt(x), 2000, 25100))

#ex5
print(all([True, True, True]))
