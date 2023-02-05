data_list = [0,1,0,1,0,0,1]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:
        print("Minimum, x",  data_list.index(minimum))
        if x < minimum:
            minimum = x

    new_list.append(minimum)
    data_list.remove(minimum)

print(new_list)


# def gt():
t = (item for item in range(1,10000) if item%42==0)
print("tesla",t,next(t))

def gt():
    return next(item for item in range(1,10000) if (item%42==0))

# for t in gt:
#     print("test",t)
print(gt())
from itertools import count
def for3():
    items = []
    for item in count(10):
        print("irt", item)
        if item %42==0:
            print("items",item)
            break

for3()

test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)]

# printing original list
print("The original list is : " + str(test_list))
test_list = [("GFG", "IS", "BEST"), ("gFg", "aVERAGE"), ("GFG",), ("gfg", "cS")]

# printing original list
print("The original list is : " + str(test_list))

# all() returns true only when all strings are uppercase
res = [sub for sub in test_list if any(ele.isupper() for ele in sub)]
# all() to check each element
# res = [sub for sub in test_list if all(ele >= 0 for ele in sub)]
# for sub in test_list:
#     if all(ele >= 0 for ele in sub):
#         print("kkk",sub,list(ele >= 0 for ele in sub))

# printing result
print("Positive elements Tuples : " + str(res))

