n=int(input());
pcnt=n//2;
spos=(pcnt*(pcnt+1));
ncnt=n-pcnt;
sneg=ncnt*ncnt;
print(spos-sneg);