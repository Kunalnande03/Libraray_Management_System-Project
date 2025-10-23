#Multipel Inheritance
class student:

    def setStudent(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def getStudent(self):
        print("Name ",self.name)
        print("Roll no",self.rollno)

class Sportsman:
    def setStportsman(self,sport,role):
        self.sport=sport
        self.role=role

    def getSportman(self):
        print("Sports ",self.sport)
        print("Role ",self.role)

class Allrounder(student,Sportsman):
    def setAllrounder(self,age):
        self.age=age
    def getAllrounder(self):
        print("Age ",self.age)

a1=Allrounder()
a1.setStudent("Ram",101)
a1.setStportsman("Cricket","Bowler")
a1.setAllrounder(15)

a1.getStudent()
a1.getSportman()
a1.getAllrounder()