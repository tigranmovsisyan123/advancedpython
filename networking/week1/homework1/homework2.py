#1
def bisect_position(l:list,n:int):
    for i in range(len(l)):
        if l[i] >= n:
            return i
        if n > max(l):
            return len(l)


#2
def all_sums(num):
    if num%2==1:
        return [(i,num-i) for i in range(1,num//2+1)]
    else: 
        return [(i,num-i) for i in range(1,num//2)]


#3
from collections import defaultdict 

def duplicate_characters(strr):
    d = defaultdict(int)
    sett = set()
    for i in strr:
        d[i] += 1
        if d[i] > 1 and i != ' ':
            sett.add(i)
   
    return sett

#4
def compare_lists(l1,l2):
    if len(l1) != len(l2):
        return False
    if(all(i in l1 for i in l2)):
        return True


#5
def heapq(l,a):
    for i in range(len(l)):
        if l[i] >= a:
            l.insert(i,a)
            return l
        if a > max(l):
            l.append(a)
            return l