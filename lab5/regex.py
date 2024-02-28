#ex1
import re

a="abbb"
x=re.search("^a(b*)$", a)
if x:
    print("Yes")
else:
    print("No")

#ex2
a="abb"
x=re.search("^a(b{2,3})$", a)
if x:
    print("Yes")
else:
    print("No")

#ex3
a="a_b"
x=re.search("^[a-z]+_[a-z]+$", a)
if x:
    print("Yes")
else:
    print("No")

#ex4
a="Acccb"
x=re.search("[A-Z]+[a-z]+$", a)
if x:
    print("Yes")
else:
    print("No")

#ex5
a="acccb"
x=re.search("a.*?b$", a)
if x:
    print("Yes")
else:
    print("No")

#ex6
a="a 3,f."
x=re.sub("[ ,.]", ":", a)
print(x)

#ex7
a="hello_world"
x=''.join(x.capitalize() or '_' for x in a.split('_'))
print(x)

#ex8
a = "HelloWorld"
print(re.findall('[A-Z][^A-Z]*', a))

#ex9
a="HelloWorld"
x=re.sub(r"(\w)([A-Z])", r"\1 \2", a)
print(x)

#ex10
a="HelloWorld"
y=re.sub('(.)([A-Z][a-z]+)', r'\1_\2', a)
x=re.sub('([a-z0-9])([A-Z])', r'\1_\2', y).lower()
print(x)