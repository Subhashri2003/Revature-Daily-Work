class College:
    def __init__(self,ccode,cname):
        self._ccode = ccode
        self._cname = cname
    @property
    def ccode(self):
        return self._ccode
    @property
    def cname(self):
        return self._cname

    def display(self):
        return self._ccode,self._cname