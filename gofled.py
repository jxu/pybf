# Golfed mini-intepreter (no debug, cell_max=256)
# Bytes: 445

# Vars
F="examples/multiply2.b"
C=256
#----------------------------
with open(F,'r')as z:p=z.read()
t=[0]*30000
i=d=l=0
while i<len(p):
 f=1;c=p[i];x=t[d];y="><+-.,[]";a=y.index(c) if c in y else 9;d+=(a==0);d-=(a==1)
 if a==2:t[d]=(x+1)%C
 if a==3:t[d]=(x-1)%C
 if a==4:print(chr(x),end="")
 if a==5:t[d]=ord(input())
 if(a,x)==(6,0):
  f=0;l=1
  while l>0:
   i+=1;c=p[i];l+=(c=="[");l-=(c=="]")
  i+=1         
 if a==7 and x!=0:
  f=0;l=1
  while l>0:
   i-=1;c=p[i];l-=(c=="[");l+=(c=="]") 
  i+=1
 if f:i+=1