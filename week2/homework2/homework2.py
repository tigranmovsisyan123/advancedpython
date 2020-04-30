#1
def bisect_position(l:list,n:int):
    for i in l:
        if i <= n:
            pass
        else:
            return l.index(i)
    return len(l)

#2
def all_sums(num):
    return [(i,num-i) for i in range(1,num//2+1)]


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

#6
def sort_list(lst,order ="ascending"):
    for i in range(len(lst)): 
        min_idx = i 
        for j in range(i+1, len(lst)): 
            if lst[min_idx] > lst[j]: 
                min_idx = j 
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
    if order == 'ascending' :
        return lst
    elif order == 'descending' :
        return list(reversed(lst))
