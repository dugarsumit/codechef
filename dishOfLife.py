t = int(input())
for i in range(0,t):
    info = input()
    n, k = info.split(" ")
    k = int(k)
    n = int(n)
    bits = [0] * k
    some = False
    sum = 0.0
    true_sum = k*(k+1)/2
    for j in range(0,n):
        row = input()
        if some is not True:
            data = row.split(" ")
            for ingre in data[1:]:
                index = int(ingre)-1
                value = bits[index]
                if value == 0:
                    bits[index] = 1
                    sum = sum + index + 1
                    if sum == true_sum and j<n-1:
                        print("some")
                        some = True
    if some is not True:
        if sum != true_sum:
            print("sad")
        else:
            print("all")
