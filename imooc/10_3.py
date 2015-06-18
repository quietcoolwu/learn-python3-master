#条件过滤的要点是综合语句的构造。利用 if 剔除掉非字符串的元素。e.g:而列表生成式则可以用一行语句代替循环生成上面的list：
#>>> [x * x for x in range(1, 11)]
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def toUppers(L):
    return [x.upper() for x in L if isinstance(x,str)]

print (toUppers(['Hello', 'world', 101]))
