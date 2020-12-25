l=int(input());
s=input();
ca,cd=0,0;
for ch in s:
    if(ch=="A"):
        ca+=1;
    else:
        cd+=1;
if(ca>cd):
    print("Anton");
elif(cd>ca):
    print("Danik");
else:
    print("Friendship");