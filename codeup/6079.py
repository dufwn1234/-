w, h =input().split()
w=int(w)
h=int(h)
a=[]
for i in range(w):
    a.append([])
    for j in range(h):
        a[i].append(0)
    
n=int(input())

for i in range(n):
    
    l, d, x, y =input().split()
    l=int(l)
    d=int(d)
    x=int(x)
    y=int(y)
    
    if d==0:
        for u in range(l):
            a[x-1][y+u-1]=1
    
    elif d==1:
        for r in range(l):
            a[x-1+r][y-1]=1
        
        


for i in range(w) :
    for j in range(h) : 
        print(a[i][j], end=' ')    
    print()