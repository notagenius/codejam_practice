import re
item_num = raw_input() 
item = 1
swipe_times = 0

def swipe(string):
    global swipe_times
    updated = False
    swipe_start = -1
    swipe_end = -1
    search_result = re.finditer("CS", string)
    for m in search_result:
        swipe_start = m.start(0)
        swipe_end = m.end(0)
    if swipe_start >= 0 and swipe_end >= 0:
        updated = True
        swipe_times = swipe_times + 1
        listed = list(string)
        listed[swipe_start] = "S"
        listed[swipe_end-1] = "C"
        string = "".join(listed)
    return updated, swipe_times, string

def scoring(string):
    single_cur = 1
    damage = 0
    for i in string:
        if i == "C":
            single_cur = single_cur * 2
        if i == "S":
            damage = damage + single_cur
    return damage

def solve(score, string):
    global swipe_times
    while int(scoring(string)) > int(score):
        updated, swipe_times, string = swipe(string)
        if updated == False:
            return "IMPOSSIBLE"
    return swipe_times


while (item <= int(item_num.strip())):
    current_line = raw_input().strip().split(' ')
    score = current_line[0]
    string = current_line[1]
    item = item + 1
    line = "%s%d%s%s"%("Case #", item-1, ": ",solve(score, string))
    print line 
    swipe_times = 0

