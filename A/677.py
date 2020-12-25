n,h=map(int,input().split());
ls=list(map(int,input().split()));
cnt=0;
for i in ls:
    if(i<=h):
        cnt+=1;
    else:
        cnt+=2;
print(cnt);