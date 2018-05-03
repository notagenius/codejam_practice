import math,string,itertools,fractions,heapq,collections,re,array,bisect,random

'''
#Way: While True
class LineOff:
    def movesToDo(self, points):
        int_move = 0
        l_p = list(points)
        act = True
        while(True):
            act = False
            for i in range(0,len(l_p)-1):
                if  l_p[i] == l_p[i+1]:
                    l_p.pop(i)
                    l_p.pop(i)
                    int_move += 1
                    act = True
                    break
            if act == False:
                break
        return int_move
'''

'''
#Way: Stack
class LineOff:
    def movesToDo(self,pts):
        stack = []
        ans = 0
        for x in pts:
            if stack and stack[-1] == x:
                print stack
                stack.pop()
                ans += 1
            else:
                print stack
                stack.append(x)
        return ans
'''

'''
#Way: Don't Pop in for without Break
import math,string,itertools,fractions,heapq,collections,re,array,bisect,random

class LineOff:
    def movesToDo(self, points):
        int_move = 0
        l_p = list(points)
        l_p_ae = list()
        len_l_p = len(l_p)
        len_l_p_ae = 0
        while(len_l_p > len_l_p_ae):
            len_l_p = len(l_p)
            l_p_ae = l_p[:]
            index = []
            for i in range(0,len(l_p_ae)-1):
                if  l_p_ae[i] == l_p_ae[i+1]:
                    index.append(i)
            remove = []
            for k in range(1,len(index)):
                if index[k]-index[k-1] == 1:
                    remove.append(k)
            remove.reverse()
            
            for k in range(0,len(remove)):
                index.pop(remove[k])

            index.reverse()
            for j in index:
                    l_p_ae.pop(j)
                    l_p_ae.pop(j)
                    int_move += 1
            len_l_p_ae = len(l_p_ae)
            l_p = l_p_ae[:]
        return int_move
'''

class LineOff:
    def movesToDo(self,pts):
        for i in range(0, len(pts)):
            if pts[i] == pts[i+1]:
                print pts
                return 1 + self.movesToDo(pts[:i]+pts[i+2:])
        return 0

test = LineOff()
s = "cabbbbbbac"
print test.movesToDo(s)

'''
Problem Statement
    
You are given a set of colored points on a straight line.
You play a game with these points. The game is a sequence of moves. In each move you have to erase two points that are adjacent and share the same color. (Two points are adjacent if there is no other point between them. Distances don't matter.)
You are given the string points. Each character of points describes the color of one point, in the order in which they are arranged on the line at the beginning of the game. (Different letters represent different colors.) Compute and return the maximum number of moves you can make.
Definition
    
Class:
LineOff
Method:
movesToDo
Parameters:
string
Returns:
integer
Method signature:
def movesToDo(self, points):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
256
Constraints
-
points will contain between 1 and 50 characters, inclusive.
-
Each character in points will be a lowercase English letter ('a'-'z').
Examples
0)

    
"abba"
Returns: 2
The only valid first move is to erase the two points of color 'b'. After that move the points of color 'a' are now adjacent and they can be removed in our second move.
1)

    
"zwwwzffw"
Returns: 2
You can remove two 'w' points and two 'f' points with your first two moves. After that the remaining points on the line will be arranged as follows: "zwzw". In this situation you don't have any adjacent points that share the same color, so there are no more moves.
2)

    
"rrrrrrr"
Returns: 3
With an odd number of points, at least one of them will have no pair.
3)

    
"dfghj"
Returns: 0
All colors are different so no points can be removed.
4)

    
"wasitacarooracatisaw"
Returns: 10

This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
'''


