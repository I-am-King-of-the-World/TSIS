#ex1
grams=int(input())
ounces=28.3495*grams
print(ounces)

#ex2
fahrenheit=int(input())
celsius=(fahrenheit-32)*(5/9)
print(celsius)

#ex3
heads=int(input())
legs=int(input())

def solve(numheads, numlegs):
    rabbit=(numlegs-2*numheads)/2
    chicken=numheads-rabbit
    print("chicken =" , chicken)
    print("rabbit =" , rabbit)
solve(heads, legs)

#ex4
def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
Numbers=[1,2,3,4,5,7657,33,24,375,9,34,9593,45]
prime_number=list(filter(prime, Numbers))
print(prime_number)

#ex5
import itertools

lisst=[1,2,3,4,5]
permutations= list(itertools.permutations(lisst))

for b in permutations:
    print(b)

#ex6
x="where are you"
s=x.split(' ')
for d in reversed(s):
    print(d)

def ounces(gramm):
    return 28.3495231 * gramm

#7.
def has_33(numbs):
    i = 0
    while i < len(numbs)-1:
        if numbs[i] == 3:
            if numbs[i+1] == 3:
                return True
        i += 1
    return False


#8.
def spy_game(numbs):
    s = ''
    for i in numbs:
        s += i
    if '007' in s:
        return True
    return False


#9.
def v_radius(radius):
    v_sphere = 4/3*3.14*radius**3
    return v_sphere


#10.
def unique_elements(l):
    new_list = []
    i = 0
    while i < len(l):
        t_or_f = True
        j = 0
        while j < i:
            if l[i] == l[j]:
                t_or_f = False
            j += 1
        if t_or_f:
            new_list.append(l[i])
        i += 1
    return new_list


#11.
def palindrome(text):
    i = 0
    j = len(text)-1
    while i < len(text)/2:
        if text[i] != text[j]:
            return 'No palindrome'
        i+=1
        j-=1
    return 'palindrome'


#12.
def histogram(gist):
    i = 0
    while i < len(gist):
        j = 0
        while j < gist[i]:
            print('*', end='')
            j += 1
        print()
        i += 1


#13.
import random;

def find_num_random(rand_num, count):
    count += 1
    num = int(input('Take a guess.\n'))
    if num == rand_num:
        print(f'Good job, KBTU! You guessed my number in {count} guesses!')
        return
    print('\nYour guess is too low.')
    return find_num_random(rand_num, count)
