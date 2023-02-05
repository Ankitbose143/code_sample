l = [1,2,3,3,3,1,-1,-9,10]
m = [4,5,6,7,3,2,-5,-3,0,1,-1]

i = 0
# for t in l:
t = 0
y = 0
# while t<len(l) and y<len(m):
#     # for y in m:
#     #     if t+y==9:
#     #         print(t,y)
#     print("==",l[t], m[y])
#     if i<len(m) and t+m[i]==9:
#             print(t,m[i])
#     t+=1
#     y+=1
#
list1 = [1, 2, 3]
list2 = ['a', 'b']

for i in range(max(len(list1), len(list2))):
    print("i",i)
    if i < len(list1):
        x = list1[i]
    else:
        x = None
    if i < len(list2):
        y = list2[i]
    else:
        y = None
    print(x, y)

print("=====================================================================")
def find_pairs(list1, list2, target):
    pairs = []
    pairs2 = []
    # for x in list1:
    for x in sorted(list1):
        y = target - x
        print("pairs x,y", x, y)
        x1 = func(sorted(list2),0,len(list2)-1, y)
        # if binary_search(list2, y):
        print("ssssxxxxsss",x1)
        # if x1:
        pairs.append((x, y))
        pairs2.append(x)
        print("pairs----------", pairs,x,y, pairs2)
    return pairs

def func(d, low, high, val):
    print("dfffdfd",d)
    if high>=low:
        mid = (low+high)//2
        print("mid", mid, low, high, d[mid], d[mid]==val, val)
        # high = mid
        if d[mid]==val:
            return mid
        elif d[mid]>val:
            print("mid val", low,mid, val, d[mid])
            return func(d,low,mid-1,val)
        else:
            print("max val", mid, val, d[mid])
            return func(d, mid+1, high, val)
    else:
        return -1

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    print("Arr", arr, x)
    while low <= high:
        mid = (low + high) // 2
        print("Arr mid", low, mid,high, arr[mid])
        if arr[mid] == x:
            print(arr[mid], mid)
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Test the find_pairs function
list1 = [1, 1,2,-1,0,2, 3]
list2 = [3,-2,5,4, 5, 6]
target = 7

pairs = find_pairs(list1, list2, target)
print(pairs)

