w=input();
up,lo=0,0;
for ch in w:
    if(ch.isupper()):
        up+=1;
    else:
        lo+=1;
if(up>lo):
    w=w.upper();
elif(lo>=up):
    w=w.lower();
print(w);