# Golfed mini-intepreter
# Bytes: 294
# Overflow undefined
# For finding matching [ ] braces, replace + with -
# Use bool string multiplication to remove strings

# Global parameters
F = "examples/multiply2.b"
#C = 256
T = 30000
#----------------------------
p=open(F).read()
t=[0]*T
i=d=0
y="><+-.,[]"
w="while l>0:i+=1;c=p[i];l+=(c=='[')-(c==']')"
while i<len(p):
 c=p[i];x=t[d];a=8;l=1
 if c in y:a=y.index(c)
 exec(("d+=1|d-=1|t[d]+=1|t[d]-=1|print(chr(x),end='')|t[d]=ord(input())|"+(x==0)*w+"|"+(x!=0)*w.replace('+','-')+"|1").split('|')[a])
 i+=1


