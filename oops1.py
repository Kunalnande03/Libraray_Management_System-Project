class student:
    def setstudent(self ,rollno,name):
        self.rollno=rollno
        self.name=name
        
    def getstudent(self):
        print("Roll No.",self.rollno)
        print("Name",self.name)


s1=student()
s1.setstudent(101,"A")
s1.getstudent()