#71.编写input()和output()函数输入，输出5个学生的数据记录。

class Student:
    name = ''
    age = 0
    score = [None]*3

    def input(self):
        self.name = input('input name:')
        self.age = int(input('input age:'))
        for i in range(len(self.score)):
            self.score[i] = int(input('input %d score:'%(i+1)))

    def output(self):
        print('name:',self.name)
        print('age:',self.age)
        for i in range(len(self.score)):
            print('input %d score:'%(i+1),self.score[i])

if __name__ == "__main__":
    n = 2
    stu = [Student()]*n

    for i in range(len(stu)):
        stu[i].input()

    for i in range(len(stu)):
        stu[i].output()