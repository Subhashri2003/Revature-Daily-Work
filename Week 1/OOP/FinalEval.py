from StudExCurr import StudExCurr
from TeacherDetails import TeacherDetail

class FinalEval(StudExCurr,TeacherDetail):
    def __init__(self,ccode,cname,rollno,sname,m1,m2,m3,exm1,exm2,empid,tname,
                 dept,feedbackfromteacher):
        TeacherDetail.__init__(self, ccode=ccode, cname=cname,empid= empid,tname= tname,dept=dept)
        StudExCurr.__init__(self, ccode, cname, rollno, sname, m1, m2, m3, exm1, exm2)

        self.feedbackfromteacher = feedbackfromteacher