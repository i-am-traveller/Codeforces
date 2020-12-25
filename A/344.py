n=int(input());
cnt=0;
prev="";
for _ in range(n):
    mg=input();
    if(prev==""):
        prev=mg;
        continue;
    if(prev!=mg):
        cnt+=1;
        prev=mg;
print(cnt+1);