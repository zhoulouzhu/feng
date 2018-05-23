import random

a=[random.randint(9000,10000) for _ in range(10)]

for i in a:
    b=i%3
    if b == 0:
        print(" 马洪亮")
    else:
        print(i)





