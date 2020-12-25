def isLucky(n):
    s=str(n);
    for ch in s:
        if(ch!="4" and ch!="7"):
            return False;
    return True;

n=input();
ldig=0;
for ch in n:
    if(ch=="4" or ch=="7"):
        ldig+=1;
if(isLucky(ldig)):
    print("YES");
else:
    print("NO");