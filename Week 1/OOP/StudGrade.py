#from StudDetails import StudentDetails
from StudExCurr import StudExCurr

roll_no=int(input("Enter your roll no: "))
name=(input("Enter your name: "))
m1=int(input("Enter your mark1: "))
m2=int(input("Enter your mark2: "))
m3=int(input("Enter your mark3: "))
ccode=(input("Enter your code: "))
cname=(input("Enter your  College name: "))
exam1=int(input("Enter your excurr mark 1: "))
exam2=int(input("Enter your excurr mark 2: "))


stud=StudExCurr(roll_no,name,m1,m2,m3,exam1,exam2,ccode,cname)
    #(StudentDetails(ccode,cname,roll_no,name,m1,m2,m3))
print(f'{stud.display()[0]}\t {stud.display()[1]}')
print(f'{stud.roll_no}\n {stud.name}\n {stud.calc_total()}\n {stud.calc_avg()}')
print(f'{stud.calc_extot()}')
