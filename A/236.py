s=input();
chs=set();
for ch in s:
    chs.add(ch);
l=len(chs);
if(l%2==0):
    print("CHAT WITH HER!");
else:
    print("IGNORE HIM!");