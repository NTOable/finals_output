class School :
    def __init__(self, name : str, student_count : int) :
        self.name = name
        self.student_count = student_count
        self.students = []
    #method to make output print more efficient
    def add_student(self, student) :
        self.students.append(student)

class Students :
    def __init__(self, first_name : str, last_name : str,
                 math : float, sci : float, eng : float, comp : float) :
        self.first_name = first_name
        self.last_name = last_name
        self.math = math
        self.sci = sci
        self.eng = eng
        self.comp = comp

    def get_avg(self) :
        total_grade = (self.math + self.sci
                     + self.eng + self.comp)
        average = total_grade / 4
        return average

    def get_gpa(self) :
        (math_credit, sci_credit,
         eng_credit, comp_credit) = (self.math, self.sci,
                                    self.eng, self.comp)
        total_credit = (math_credit + sci_credit
                            + eng_credit + comp_credit) / 4
        gpa = (total_credit / 100) * 4
        return gpa

class SchoolOne(School) :
    pass

class SchoolTwo(School) :
    pass

#instances (school)
schoolone = SchoolOne("Harvard & Yale", 5)
schooltwo = SchoolTwo("Langston State", 4)

#instances (harvard yale students)
hystudent1 = Students("Jake", "Lyle", 80.00, 80.00, 78.00, 68.00)
hystudent2 = Students("Carl", "McCan", 90.00, 76.00, 89.00, 93.00)
hystudent3 = Students("Shaun", "Jones", 76.00, 85.00, 92.00, 85.00)
hystudent4 = Students("Nick", "Hayes", 89.00, 85.00, 92.00, 87.00)
hystudent5 = Students("Kyle", "Lothar", 88.00, 97.00, 83.00, 94.00)

schoolone.add_student(hystudent1)
schoolone.add_student(hystudent2)
schoolone.add_student(hystudent3)
schoolone.add_student(hystudent4)
schoolone.add_student(hystudent5)

#instances (langston state students)
lsstudent1 = Students("Bam", "Stein", 80.00, 88.00, 98.00, 85.00)
lsstudent2 = Students("Trevor", "Jacobs", 94.00, 82.00, 91.00, 77.00)
lsstudent3 = Students("Mike", "Schofield", 99.00, 89.00, 98.00, 92.00)
lsstudent4 = Students("Tyrone", "Smiths", 85.00, 86.00, 100.00, 93.00)

schooltwo.add_student(lsstudent1)
schooltwo.add_student(lsstudent2)
schooltwo.add_student(lsstudent3)
schooltwo.add_student(lsstudent4)

#print harvard student list
print(schoolone.name)
print(f"No. of achievers for this term: {schoolone.student_count}")
for student in schoolone.students:
    print(f"{student.first_name} {student.last_name} : AVG : {student.get_avg()} "
      f"GPA: {student.get_gpa()}")
#white space between the two lists
print()

#print langston student list
print(schooltwo.name)
print(f"No. of achievers for this term: {schooltwo.student_count}")
for student in schooltwo.students:
    print(f"{student.first_name} {student.last_name} : AVG : {student.get_avg()} "
      f"GPA: {student.get_gpa()}")
