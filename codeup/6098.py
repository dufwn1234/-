a=[]
for i in range(10):
    a.append([])
    a[i]=list(map(int,input().split()))
x=1
y=1
a[x][y]=9

while True:
    if a[x][y+1]==0 :
        a[x][y+1]=9
        y+=1
        continue
            
    elif a[x][y+1]==1 and a[x+1][y]==0:
        a[x+1][y]=9
        x+=1
        continue
    
    elif a[x][y+1]==2:
        a[x][y+1]=9
        break
    
    elif a[x][y+1]==1 and a[x+1][y]==2:
        a[x+1][y]=9
        break
        
    elif a[x][y+1]==1 and a[x+1][y]==1:
        break
    


for i in range(10):
    for j in range(10):
        print(a[i][j],end=" ")
    print()