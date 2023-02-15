N= 2
# l = [[1,3],[2,3]]
N= 4
l1 = [[1,3],[1,4],[2,3],[3,4],[4,3],[4,1]]
print("l1", l1)

g = list(map(lambda x:x[1],l1))#append 2nd index in alist
print(g)
# result = [t for t in l1 if t[1]==3]
# print(result)
f = []
k = []
for i in l1:
    print(i)
    f.append(i[1])
    # for j in
print("f===",f)
re = {x:f.count(x) for x in set(f)}#find count of elements in list and into dict
print(re, max(re.values()))#find max in dict values
# lists = l1
# def common_elements(lists):
#     seen = set(lists[0][1])
#     for i in range(1, len(lists)):
#         seen &= set(lists[i][1])
#     print("Seen", seen)
#     return list(seen)
#
# common_elements(l1)

# finding the count iteration i and i-1 and then if not matching storing in to another variable max count
# and checking max
def max_occurring(arr):
    arr.sort()
    max_element = arr[0]
    max_count = 1
    current_element = arr[0]
    current_count = 1
    print(arr)
    for i in range(1, len(arr)):
        print("------curr",current_element, current_count, max_count)
        print(arr[i], arr[i-1])
        if arr[i] == arr[i - 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_element = current_element
                max_count = current_count
            current_element = arr[i]
            current_count = 1
    if current_count > max_count:
        max_element = current_element
    return max_element
print("hi")
print("max",max_occurring(g))

arr1 = g
current_count1 = 0
for i in range(1, len(arr1)):
    print("arr1", arr1)
    # print("------curr", current_element, current_count, max_count)
    print("arrays",i,"====",arr1[i], arr1[i - 1])
    if arr1[i] == arr1[i - 1]:
        current_count1 += 1
        print("current_count1", current_count1)
