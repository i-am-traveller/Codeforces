yr=int(input());
while(True):
    yr+=1;
    s=str(yr);
    l=len(s);
    st=set(s);
    lst=len(st);
    if(l==lst):
        print(yr);
        break;
