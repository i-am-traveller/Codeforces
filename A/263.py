mat=[];
pi,pj=-1,-1;
for i in range(5):
    row=list(map(int,input().split()));
    if(1 in row):
        pi=i;
        pj=row.index(1);
    mat.append(row);
rowdiff = int(abs(2-pi));
coldiff = int(abs(2-pj));
print(rowdiff+coldiff);