from OOP.College import College
class TeacherDetail(College):
    def __init__(self,ccode,cname,empid,tname,dept):
        College.__init__(self, ccode,cname)
        self.empid = empid
        self.tname = tname
        self.dept = dept

    def display(self):
        print(f'{self._ccode}\t {self._cname}\n'
              f'{self.empid}\t {self.tname}\t {self.dept}')