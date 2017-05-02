import random
# **Create a Python module** that generates a K-12 school with students and teachers at every grade level. Make sure to appropriately document your code. Show us what you can do!
#
# Data Representation
# -------------------
#
# 1. Your school should have a name, and can have many students and many teachers.
# 2. Students should have names, GPAs (out of 100), grade level (K - 12), and a teacher name.
# 3. Teachers should have names and grade levels, and should be able to have multiple students.
# 4. A teacher should have no more than 10 students.
# 5. If there are no teachers, there should be no students.

class teacher(object):
    """docstring for teacher."""
    def __init__(self, name, grade, **kargs):
        self.name = name
        self.grade = grade
        self.students = []

class student(object):
    """docstring for student."""
    def __init__(self, name, teacher, **kargs):
        self.name = name
        self.teacher = teacher
        self.gpa = random.randint(0,100)
        self.grade = teacher.grade


teacher_Names = ['Mrs. Janet', 'Mr. Wallace', 'Miss Molly', 'Mr. Rodgers', 'Miss Rooney', 'Mr. Edwin', 'Mrs. Ruth', 'Mr. Richards', 'Mr.Evans', 'Mrs.Karkins', 'Mrs.Tae', 'Mr.Ruby', 'Mr.Stone', 'Ms. Schafer', 'Mrs. Finney']
student_Names = ['Bill', 'Bob', 'Janet', 'Reggie', 'Angel', 'Abbie', 'Tommy', 'Peter', 'Adrian', 'James', 'April', 'Suzy', 'Ethan', 'Rachel', 'Evan', 'Melissa', 'Carter', 'Toby', 'Wendy', 'Sally', 'Susan', 'Margie', 'Clement', 'Wally', 'Regina', 'Markus', 'Teresa', 'Yuko', 'Daisy', 'Clarissa' ,'Firdos', 'Khaleel', 'Mazin', 'Isa', 'Yasin', 'Nasim', 'Leila', 'Al-Amir', 'Haamid']
Grade = ['K', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
random.shuffle(teacher_Names)
random.shuffle(student_Names)

school = [teacher(name, grade) for name, grade in zip(teacher_Names, Grade)]
for clsroom in school:
    for i in range(0, 3):
        cur_studnt = student(student_Names.pop(), clsroom)
        clsroom.students.append(cur_studnt)
        
