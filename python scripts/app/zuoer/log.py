#coding=utf-8
import  time
import logging
def log(str):

 '''   f=open("log.txt",'a')
    f.writelines(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    f.writelines(" "+str)
    f.writelines("\n")
    f.close()

log("appiumtest")
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))'''

def log(str):
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='log-appium.log',
                    filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    #logging.debug('test1')
    logging.info(str)
    #logging.warning('')
    #logging.error('test4')

log('买票 ')

#print 3/0
'''try:
    print (3/0)
except:
    print ('ex')
print ('tt')'''