#1 
def all_positive(arg,*args):
    return min([arg,args])<0

#2
def xor3(a,b,c):
    return bool((a or b) and not (a and b) or  (b or c) and not (b and c))

#3
def mirror_string(strr):
    code = {"a":"z", "b":"y", "c":"x" ,"d":"w" ,"e":"v", "f":"u", "g":"t", "h":"s", "i":"r","j":"q","k":"p","l":"o", "m":"n", "n":"m", "o":"l", "p":"k", "q":"j", "r":"i", "s":"h", "t":"g", "u":"f", "v":"e", "w":"d","x":"c", "y":"b", "z":"a", "A":"Z", "B":"Y", "C":"X" ,"D":"W" ,"E":"V", "F":"U", "G":"T", "H":"S", "I":"R","J":"Q","K":"P","L":"O", "M":"N", "N":"M", "O":"L", "P":"K", "Q":"J", "R":"i", "S":"H", "T":"G", "U":"F", "V":"E", "W":"D","X":"C", "Y":"B", "Z":"A"," ":" "}
    reverse = ""
    for x in strr:
        if x in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRQRSTUWXYZ ":
            reverse += code[x]
        else:
            reverse+=x
    
    return reverse
            
#4







#5
def binary_sum(a,b):
    int_sum = int(a, 2) + int(b, 2)
    return int_sum 

#6

def only_names(name):
    if len(name) != 0:
        return name

#7
discriminant = lambda a,b,c: b**2 - 4*a*c

#8
full_name  = lambda a,b:a + ' '+ b
