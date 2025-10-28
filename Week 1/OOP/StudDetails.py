from OOP.College import College
class StudentDetails(College):
    def __init__(self,roll_no,name,m1,m2,m3,ccode,cname):
        super().__init__(ccode,cname)
        self.__roll_no=roll_no
        self.__name=name
        self.__m1=m1
        self.__m2=m2
        self.__m3=m3

        def get_roll_no(self):
            return self.__roll_no
        def set_roll_no(self):
            self.__roll_no=roll_no

        @property
        def _name(self):
            return self.__name
        @name.setter
        def _name(self):
            self.__name=name

        def get_m1(self):
            return self.__m1
        def set_m1(self):
            self.__m1=m1

        def get_m2(self):
            return self.__m2
        def set_m2(self):
            self.__m2=m2

        def get_m3(self):
            return (self.__m3)
        def set_m3(self):
            self.__m3=m3

    def calc_total(self):
        self.total=self.__m1+self.__m2+self.__m3

    def calc_avg(self):
        return self.calc_total()/3