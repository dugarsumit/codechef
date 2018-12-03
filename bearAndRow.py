test=int(input())
for t in range(0, test):
    a=input()
    count = one_start=one_end=zero_start=zero_end=index=zero_count=one_count=0
    data_len=len(a)
    while (index < data_len and a[index] != '1'):
        index=index+1
    one_start=one_end=index
    while (index < data_len and one_end != data_len):
        while (index < data_len and a[index] != '0'):
            index=index+1
        one_end=zero_start=zero_end=index
        while (index < data_len and a[index] != '1'):
            index=index+1
        zero_end=index
        one_count = one_count + one_end-one_start
        zero_count = zero_end-zero_start
        if (zero_count > 0):
            update = one_count*(zero_count + 1)
        else:
            update=one_count * zero_count
        count=count+update
        one_start = zero_start = one_end = index = zero_end
    print(count)