s=input();
ls=[0]*3;
for ch in s:
    if(ch=="1"):
        ls[0]+=1;
    elif(ch=="2"):
        ls[1]+=1;
    elif(ch=="3"):
        ls[2]+=1;
res="";
for i in range(len(ls)):
    if(ls[i] != 0):
        pt=str(i+1);
        for j in range(0,ls[i]):
            res+=pt+"+";
print(res[:-1]);