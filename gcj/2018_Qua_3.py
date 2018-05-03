import random
import sys
item_num = int(raw_input()) 

def solve(A): 
    print 500+random.randint(-A,A),500+random.randint(-A,A)
    sys.stdout.flush()
    s = raw_input()
    if s == "0 0":
        return
    else:
        solve(A)
                
        


for i in xrange(1, item_num+1):
    squ = int(raw_input()) ** 0.5
    if squ%2 == 1:
        squ += squ
    A = int(round((squ-2)/2))
    solve(A)
