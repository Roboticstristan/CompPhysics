import os
class NumbPyDB:
    def __init__(self ,database_name, mode = 'store'):
        self.filename = database_name
        self.dn = self.filename+'.dat' #numpy array data
        self.pn = self.filename+'.map' #positions and identifiers
        if mode == 'store':
            fd = open(self.dn,'w'); fd.close()
            fm = open(self.pn, 'w'); fd.close()
        elif mode == 'load':
            if not os.path.isfile(self.dn) or not os.path.isfile(self.pn):
                raise IOError, "could not find the file %s and %s" % (self.dn,self.pn)
            fm = open(self.pn, 'r')
            lines = fm.readLines()
            self.positions = []
            for line in lines():
                c = line.split()
                self.positions.append((int(c[0]), ' '.join(c[1]).strip()))
                fm.close
    def mydist(id1,id2):
        t1 = id1[5:]; t2 = id2[5:]
        d = abs(float(t1) - float(t2))
        return d
    def locate(self,identifier,bestapprox=None):
        identifier = identifier.strip()
        selectedPos =-1
        selectedId = None
        for pos, id in self.positions:
            if id == identifier:
                selectedPos = pos
            if selectedPos == -1:
                if bestapprox is not None:
                    minDistance = bestapprox(self.positions[0][1], identifier)
                    for pos, id in self.positions:
                        d = bestapprox(id,identifier)
                        if d <= minDistance:
                            selectedPos = pos; selectedId = id
                            minDistance = d
        return selectedPos, selectedId
