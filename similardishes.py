t = int(input().split(" ")[0])
for i in range(0,t):
    dish1 = input()
    dish2 = input()
    ingredients1 = dish1.split(" ")
    ingredients2 = dish2.split(" ")
    count = 0
    for ingredient in ingredients2:
        if ingredient in ingredients1:
            count +=1
            if count >=2:
                break
    if(count>=2):
        print("similar")
    else:
        print("dissimilar")