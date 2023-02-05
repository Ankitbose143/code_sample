def PhoneNumber(N):
    # this is default OUTPUT. You can change it.
    result = ""
    # print(N, type(N))
    # write your Logic h:ere:
    s = N
    print(s.rfind('?'))
    # print(s.lfind('?'))
    print(s.index('?'))
    print(s.find('?'))
    res = 0
    k = []
    for i in range(0, len(N)):
        if N[i] == '?':
            res = i + 1
            k.append(i)
            print("ggggg",i,res)
    print("gggggkkk", k)
    u = 0
    # t = k[0]
    # while u<=9 or t in k[::-1]:
    for t in k[::-1]:
        print(t, N[:t])
        # if '?' in N[t]:
        N=N[:t]+str(u)+N[t+1:]
        print(N)
        u+=1
        t+=1
        # N = N.replace('?', str(t))
        # print(N, type(N))
        # if int(N) % 3 == 0:
        #     result = int(N)

    print(result)


# INPUT [uncomment & modify if required]
N = input()

# OUTPUT [uncomment & modify if required]
PhoneNumber(N)