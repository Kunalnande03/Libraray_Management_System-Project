'''class Box:
#Creating constructor
    def __init__(self,length,breadth,height):#CONSTRUCTOR
        self.length=length
        self.breadth=breadth
        self.height=height

    def getBox(self):
        print('length= ',self.length)
        print('breadth= ',self.breadth)
        print('height= ',self.height)

 # Creating manipulator for performing mathematical operation
    def volume(self):  #MANIPULATOR
        vol=self.length*self.breadth*self.height
        print('Volume is= ',vol)

box1=Box(5,3,2)
box2=Box(2,4,6)

box1.getBox()
box1.volume()
box2.getBox()
box2.volume()'''

'''class Course:
    def __init__(self,cname,duration,fees):
        self.cname=cname
        self.duration=duration
        self.fees=fees

    def getCourse(self):
        print('Course Name= ',self.cname)
        print('Time Duration= ',self.duration)
        print('Total Fees= ',self.fees)

    def calcDiscount(self):
        dis=self.fees*10/100
        print('Discount Rs. ',dis)

c1=Course('BTech',48,70000)
c2=Course('BCA',36,80000)

c1.getCourse()
c1.calcDiscount()
c2.getCourse()
c2.calcDiscount()'''
# EXAMPLE OF HIERARCHICAL INHERITANCE
class Person: #Parent class
    def setPerson(self,name,address):
        self.name=name
        self.address=address

    def getPerson(self):
        print('Name: ', self.name)
        print('Address:',self.address)


class Student(Person): # firstchildclass
    def setStudent(self,rollno,marks):
        self.rollno=rollno
        self.marks=marks

    def getStudent(self):
        print('Roll No is= ',self.rollno)
        print('Marks= ',self.marks)

class Teacher(Person): # secondchildclass
    def setTeacher(self,exp,quali):
        self.exp=exp
        self.quali=quali

    def getTeacher(self):
        print('Experience= ',self.exp)
        print('Qualification= ',self.quali)

s1=Student()
t1=Teacher()
s1.setPerson("Tatyabichu","bombay")
t1.setPerson("Manjoulika","bhanugardh")

s1.setStudent(88,45)
t1.setTeacher(200,"BHorror")

s1.getPerson()
s1.getStudent()
t1.getPerson()
t1.getTeacher()