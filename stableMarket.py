test=int(input())
for t in range(0, test):
    n, q = input().split(" ")
    n = int(n)
    q = int(q)
    prices = input().split(" ")
    cons_count = [0]*n
    start = end = 0
    l = len(prices)
    for index in range(0, l):
        if start < l:
            p=prices[start]
        while(end < l and p == prices[end]):
            end = end + 1
        count = end - start
        for i in range(start, end):
            cons_count[i] = count
            count = count - 1
        index = start = end
    #print(cons_count)
    m=max(cons_count)
    for qn in range(0, q):
        que = input().split(" ")
        L = int(que[0])
        R = int(que[1])
        K = int(que[2])
        stable_count = 0
        j = L-1
        if K <= m:
            while(j<R):
                v = cons_count[j]
                if v<K:
                    j=j+v
                elif(v > R-j):
                    if(R-j >= K):
                        stable_count = stable_count + 1
                    j = R
                else:
                    stable_count = stable_count + 1
                    j = j + v
        print(stable_count)