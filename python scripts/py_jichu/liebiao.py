list1=[123,456]
list2=[456,234]
list3=[456,234]
list4=list1+list2
print(list4)
print(list1*3)
list3*=3
print(list1>list2)
print(list1<list2 and list3==list2)

print('gouyang' in list1)
print(list3.count(234))
print(list3.index(234,0,7))
print(list3.reverse())
print(list3)
list4=[5,8,7,1,5,3,6,4,9]
list4.sort()
print(list4)

list4.sort(reverse=True)
print(list4)