class College:
    def __init__(self,ccode,cname):
        self._ccode=ccode
        self._cname=cname

    def display(self):
        return self._ccode,self._cname