__author__ = "Muhammed Mahir Varlioglu"
__email__ = "mmahirv@hotmail.com"

class School:
    def __init__(self, name, foundation_year, students, teachers):
        self.name = name
        self.foundation_year = foundation_year
        self.students = students
        self.teachers = teachers

    def add_new_student(self, student_name, class_name):
        student = {"name": student_name, "class_name": class_name}
        self.students.append(student)
        
    def add_new_teacher(self, teacher_name, branch):
        teacher = {"name": teacher_name, "branch": branch}
        self.teachers.append(teacher)
        
    def view_student_list(self):
        for student in self.students:
            print(f"Student Name: {student['name']}, Class: {student['class_name']}")
    
    def view_teacher_list(self):
        for teacher in self.teachers:
            print(f"Teacher Name: {teacher['name']}, Branch: {teacher['branch']}")
            

roc_school = School("ROC School", 1990, 
                    [
                        {
                            "name": "John Doe",
                            "class_name": "10A"
                        }, {
                            "name": "Alice Johnson",
                            "class_name": "11B"
                        }
                    ], 
                    [
                        {
                            "name": "Jane Smith",
                            "branch": "Mathematics"
                        }, {
                            "name": "Robert Brown",
                            "branch": "Physics"
                        }
                    ])

roc_school.add_new_student("Emily Davis", "12C")
roc_school.add_new_teacher("Michael Wilson", "Chemistry")   

roc_school.view_student_list()
roc_school.view_teacher_list()