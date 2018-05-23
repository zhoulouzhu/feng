student=['jack','gy','syy','dlg']
print(student[0])
print(student[1])
print(student[2])
print(student[3])
print(student[-2])
print(student[-1])#访问最后一个元素
student.append('gyy')
student.insert(0,"hehe")
student[0]="daye"
student.pop(2)
print(student)


course=('cc','zz','ff','mm','ww')
print(course)
print(course[1:3])
print(len(course))
t=(1,)
print(t)
score=(78,90,88,67,78)
print(min(score))
student={1:'jack',2:'bob',3:'marry',4:',micle'}
print(student[2])
student[2]='haryy'
print (student)
del student[1]
print (student)
student.clear()
print (student)
del student