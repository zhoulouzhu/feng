import  random
answer=random.randint(1,100)
guess = int(input("猜数字："))
while guess != answer:



    if guess >answer:
        guess =int(input("重输，大了："))

    elif guess< answer:
        guess=int(input("重输，小了："))




print("gameover")

