# integer array
l = [1,2,3,4,1,2,1,2]
d = set(l)# remove duplicates

# time complexity - O(N)
k = []
for i in l:
    if i not in k:
        k.append(i)

print(k)

d = [1,2,3,1,3,4,3,0,-1]
# create func and return index of the searched value
d = sorted(d)
print("d===",d)
low = d[0]
high = d[-1]
def func(d, low, high, val):
    # print(sorted(d))
    if high>=low:
        mid = (low+high)//2
        print("mid", mid, d, low, high)
        # high = mid
        if d[mid]==val:
            return mid
        elif d[mid]>val:
            print("mid val", mid, val, d[mid])
            return func(d,low,mid-1,val)
        else:
            print("max val", mid, val, d[mid])
            return func(d, mid+1, high, val)
    else:
        return -1
    # for t in sorted(d):
    #     if val in d:
    #         print("index of search value",d.index(val))
    #         return d.index(val)

result = func(d,0, len(d)-1,1)
print("index at", result)

# inner join
# left join
# right join
# cross join
# ecommerce, users, products
# each user can buy products
# Tables
# user_id,
# id pk
# name
# email
# phone no
#
# product
# # user_id fk
# product_id
# product_name
# Product_cost
# total_products
#
# user_product
# user_id
# product_id
#
# # each user purchased products
# select u.uname, concat(u.uname, p.product_name) as productname from user_product up, user u, product p
# where up.user_id =u.id and up.product_id =product.product_id
# # group by user_id
#
# user product
# Ankit car|vehicle|


# projects a have some python version and libraries
# projects b have some python version and libraries

# create venv
# project dependencies libraries

# python 3
# or python 2
# x (y,z,a,b)
# api  time taken
# within 10 mins