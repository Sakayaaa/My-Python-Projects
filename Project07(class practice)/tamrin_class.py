
lesson_list = []

class Lesson:
    # در زمان ایجاد یک شی از این کلاس کاربر چه داده هایی را باید وارد کند
    def __init__(self, id, name, code, teacher, vahed):
        self.id = id
        self.name = name
        self.code = code
        self.teacher = teacher
        self.vahed = vahed

    def save(self):
        print(self.name , "with the code", self.code, "Saved")



# دقیقا داده هایی که در کلاس  lesson در متد __init__ تعریف شده است را وارد کن
id = 0
while input("Add Lesson? (y/n): ").lower() == "y":
    name = input("Enter Name : ")
    code = int(input("Enter Lesson Code : "))
    teacher = input("Enter Teacher : ")
    vahed = int(input("Enter Vahed : "))
    id += 1
    lesson = Lesson(id, name, code, teacher, vahed)
    lesson_list.append(lesson)
    lesson.save()


for lesson in lesson_list:
    print(lesson.__dict__)