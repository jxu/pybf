# Golfed mini-intepreter
# Bytes: 307
# Overflow undefined

# Global parameters
F = "examples/multiply2.b"
#C = 256
T = 30000
#----------------------------
p=open(F).read()
t=[0]*T
i=d=l=0
y="><+-.,[]"
w="l=1;\n while l>0:i+=z;c=p[i];l+=z*((c=='[')-(c==']'))\n i-=1"
while i<len(p):
 c=p[i];x=t[d];a=8
 if c in y:a=y.index(c)
 exec(("d+=1|d-=1|t[d]+=1|t[d]-=1|print(chr(x),end='')|t[d]=ord(input())|if x==0:\n z=1;"+w+"|if x:\n z=-1;"+w+"|1").split('|')[a])
 i+=1


