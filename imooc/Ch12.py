#12_3
import math
import functools 
import time

def add(x, y, f):
    return f(x) + f(y)

print (add(25, 9, math.sqrt))



#12_4   map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。由于list包含的元素可以是任何类型，因此，map() 不仅仅可以处理只包含数值的 list，事实上它可以处理包含任意类型的 list，只要传入的函数f可以处理这种数据类型。

def format_name(s):
    return s[0].upper()+s[1:].lower()

print (list(map(format_name, ['adam', 'LISA', 'barT'])))  #将list内字符串规范为首字母大写其余小写





#12_5   reduce()函数也是Python内置的一个高阶函数。reduce()函数接收的参数和 map()类似，一个函数 f，一个list，但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。reduce()还可以接收第3个可选参数，作为计算的初始值
#reduce(f, [1, 3, 5, 7, 9], 100)
#结果将变为125
def prod(x, y):
    return x*y

print (functools.reduce(prod,[2,4,5,7,12]))




#12_6  这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。 int类型不能直接迭代。
def is_sqr(s):
    return int(math.sqrt(s))**2==s

print (list(filter(is_sqr, range(1,101))))




#12_7  sorted()也是一个高阶函数，它可以接收一个比较函数来实现自定义排序，比较函数的定义是，传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。此题待验证。对字符串排序时，有时候忽略大小写排序更符合习惯。请利用sorted()高阶函数，实现忽略大小写排序的算法。
''''def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0'''
print (sorted(['bob', 'about', 'Zoo', 'Credit'],key=lambda a:a.upper()))






#12-8  在函数 f 内部又定义了一个函数 g。由于函数 g 也是一个对象，函数名 g 就是指向函数 g 的变量，所以，最外层函数 f 可以返回变量 g，也就是函数 g 本身。返回函数可以把一些计算延迟执行。函数名指向了一个匿名函数，这个匿名函数是个对象。再写一个以g命名的函数就是对变量重新赋值了，所以Python里没有重载这个概念
import functools
def calc_prod(lst):
    def lazy_prod():
        def prod(x,y):
            return x*y 
        return functools.reduce(prod,lst)   
    return lazy_prod    
    

f = calc_prod([1, 2, 3, 4])
print (f())



#12-9考察上一小节定义的 calc_sum 函数：
''''def calc_sum(lst):
    def lazy_sum():
        return sum(lst)  #此处引用lst
    return lazy_sum
注意: 发现没法把 lazy_sum 移到 calc_sum 的外部，因为它引用了 calc_sum 的参数 lst。
像这种内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。闭包的特点是返回的函数还引用了外层函数的局部变量，所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。举例如下：
# 希望一次返回3个函数，分别计算1x1,2x2,3x3:
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果全部都是 9（请自己动手验证）。
原因就是当count()函数返回了3个函数时，这3个函数所引用的变量 i 的值已经变成了3。由于f1、f2、f3并没有被调用，所以，此时他们并未计算 i*i，当 f1 被调用时：
>>> f1()
9     # 因为f1现在才计算i*i，但现在i的值已经变为3
因此，返回函数不要引用任何循环变量，或者后续会发生变化的变量。答案：考察下面的函数 f:
def f(j):
    def g():
        return j*j
    return g
它可以正确地返回一个闭包g，g所引用的变量j不是循环变量，因此将正常执行。
在count函数的循环内部，如果借助f函数，就可以避免引用循环变量i。
参考代码:
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()'''


def count():
    fs = []
    for i in range(1, 4):
        def g(i):
            def f():
                return i*i
            return f
            
        fs.append(g(i))
    return fs

f1, f2, f3 = count()
print (f1(), f2(), f3())







