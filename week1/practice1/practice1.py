#1
def implication3(a,b,c):
    return not b or c or not a





#2
def expr_vale(strr):
    for i in strr:
        return "{:.2f}".format(eval(strr))

#3
def quick_or(b_list):
    return (any(b_list))

#4

def ispalindrome(strr): 
      
    list1 = [] 
    
    for i in range(len(strr)): 
        if (strr[i] in list1): 
            list1.remove(strr[i]) 
        else: 
            list1.append(strr[i]) 
              
    if (len(strr)% 2 == 0 and len(list1) == 0):
        return True
    elif (len(strr) % 2 == 1 and len(list1) == 1): 
        return True
    else: 
        return False
    

#5
def last_digit(n):
    summ = 0
    for i in range(1, n+1):
        summ += i*i
        res = summ%10
    return res