#Python中，迭代永远是取出元素本身，而非元素的索引。变成了类似：
#[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]
#因此，迭代的每一个元素实际上是一个tuple：


L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print (index+1,'-',name)
