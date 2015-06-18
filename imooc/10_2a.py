''''字符串可以通过 % 进行格式化，用指定的参数替代 %s。字符串的join()方法可以把一个 list 拼接成一个字符串。


如果我们用一个函数来替换字符串的格式化代码，可以得到更清晰的代码：
def generate_tr(name, score):
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
tds = [generate_tr(name, score) for name, score in d.iteritems()]
这样，只需要修改 generate_tr() 函数，必要的时候把score标红。
'''

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }

def generate_tr(name, score):   #注意程序结构
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
tds = [generate_tr(name, score) for name, score in d.items()]

print ('<table>')
print ('<tr><th>Name</th><th>Score</th><tr>')
print ('\n'.join(tds))
print ('</table>')