#12_10
'''高阶函数可以接收函数做参数，有些时候，我们不需要显式地定义函数，直接传入匿名函数更方便。
在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算 f(x)=x2 时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：
>>> map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
[1, 4, 9, 16, 25, 36, 49, 64, 81]
通过对比可以看出，匿名函数 lambda x: x * x 实际上就是：
def f(x):
    return x * x
关键字lambda 表示匿名函数，冒号前面的 x 表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不写return，返回值就是该表达式的结果。
使用匿名函数，可以不必定义函数名，直接创建一个函数对象，很多时候可以简化代码：
>>> sorted([1, 3, 9, 5, 0], lambda x,y: -cmp(x,y))
[9, 5, 3, 1, 0]
返回函数的时候，也可以返回匿名函数：
>>> myabs = lambda x: -x if x < 0 else x 
>>> myabs(-1)
1
>>> myabs(1)
1

利用匿名函数简化以下代码：
def is_not_empty(s):
    return s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])'''


is_not_empty=lambda s:s and len(s.strip())>0  #注意and的用法

print (list(filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])))



#12_11 装饰器教学视频 无题目



#12_12
''''Python的 decorator 本质上就是一个高阶函数，它接收一个函数作为参数，然后，返回一个新函数。
使用 decorator 用Python提供的 @ 语法，这样可以避免手动编写 f = decorate(f) 这样的代码。
考察一个@log的定义：
import functools

def log(f):
    def fn(x):
        print ('call ' + f.__name__ + '()...')
        return f(x)
    return fn
    
@log
def factorial(n):
    return functools.reduce(lambda x,y: x*y, range(1, n+1))
print (factorial(10))

但是，对于参数不是一个的函数，调用将报错：
@log
def add(x, y):
    return x + y
print add(1, 2)
结果：
Traceback (most recent call last):
  File "test.py", line 15, in <module>
    print add(1,2)
TypeError: fn() takes exactly 1 argument (2 given)
因为 add() 函数需要传入两个参数，但是 @log 写死了只含一个参数的返回函数。
要让 @log 自适应任何参数定义的函数，可以利用Python的 *args 和 **kw，保证任意个数的参数总是能正常调用：
def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()...'
        return f(*args, **kw)
    return fn
现在，对于任意函数，@log 都能正常工作。'''

def performance(f):
    def fn(*args, **kw):
        t1 = time.time()  #.time(...)  time() -> floating point number返回当前时间的时间戳
        r = f(*args, **kw)
        t2 = time.time()
        print ('call %s() in %fs' %(f.__name__, (t2 - t1)))  #%是格式化的意思，%s是格式化字符串，%f是格式化浮点数，这句话的意思是把f.__name__插入到了%s这个位置，(t2-t1)计算后的值插入到了%f这个位置
        return r
    return fn

@performance
def factorial(n):
    return functools.reduce(lambda x,y: x*y, range(1, n+1))
print (factorial(10))






#12_13 
'''考察上一节的 @log 装饰器：
def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn
发现对于被装饰的函数，log打印的语句是不能变的（除了函数名）。
如果有的函数非常重要，希望打印出'[INFO] call xxx()...'，有的函数不太重要，希望打印出'[DEBUG] call xxx()...'，这时，log函数本身就需要传入'INFO'或'DEBUG'这样的参数，类似这样：
@log('DEBUG')
def my_func():
    pass
把上面的定义翻译成高阶函数的调用，就是：
my_func = log('DEBUG')(my_func)
上面的语句看上去还是比较绕，再展开一下：
log_decorator = log('DEBUG')
my_func = log_decorator(my_func)
上面的语句又相当于：
log_decorator = log('DEBUG')
@log_decorator
def my_func():
    pass
所以，带参数的log函数首先返回一个decorator函数，再让这个decorator函数接收my_func并返回新函数：
def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBUG')
def test():
    pass
print test()
执行结果：
[DEBUG] test()...
None
对于这种3层嵌套的decorator定义，你可以先把它拆开：
# 标准decorator:
def log_decorator(f):
    def wrapper(*args, **kw):
        print '[%s] %s()...' % (prefix, f.__name__)
        return f(*args, **kw)
    return wrapper
return log_decorator

# 返回decorator:
def log(prefix):
    return log_decorator(f)
拆开以后会发现，调用会失败，因为在3层嵌套的decorator定义中，最内层的wrapper引用了最外层的参数prefix，所以，把一个闭包拆成普通的函数调用会比较困难。不支持闭包的编程语言要实现同样的功能就需要更多的代码。'''

