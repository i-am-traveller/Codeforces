t=int(input());
x=0;
for _ in range(t):
    s=input();
    for ch in s:
        if(ch=="+"):
            x+=1;
            break;
        elif(ch=="-"):
            x-=1;
            break;
print(x);