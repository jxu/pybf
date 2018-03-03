# Golfed mini-intepreter (no exec)
# Bytes: 291
# Techniques: Replaced char matching with index y, replaced conditional addition  
# with adding boolean values (x+(a==2)), variable renaming and replacing 
# repeated expressions. Note: z is 1 or -1

# Global parameters
F = "examples/multiply2.b"
C = 256
T = 30000
#----------------------------
p=open(F).read()
t=[0]*T
i=d=l=0
y="><+-.,[]"
while i<len(p):
 c=p[i];x=t[d];a=9;l=1
 if c in y:a=y.index(c)
 t[d]=(x+(a==2)-(a==3))%C;d+=(a==0)-(a==1)
 if a==4:print(chr(x),end='')
 if a==5:t[d]=ord(input())
 if a-6==(x!=0):
  z=13-2*a
  while l>0:i+=z;c=p[i];l+=z*((c=="[")-(c=="]"))
 i+=1
