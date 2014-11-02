# Golfed mini-intepreter (no debug, cell_max=256)
# Bytes: 421
# Techniques: Replaced char matching with index y, replaced conditional addition  
# with adding boolean values (x+(a==2)), variable renaming, using variables for
# repeated expressions

# Global parameters
F="examples/multiply2.b"
C=256
#----------------------------
with open(F,'r')as z:p=z.read()
t=[0]*30000
i=d=l=0
while i<len(p):
 f=1;c=p[i];x=t[d];y="><+-.,[]";a=y.index(c)if c in y else 9;d+=(a==0)-(a==1)
 if a in(2,3):t[d]=(x+(a==2)-(a==3))%C
 if a==4:print(chr(x),end="")
 if a==5:t[d]=ord(input())
 if(a,x)==(6,0):
  f=0;l=1
  while l>0:i+=1;c=p[i];l+=(c=="[")-(c=="]")
  i+=1         
 if a==7 and x!=0:
  f=0;l=1
  while l>0:i-=1;c=p[i];l-=(c=="[")-(c=="]")
  i+=1
 if f:i+=1