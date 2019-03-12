#函数的调用，不多说
#import 调用外部文件的使用from filename import function
#定义函数：使用def语句
#def my_abs(x):
#    if x==1:
#        return 0
#    else:
#       return 1
#参数类型检查
#isinstance函数使用
#def my_abs(x):
#    if not isinstance(x, (int, float)):
#        raise TypeError('bad operand type')
#    if x >= 0:
#        return x
#    else:
#        return -x
#可以返回多个值，实际上返回的是一个，只不过类型是tuple
#def move(x, y, step, angle=0):
#    nx = x + step * math.cos(angle)
#    ny = y - step * math.sin(angle)
#    return nx, ny
import math
def quadra(a,b,c):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
        raise TypeError('bad operand type')
    #math.sqrt()
    if b**2-4*a*c < 0:
        return None
    elif a==0:
        return -1*c/b
    else:
        res = ((-1*b+math.sqrt(b**2-4*a*c))/2*a,(-1*b-math.sqrt(b**2-4*a*c))/2*a)
        return res
print(quadra(0,4,2))

#参数问题，可以给函数的参数提前赋值，这样的有些参数就是默认的值了
#参数个数不同的情况下，在参数前面加个*号就可以传回去了
#可以用**传递一个字典，传入参数不受限定
#位置参数必须有且类型一致
def product(*args,**rgs):
    gras=1
    for tbs in args:
        gras *= tbs
    return gras

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
#递归函数和常规得一样