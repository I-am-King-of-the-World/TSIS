#ex1
import datetime
x = datetime.datetime.now()
print(x.day-5)

#ex2
import datetime
x = datetime.datetime.now()
z= int(input())
if x.day-1==z:
    print("yesterday")
elif x.day+1==z:
    print("tomorrow")
elif x.day==z:
    print("today")

#ex3
d=x.replace(microsecond=0)
print(d.microsecond)

#ex4
q=datetime.datetime(2024,2,20)
w=(x-q)
print(w)
w=(x-q).total_seconds()
print(w)