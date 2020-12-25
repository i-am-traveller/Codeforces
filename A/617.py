x=int(input());
step=0;
ls=[5,4,3,2,1];
for i in range(5):
    while(x>=ls[i]):
        x-=ls[i];
        step+=1;
print(step);