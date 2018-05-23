sum=0
for i in  range(10):
    sum+=i
print(sum)

n=10
while n>0:
    n=n-1
    print(n)
print('game over')

import  random
answer=random.randint(1,100)
n=int(input("please input num:"))
while n!=answer:
    if n>answer:
        n=int(input("num is big!please continue input:"))
    elif n<answer:
        n=int(input("num is small! please continue input:"))
print("you win the game!")


