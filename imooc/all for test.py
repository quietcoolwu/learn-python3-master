class Student(object):

    def __init__(self, name, dick):
        self.name = name
        self.dick = dick
        

    @property
    def shit(self):
        return self.dick

    @shit.setter
    def fuck(self, dick1):
        self.dick = dick1
        if dick1 < 0 or dick1 > 100:
            raise ValueError('invalid score')
        #pass
        
        
    @property
    def my_grade(self):
        
        if self.dick>=80:
            return 'A'
        elif self.dick<60:
            return 'C'
        else:
            return 'B'
        
s = Student('Bob', 59)
print (s.my_grade)

s.fuck = 60
print (s.my_grade)

s.fuck = 99
print (s.my_grade)

s.fuck = 120
print (s.my_grade)
