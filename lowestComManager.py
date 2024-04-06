class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
        
def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
    pass

def getDepth(topManager, report):
    d = 0
    while topManager is not report:
        topManager = topManager.directReports
        d += 1
    return d
A = OrgChart("A")
B = OrgChart("B")
C = OrgChart("C")
D = OrgChart("D")
E = OrgChart("E")
F = OrgChart("F")
G = OrgChart("G")
H = OrgChart("H")
I = OrgChart("I")
A.directReports.append(B)
A.directReports.append(C)
B.directReports.append(D)
B.directReports.append(E)
C.directReports.append(F)
C.directReports.append(G)
D.directReports.append(H)
D.directReports.append(I)