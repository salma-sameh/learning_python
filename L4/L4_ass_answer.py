import json
# -------------------- Person Base Class --------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


# -------------------- Student Class --------------------
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def __str__(self):
        return f"Student [{self.student_id}] - {super().__str__()} | Courses: {self.courses}"


# -------------------- Teacher Class --------------------
class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.subjects = []

    def __str__(self):
        return f"Teacher [{self.teacher_id}] - {super().__str__()} | Subjects: {self.subjects}"


# -------------------- Course Class --------------------
class Course:
    def __init__(self, course_id, name, teacher=None):
        self.course_id = course_id
        self.name = name
        self.teacher = teacher
        self.students = []

    def __str__(self):
        teacher_name = self.teacher.name if self.teacher else "No Teacher"
        return f"Course [{self.course_id}] - {self.name}, Teacher: {teacher_name}, Students: {[s.name for s in self.students]}"


# -------------------- School Class --------------------
class School:
    def __init__(self):
        self.students = {}
        self.teachers = {}
        self.courses = {}

    # ---------- Student Management ----------
    def add_student(self, student): # this function take object
        try:
            self.students[student.student_id] = student
        except Exception as e:
            print("Error adding student:", e)

    def remove_student(self, student_id): # this fuction take student id (key)
        try:
            del self.students[student_id]
        except KeyError:
            print("Student not found (key not found)")

    # ---------- Teacher Management ----------
    def add_teacher(self, teacher):
        try:
            self.teachers[teacher.teacher_id] = teacher
        except Exception as e:
            print("Error adding teacher:", e)

    def remove_teacher(self, teacher_id):
        try:
            del self.teachers[teacher_id]
        except KeyError:
            print("Teacher not found")

    # ---------- Course Management ----------
    def add_course(self, course):
        try:
            self.courses[course.course_id] = course
        except Exception as e:
            print("Error adding course:", e)

    # ---------- Enroll Student ----------
    def enroll_student(self, student_id, course_id):
        try:
            student = self.students[student_id]
            course = self.courses[course_id]

            course.students.append(student)
            student.courses.append(course.name)

        except KeyError:
            print("Student or Course not found")

    # ---------- Assign Teacher ----------
    def assign_teacher(self, teacher_id, course_id):
        try:
            teacher = self.teachers[teacher_id]
            course = self.courses[course_id]

            course.teacher = teacher
            teacher.subjects.append(course.name)

        except KeyError:
            print("Teacher or Course not found")

    # ---------- Display Info ----------
    def display_all(self):
        print("\n--- Students ---")
        for student in self.students.values():
            print(student)

        print("\n--- Teachers ---")
        for teacher in self.teachers.values():
            print(teacher)

        print("\n--- Courses ---")
        for course in self.courses.values():
            print(course)

    # ---------- Save Data ----------
    def save_data(self, filename="school_data.json"):
        try:
            data = {
                "students": {sid: vars(s) for sid, s in self.students.items()},
                "teachers": {tid: vars(t) for tid, t in self.teachers.items()},
                "courses": {cid: {"course_id": c.course_id, "name": c.name} for cid, c in self.courses.items()},
            }

            with open(filename, "w") as f:
                json.dump(data, f, indent=4)

            print("Data saved successfully")

        except Exception as e:
            print("Error saving data:", e)

    # ---------- Load Data ----------
    def load_data(self, filename="school_data.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            for sid, s in data["students"].items():
                self.students[sid] = Student(s["name"], s["age"], sid)

            for tid, t in data["teachers"].items():
                self.teachers[tid] = Teacher(t["name"], t["age"], tid)

            for cid, c in data["courses"].items():
                self.courses[cid] = Course(c["course_id"], c["name"])

            print("Data loaded successfully")

        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Error loading data:", e)


# -------------------- Demo run the system --------------------
if __name__ == "__main__":

    school = School()

    # Sample Data Creation
    s1 = Student("Salma", 21, "S1")
    s2 = Student("Ali", 22, "S2")

    t1 = Teacher("Dr. Ahmed", 40, "T1")

    c1 = Course("C1", "Python")
    c2 = Course("C2", "AI")

    school.add_student(s1)
    school.add_student(s2)

    school.add_teacher(t1)

    school.add_course(c1)
    school.add_course(c2)

    # Assign teacher
    school.assign_teacher("T1", "C1")

    # Enroll students
    school.enroll_student("S1", "C1")
    school.enroll_student("S2", "C2")

    # Display all data
    school.display_all()

    # Save & Load demo
    school.save_data()
    school.load_data()
