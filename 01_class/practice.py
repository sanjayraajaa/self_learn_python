class Student():
    def __init__(self,name):
        self._name = name
        self.__grade = []
    
    def add_grade(self, grade):
        self.__grade.append(grade)
    
    def get_average(self):
        average = sum(self.__grade) / len(self.__grade)
        return average

a = Student("Sanjay")
a.add_grade(50)
a.add_grade(100)
a.add_grade(50)
a.add_grade(100)

print(a.get_average())