#HIriarical Inheritance
class person:
    def setPrsone(self,name,addr):
        self.name=name
        self.addr=addr
    def getPers(self):
        print("Name ",self.name)
        print("Address ",self.addr)

class student(person):
    def setStudent(self,rollno,marks):
        self.rollno=rollno
        self.marks=marks
    def getStudent(self):
        print("Roll No ",self.rollno)
        print("Marks ",self.marks)

class teacher(person):
    def setteacher(self,exp,sal):
        self.exp=exp
        self.sal=sal

    def getteacher(self):
        print("Experienc",self.exp)
        print("Salary",self.sal)

s1=student()
t1=teacher()
s1.setPrsone("A","ba")
s1.setStudent(101,45)
t1.setPrsone("AMAN","Damoh")
t1.setteacher("BA",20000)

s1.getPers()
s1.getStudent()
t1.getPers()
t1.getteacher()
