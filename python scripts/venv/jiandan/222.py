import random
answer=random.randint(1,100)
n=int(input("请输入数字："))
while n!=answer:
    if n>answer:
        n=int(input("数字太大，重输："))
    elif n<answer:
        n=int(input("数字小了，重输："))

print("猜对了")

name="xuerb"
chengshi="huaian"
nianling="25"
print("wojiao%s,jiazhu%s,jinnian%sle."%(name,chengshi,nianling))

print("heihei")


class Student():
    def __init__(self,name,city):
        self.name=name
        self.city=city
        print("My name is %s and come from %s" % (name, city))





