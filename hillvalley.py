def hv(a):
    d=1
    i=0
    while i+2<=len(a):
        if a[i]>a[i+1]:
            if a[i+1]<a[i+2]:
                return True
        if a[i]<a[i+1]:
            if a[i+1]>a[i+2]:
                return True
        i=i+1
    return False







        # w2 programming qs answer passed 9/11 test cases
def threesquares(m):
    while m%4==0:
        m=m/4
    if(m%8==7):
        return False
    return True

        
        
def repfree(s):
  rep=[]
  for i in s:
    if i in rep:
      return False
    else :
      rep.append(i)
  return True



def hillvalley(l):
    i=0
    while i+2<=len(l):
        if l[i]>l[i+1]:
            if l[i+1]<l[i+2]:
                return True
        if l[i]<l[i+1]:
            if l[i+1]>l[i+2]:
                return True
        i=i+1
    return False
        
    
      
