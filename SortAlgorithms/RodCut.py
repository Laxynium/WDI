import sys
#Here is somewhere bug, becouse gives wrong answers
def MemoCutRod(p,n):
    r=[-sys.maxsize-1]*n

    return MemoCutRodAux(p,n,r)
def MemoCutRodAux(p,n,r):
    if(r[n-1]>=0):
        return r[n-1]
    if(n==0):
        q=0
    else:
        q=-sys.maxsize-1
        for i in range(0,n):
            q=max(q,p[i],+MemoCutRodAux(p,n-i-1,r))
    r[n-1]=q
    return q

def CutRod(p,n):
    if(n==0):
        return 0
    q=-sys.maxsize-1
    for i in range(0,n):
        q=max(q,p[i]+CutRod(p,n-i-1))
    return q

def BottomUpCutRod(p,n):
  r=[None]*(n+1)
  r[0]=0
  for j in range(0,n):
      q=-sys.maxsize-1
      for i in range(0,j+1):
          q=max(q,p[i]+r[j-i])
      r[j+1]=q
  return r[n]



PriceTable=[1,5,8,9,10,16,17,20,24,26]

n:int=int(input("Put rod length..."))
print(CutRod(PriceTable,n))
print(BottomUpCutRod(PriceTable,n))