
l = [1,2,2,3,3,4]
m = [4,45,5,7,78,8,67,678]


for el, el1 in zip(l,m):
    print(el)
    print(el1)
i = 0
j = 0
while i < len(l) or j < len(m):
    if i < len(l):
        element1 = l[i]
        # Do something with element1
        print(element1)
        i += 1
    if j < len(m):
        element2 = m[j]
        # Do something with element2
        print(element2)
        j += 1