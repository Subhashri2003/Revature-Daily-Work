from StudDetails import StudentDetails
class StudExCurr(StudentDetails):
        def __init__(self,ccode,name,roll_no,m1,m2,m3,cname,exam1,exam2):
            super().__init__(self,ccode,name,roll_no,m1,m2,m3,cname)
            self.exam1=exam1
            self.exam2=exam2
        def calc_extot(self):
            return self.exam1+self.exam2
