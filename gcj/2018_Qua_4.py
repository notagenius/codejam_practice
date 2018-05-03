item_num = int(raw_input()) 

def solve(A): 
    if A <= 2**0.5:
        cos = float((A+(2-A*A)**0.5)/2)
        sin = float((A-(2-A*A)**0.5)/2)
        face0 = [0.5*cos, 0.5*sin, 0]
        face1 = [-0.5*sin, 0.5*cos, 0]
        face2 = [0, 0, 0.5]
        return face0, face1, face2
    else:
        cos = float(A / (2*(2**0.5)))
        sin = float((1-(A*A/8))**0.5)
        squ = float((2**0.5)/4)
        face0 = [squ, squ*cos, squ*sin]
        face1 = [-squ, squ*cos, squ*sin]
        face2 = [0, -0.5*sin, 0.5*cos]
        return face0, face1, face2
                
        


for i in xrange(1, item_num+1):
    A = float(raw_input())
    face0, face1, face2 = solve(A)
    print "%s%d%s" %("Case #", i, ": ")
    print "%s%s%s%s%s" %(face0[0], " ", face0[1], " ", face0[2])
    print "%s%s%s%s%s" %(face1[0], " ", face1[1], " ", face1[2])
    print "%s%s%s%s%s" %(face2[0], " ", face2[1], " ", face2[2])
    
