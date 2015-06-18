class Person(object):

    def __init__(self, name, score):
        self.name=name
        self.score=score

    def get_grade(self):
        if self.score>=90:
            return 'A'
        elif self.score<60:
            return 'C'
        else:
            return 'B'
            
    def __str__(self):
        return '(Student: %s, %s)' % (self.name, self.score)
    __repr__ = __str__

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)


print (p1)
print (p2.get_grade())
print (p3.get_grade())