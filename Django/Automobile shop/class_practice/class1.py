class Student:
    '''this is class'''
    clg_name='bit'

    def __init__(self):
        self.__name="sanskar jain"
        self.age=20
    def input(self):
        self.__name="sanskar"
        self.age=20
    def show(self):
        print(f"name: {self._Student__name}")
        print(f"age: {self.age}")
        print(f"colege name: {Student.clg_name}")
s1=Student()
s1.input()
print(s1._Student__name)
s1.show()