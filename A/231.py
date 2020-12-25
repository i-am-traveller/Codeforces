n=int(input());
res=0;
for _ in range(n):
    ls=list(map(int,input().split()));
    if(ls.count(1) >= 2):
        res+=1;
print(res);