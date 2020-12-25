n,k=map(int,input().split());
ls=list(map(int,input().split()));
cut=ls[k-1];
cnt=0;
for i in ls:
    if(i>=cut and i>0):
        cnt+=1;
print(cnt);