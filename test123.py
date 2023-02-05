string = "biggeststring"
substrings = [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string)+1)]
smallest_substring = min(substrings, key=len)
print(smallest_substring)

strings = ['ahffskaksfajeebsne', 'jefaa']
biggest_string = max(strings, key=len)
print("rere", biggest_string)
substrings = [biggest_string[i: j] for i in range(len(biggest_string)) for j in range(i + 1, len(biggest_string)+1)]
smallest_substring = min(substrings, key=len)
print(smallest_substring)
strings = 'ahffskaksfajeebsne'
char = 'a'
d = strings[1]
print("iuoi",d, strings[0])
r = 0
for index in range(len(strings)):
    # if strings.find(char, j):
    index = strings.find('a', index)
    r+=1
    if index == -1:
        break
    print("indx",index)


strings = 'ahffskaksfajeebsne'
index = 0
char = 'a'
while index < len(strings):
    print("idx",index)
    index = strings.find(char, index)
    print("idx12",index)
    if index == -1:
        break
    print("inhhh",index,char)
    index += 1

import re
strings = ['ahffskaksfajeebsne', 'jefaa']
lt= []
lt2 = []
for match2 in strings[1]:
    lt = []
    for match in re.finditer(match2, strings[0]):
        lt.append(match.start())
        print("dfg",match2,match.start(), lt)
    lt2.append(lt)
# print(min(lt2, key=len))
print("ok", lt2)
print("dup", list(set(map(tuple,lt2))))
print(list(set(frozenset(i) for i in lt2)))
unique_list = [x for i, x in enumerate(lt2) if x not in lt2[:i]]
print("uniq", unique_list)
unique_list2= []
unique_list3= []
for i, x in enumerate(lt2):
    print(i,x, lt2[:i])
    if x not in lt2[:i]:
        unique_list2.append(x)
    else:
        unique_list3.append(x)
print("uniq", unique_list2)
print("uniq3", unique_list3)
unique_list3.sort(reverse=True)
print(unique_list3)
# print("---",lt2-list(set(lt2)))