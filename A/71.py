t=int(input());
for _ in range(t):
    w=input();
    l=len(w);
    if(l>10):
        cnt = l-2;
        res = w[0] + str(cnt) + w[-1];
        print(res);
    else:
        print(w);