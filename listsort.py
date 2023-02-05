def find_pairs(arr, k):
    arr.sort()
    print(arr)
    left, right = 0, len(arr) - 1
    pairs = []
    pairs2 = []
    per = {}
    while left < right:
        print("====",left, right, arr[left], arr[right])
        if arr[left] + arr[right] < k:
            pairs.append((arr[left], arr[right]))
            pairs2.append(arr[left]+arr[right])
            per[arr[left]+arr[right]] = (arr[left], arr[right])
            left += 1
        else:
            right -= 1
    print("pairs", pairs)
    print("pairs2", pairs2)
    print("per", per, max(per), "sasasamax",max(per.values()))
    return max(pairs)


arr = [23,4,53,3,54,45,90,78,1,59,58, 2,57]
k = 60

print(find_pairs(arr, k))