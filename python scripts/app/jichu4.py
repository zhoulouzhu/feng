#_*_ coding:utf-8 _*_
import json
import xml.dom.minidom
'''test1={'android':'appium','web':'selenium','interface':u"test"}
js=json.dumps(test1)
js=json.dumps(test1,sort_keys=True,indent=4,separators=(',',':'),ensure_ascii=True)
#print(js)
#print(type(js))

#print(json.loads(js))
#print(type(json.loads(js)))
#f=open("test.json",'w')
#json.dump(js,f)
f=open("test.json",'r')
print(json.load(f))'''

dom=xml.dom.minidom.parse("cc.xml")
root=dom.documentElement
list=root.getElementsByTagName('user')
print(list[0].getAttribute('id'))
print(list.getElementsByTagName("name").childNodes[0].nodeValue)