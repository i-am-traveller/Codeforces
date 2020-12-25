n=int(input());
if(n%2!=0):
    print("NO");
else:
    rem = n - 2;
    if(rem>0):
        print("YES");
    else:
        print("NO");