class User():
    def __init__(self,user,name):
        self.user = user
        self.name = name
    
    def show_user_details(self):
        print(f"User Details:\n---- --------\nUser: {self.user}\nName: {self.name}\n")

class Employee():
    def __init__(self,emp_id,dept):
        self.emp_id = emp_id
        self.dept = dept
    
    def show_employee_details(self):
        print(f"Employee Details:\n-------- --------\nEmployee ID: {self.emp_id}\nDepartment: {self.dept}")

class HRMS(User,Employee):
    def __init__(self, user, name,emp_id,dept):
        User.__init__(self, user, name)
        Employee.__init__(self,emp_id,dept)
    
    def show_details(self):
        User.show_user_details(self)
        Employee.show_employee_details(self)

u1 = HRMS("sanjayraja","Sanjay Raja S","HR-EMP-0001","Frappe")
u1.show_details()