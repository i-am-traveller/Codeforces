k,n,w=map(int,input().split());
smb=(w*(w+1))//2;
price=smb*k;
if(price<=n):
    print(0);
else:
    print(price-n);