#import time

#上一节的@performance只能打印秒，请给 @performace 增加一个参数，允许传入's'或'ms'：我的答案：
def performance(unit):
    def performace_decorator(f):
        def wrapper(*args,**kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            if unit=='ms':
                print ('call %s() in %fms' %(f.__name__, (t2 - t1)*1000))
            elif unit=='s':
                print ('call %s() in %fs' %(f.__name__, (t2 - t1)))
            return r
        return wrapper
    return performace_decorator    

@performance('ms')
def factorial(n):
    return functools.reduce(lambda x,y: x*y, range(1, n+1))

print (factorial(10))



#官方答案：
#import time
def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print ('call %s() in %f %s' % (f.__name__, t, unit))
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return functools.reduce(lambda x,y: x*y, range(1, n+1))
print (factorial(10))









#12_14
''''@decorator可以动态实现函数功能的增加，但是，经过@decorator“改造”后的函数，和原函数相比，除了功能多一点外，有没有其它不同的地方？
在没有decorator的情况下，打印函数名：
def f1(x):
    pass
print f1.__name__
输出： f1
有decorator的情况下，再打印函数名：
def log(f):
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
@log
def f2(x):
    pass
print f2.__name__
输出： wrapper
可见，由于decorator返回的新函数函数名已经不是'f2'，而是@log内部定义的'wrapper'。这对于那些依赖函数名的代码就会失效。decorator还改变了函数的__doc__等其它属性。如果要让调用者看不出一个函数经过了@decorator的“改造”，就需要把原函数的一些属性复制到新函数中：
def log(f):
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    wrapper.__name__ = f.__name__
    wrapper.__doc__ = f.__doc__
    return wrapper
这样写decorator很不方便，因为我们也很难把原函数的所有必要属性都一个一个复制到新函数上，所以Python内置的functools可以用来自动化完成这个“复制”的任务：
import functools
def log(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
最后需要指出，由于我们把原函数签名改成了(*args, **kw)，因此，无法获得原函数的原始参数信息。即便我们采用固定参数来装饰只有一个参数的函数：
def log(f):
    @functools.wraps(f)
    def wrapper(x):
        print 'call...'
        return f(x)
    return wrapper
也可能改变原函数的参数名，因为新函数的参数名始终是 'x'，原函数定义的参数名不一定叫 'x'。请思考带参数的@decorator，@functools.wraps应该放置在哪：'''


#import time, functools 我的答案：

def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print ('call %s() in %f %s' % (f.__name__, t, unit))
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return functoolsreduce(lambda x,y: x*y, range(1, n+1))

print (factorial.__name__)





#12_15
'''在第7节中，我们在sorted这个高阶函数中传入自定义排序函数就可以实现忽略大小写排序。请用functools.partial把这个复杂调用变成一个简单的函数：
sorted_ignore_case(iterable)

要固定sorted()的cmp参数，需要传入一个排序函数作为cmp的默认值。
参考代码:
import functools  我们在sorted这个高阶函数中传入自定义排序函数就可以实现忽略大小写排序。请用functools.partial把这个复杂调用变成一个简单的函数：'''
sorted_ignore_case = functools.partial(sorted, key=lambda a:a.upper()) #不用cmp的话，sorted还有个key参数嘛
print (sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']))

#sorted_ignore_case = functools.partial(sorted, cmp=lambda s1, s2: cmp(s1.upper(), s2.upper()))











