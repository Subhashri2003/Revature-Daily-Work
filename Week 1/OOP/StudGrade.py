#from student details import Stud
from OOP.StudExCurr import   StudExCurr
from TeacherDetails import TeacherDetail
from FinalEval import  FinalEval
#multilevel Inheritence
ccode = input('ccode: ')
cname = input('cname: ')
rollno = int(input("Roll no: "))
sname = input("Name: ")
m1 = int(input("Mark 1: "))
m2 = int(input("Mark 2: "))
m3 = int(input("Mark 3: "))
exm1=int(input("Ex mark 1: "))
exm2=int(input("Ex mark 2: "))

'''#stud = StudExCurr(ccode,cname,rollno,sname,m1,m2,m3,exm1,exm2)

print(f'{stud.display()[0]} \t {stud.display()[1]}' )
print(f'{stud.get_rollno()}\n {stud.get_sname()}\n '
      f'{stud.calc_tot()}\n {stud.calc_avg()}')
print(f'{stud.calc_extot()}')'''


#herarical Inheritance
empid = int(input('Empid: '))
tname = input('Tname: ')
dept = (input('Dept: '))

'''teacher = TeacherDetail(ccode,cname,empid,tname,dept)
teacher.display()'''

feedbackfromteacher = input('Enter Feedback: ')
fe = FinalEval(ccode= ccode,cname=cname,rollno=rollno,sname=sname,m1=m1,m2=m2,m3=m3,exm1=exm1,exm2=exm2,
               empid=empid,tname=tname,dept=dept,feedbackfromteacher=feedbackfromteacher)

print(f'{fe.display()}\n'
      f'{fe.get_rollno()}\n '
      f'{fe.get_sname()} \n'
      f'{fe.calc_tot()}\n '
      f'{fe.calc_avg()}\n'
      f'{fe.calc_extot()}\n'
      #f'{fe.display()}\n'
      f'{fe.feedbackfromteacher}')