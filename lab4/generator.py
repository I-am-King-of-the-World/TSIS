#ex1
a = (i**2 for i in range(1,5))
for i in a:
    print(i)

#ex2
n = int(input())

for i in range(0, n+1, 2):
  if i < n - 1:
    print(i, end = ',' )
  else:
    print(i)

#ex3
n=int(input())

div = [i for i in range(0, n) if (i % 7 == 0)]
print(div)

#ex4
q=int(input())
w=int(input())
a = (i**2 for i in range(q,w))
for i in a:
    print(i)

#ex5
q=int(input())
a = (i**2 for i in range(0,q))
for i in a:
    print(i)