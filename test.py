t = ([1],)
#([1,2],)
# l = [1]
# f = {t:"asd"}
# print(f[(t])
class test():
    id = 0
    def __init__(self,id):
        self.id = id
        id = 2

t = test(1)
print("===========t.id",t.id)
# def f():
#     f()
#     return 42
#
# f()

try:
    [1,2,3][4]
except IndexError:
    print("Index")
except:
    print("Exc")
else:
    print("something")
finally:
    print("finally")
a = {1:2,2:4}
print(a.items())
print(type(a))
#name as input and add epam
def mydev(f):
    def wrap(t):
        # t =
        print("t",f,t)
        return t+'epam'
    return wrap

@mydev
def nm(t):
    # nm = t
    return nm

print("hi123",nm("Ankit"))
 # 0 1 1 ()
# )
def fibona():
    a = 0
    b = 1
    for i in range(10):
        c = a+b
        a= b
        b = c
        # print(c)
        yield c

d =fibona()
print(d.__next__())
# == and is
print(d.__next__())
print(d.__next__())
print(d.__next__())

l = [0,0,1,1,0,1]

d = 0
for t in range(len(l)):
    for y in range(len(l)):
        if (l[t]<l[y]):
            c = l[t]
            l[t]= l[y]
            l[y]=c

print(l)

s = 'aaabb'
# l = ['aaabb']
# aba
# print(s[::-1]==s)
if s[::-1]==s:
    print("Anagram")
else:
    print("Not Anagram")

from itertools import permutations

s1 = permutations(s,5)
for t in s1:
    # print("".join(t))
    if "".join(t)=="".join(t)[::-1]:
        print("Anagram", "".join(t))
    # print(t)

a1 = int(input('Give amount: '))

def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

a = fib()
a.__next__()# 0
for i in range(a1):
    print(a.__next__())
