test=int(input())
for t in range(0, test):
    n, q=input().split(" ")
    n=int(n)
    q=int(q)
    prices=input().split(" ")
    cons_count=[0] * n
    max_count=1
    l=len(prices)
    m = 1
    cons_count[0]=1
    for index in range(1,l):
        if prices[index] == prices[index-1]:
            cons_count[index] = cons_count[index-1] + 1
        else:
            cons_count[index] = 1
        if cons_count[index]>m:
            m = cons_count[index]

    #print(cons_count)
    for qn in range(0, q):
        que=input().split(" ")
        L=int(que[0])
        R=int(que[1])
        K=int(que[2])
        stable_count=0
        j=R-1
        if K<=m:
            while(j>=L-1):
                v = cons_count[j]
                num_left = j-L+2
                if num_left>=v:
                    if v >= K:
                        stable_count=stable_count+1
                    j=j-v
                else:
                    if num_left>=K:
                        stable_count=stable_count+1
                    j = L-2
        print(stable_count)