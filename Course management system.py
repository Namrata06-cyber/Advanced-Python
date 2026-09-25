class Course:
    def __init__(self, name, duration, fee):
        self.name = name
        self.duration = duration
        self.fee = fee

    def category(self):
        if self.duration <= 6:
            return "Short-Term"
        else:
            return "Long-Term"

    def display(self):
        print("Course Name:", self.name)
        print("Duration:", self.duration, "months")
        print("Fee: ₹", self.fee)
        print("Category:", self.category())
        print("------------------------")


class Institute:
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def display_courses(self):
        print("\nAll Courses:")
        print("========================")
        for course in self.courses:
            course.display()



institute = Institute()

n = int(input("Enter number of courses: "))

for i in range(n):
    print("\nEnter details of Course", i + 1)
    name = input("Course Name: ")
    duration = int(input("Duration (in months): "))
    fee = float(input("Fee: "))

    course = Course(name, duration, fee)
    institute.add_course(course)

institute.display_courses()