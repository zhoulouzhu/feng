member=["狗杨",'孙杨','方哥']
member.append("小方子")
member.extend(["方块",("狗蛋")])
member.insert(0,'孟伟')
#member.clear()
#member.remove("狗蛋")
temp=member[0]
member[0]=member[1]
member[1]=temp
#del  member[1]
member.pop()
member.pop(1)
member[1:3]
print(member[1])
print(member)
print(member[1:3])
print(member[1])
print(member[3])
print(member[:])
print(member[:3])
print('{名字}今天{动作}'.format(名字='陈某某', 动作='拍视频'))