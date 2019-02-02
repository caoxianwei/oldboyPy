__author__ = "Alex Li"
def test1():
    print('in the test1')

def test2():
    print('in the test2')
    return 0
def test3():
    print('in the test3')
    #return 1,'hello',['alex','wupeiqi'],{'name':'alex'}
    return  test2


x=test1()
y=test2()
z=test3()
print(x)
print(y)
print(z)

print('from test1 return is [%s]:' %type(t1),t1)
print('from test2 return is [%s]:' %type(t2),t2)
print('from test3 return is [%s]:' %type(t3),t3)
