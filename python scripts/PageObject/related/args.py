def fun_args1(args):
    print("args,is %s" %args)

def fun_args2(args1,args2):
    print("args1 is %s args2 is %s"%(args1,args2))

def fun_var_args(*args):
    for value in  args:
        print("args:",value)

# fun_args1('51zxw')
# fun_args1()

# fun_args2('51zxw','Python')
# fun_args2('51zxw')



#fun_var_args("sd ","sd")
fun_var_args()