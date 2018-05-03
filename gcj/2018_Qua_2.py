item_num = int(raw_input()) 

def solve(num, list_in):
    single = []
    double = []
    s = True
    ok = True
    for i in list_in:
        if s:
            single.append(i)
        else:
            double.append(i)
        s = not s
    single = sorted(single)
    double = sorted(double)
    for i in xrange(0, num-1):
        if i%2==0:
            cur = i/2
            if single[cur] > double[cur]:
                ok = False
                return ok, i
        else:
            cur = (i-1)/2
            if double[cur] > single[cur+1]:
                ok = False
                return ok, i
    return ok, -1


for i in xrange(1, item_num+1):
    num = int(raw_input())
    list_in = map(lambda x:int(x),raw_input().split())
    ok, index = solve(num, list_in)
    if ok == True:
        line = "%s%d%s%s"%("Case #", i, ": ","OK")
    else:
        line = "%s%d%s%s"%("Case #", i, ": ",index)
    print line 

