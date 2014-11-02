# Golfed mini-intepreter (no debug, cell_max=256)
# Bytes: 

# Vars
F = "examples/multiply2.b"
C = 256

#----------------------------
with open(F,'r')as z:p=z.read()
t=[0]*30000
i =0
d = 0
l = 0
while i < len(p):
    f = True  
    c = p[i]
    x= t[d]
    if c == ">":d += 1
    if c == "<":d -= 1
    if c == "+":t[d] = (x+ 1) % C
    if c == "-":t[d] = (x- 1) % C
    if c == ".":print(chr(x), end="")
    if c == ",":t[d] = ord(input())         
    if c == "[" and x== 0:
        f = False        
        l = 1     
        while l > 0:
            i += 1
            c = p[i]
            if c == "[":l += 1
            if c == "]":l -= 1
        i += 1         
    if c == "]" and x!= 0:
        f = False
        l = 1
        while l > 0:
            i -= 1
            c = p[i]
            if c == "[":l -= 1
            if c == "]":l += 1          
        i += 1
    if f:i += 1