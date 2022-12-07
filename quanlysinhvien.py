class Student:
    def __init__(self, student_id, name, dob, address, cls):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.address = address
        self.st_cl = cls
        
    def print_informatin():
        print("Information of the student: ")
        print('id = ',self.student_id)
        print('name: ',self.name)
        print('dob: ',self.dob)
        print('address: ',self.address)
        print('class: ', self.cls, "\n")
        
        
class Studentlist:
    def __init__(self):
        self.student_list = []
    #in thông tin sinh viên
    def print_student(self):
        for student in self.student_list:
            student.print_information()
        
    
    #Thêm sinh viên mới:
    def add_student(self):
        print('Please input student information')
        student_id = int(input("student_id: "))
        name = input("name: ")
        dob = input("dob: ")
        address = input("address: ")
        cls = input("class: ")
        new_student = Student(student_id, name, dob, address, cls)
        self.student_list.append(new_student)
    
    #Tìm kiếm thông tin sinh viên theo id:
    def find_student_by_id(self):
        student_id = int(input('Input student id: '))
        index = -1
        for i in range(len(self.student_list)):
            if self.student_list[i].student_id == student_id:
                index = 1
            return index
        
     #Tìm kiếm thông tin sinh viên theo tên
    def find_student_by_name(self):
        name = input("Name of student: ")
        result_students = []
        for i in range(len(self.student_list)):
            if self.student_list[i].name == name:
                result_students.append(self.student_list[i])
                
        if len(result_students) == 0:
            print("Not found student name")
        else:
            for student in result_students:
                student.print_information()
        
    #Cập nhật thông tin sinh viên theo id:
    def update_student_information(self, name, dob, address, cls):
        index_of_student = self.find_student_by_id()
        if index_of_student == -1:
            print("Not found student id")
        else:
            self.student_list[index_of_student].name = name
            self.student_list[index_of_student].dob = dob
            self.student_list[index_of_student].address = address
            self.student_list[index_of_student].cls = cls
                            
                
    #Xóa thông tin sinh viên theo id:
    def delete_student(self):
        student_id = int(input("Student id: "))
        index = -1
        for i in range(len(self.student_list)):
            if self.student_list[i].student_id == student_id:
                index = 1
        if index == -1:
            print("Not found student id")
        else: 
            del self.student_list[index]
            
 
    # Sắp xếp sinh viên
    def sort_student(self):
        # sort_by_id
        self.student_list = sorted(self.student_list, key = lambda x : x.name)
    
        
        
   
        
#Tạo đối tượng của lớp Studentlist để sử dụng
studentlist = Studentlist()

while True:
    option = int(input("Selcet function: \n \
                        1. View student \n \
                        2. Add new student \n \
                        3. Update student \n \
                        4. Delete student \n \
                        5. Find student \n \
                        6. Sort student \n"))
    if option == 1:
        studentlist.print_student()
    elif option == 2:
        studentlist.add_student()
    elif option ==3:
        print("Please input student information:")
        name = input("Name: ")
        dob = input("Dob: ")
        address = input("Address: ")
        cls = input("Class: ")
        studentlist.update_student_information(name, dob, address, cls)
    elif option == 4:
        studentlist.delete_student()
    elif option == 5:
        studentlist.find_student_by_name()
    elif option ==6:
        studentlist.sort_student()
    else:
        print("Invalid option")
    
    y_o_n = input("Continue? [Y/N]: ")
    if y_o_n.lower() == 'N':
        break