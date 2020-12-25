n=int(input());
s=input();
if(n==1):
    print(0);
else:
    cnt=0;
    prev=0;
    for i in range(1,n):
        if(s[prev]==s[i]):
            cnt+=1;
        else:
            prev=i;
    print(cnt);
