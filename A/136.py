n=int(input());
ls=list(map(int,input().split()));
res="";
for i in range(1,n+1):
    res+=str(ls.index(i)+1)+" ";
print(res[:-1]);
