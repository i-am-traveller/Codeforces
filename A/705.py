n=int(input());
res="";
if(n==1):
    print("I hate it");
else:
    for i in range(1,n):
        if(i%2==0):
            res+="I love that ";
        else:
            res+="I hate that ";
    if(n%2==0):
        res+="I love it";
    else:
        res+="I hate it";
    print(res);