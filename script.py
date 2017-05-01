import random

teacher_Names = ['Mrs. Janet', 'Mr. Wallace', 'Miss Molly', 'Mr. Rodgers', 'Miss Rooney', 'Mr. Edwin', 'Mrs. Ruth', 'Mr. Richards', 'Mr.Evans', 'Mrs.Karkins', 'Mrs.Tae', 'Mr.Ruby', 'Mr.Stone', 'Ms. Schafer', 'Mrs. Finney']
random.shuffle(teacher_Names)
Grade = ['K', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
teacher_dict = dict(zip(teacher_Names, Grade))


student_Names = ['Bill', 'Bob', 'Janet', 'James', 'April', 'Suzy', 'Ethan', 'Rachel', 'Evan', 'Melissa', 'Carter', 'Toby', 'Wendy', 'Sally', 'Susan', 'Margie', 'Clement', 'Wally', 'Regina', 'Markus', 'Teresa', 'Yuko', 'Daisy', 'Clarissa']
student_Teacher = []
student_list = []

def generate_GPA(student):
    return randint(0,100)

def fname(arg):
    pass
