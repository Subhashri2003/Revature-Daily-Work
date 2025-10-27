numbers=[10,20,30,40,50]
sqnum=[]
dnum=dict()
for num in numbers:
    print(num)
    sqnum.append(num*num)
    tupsq = tuple(sqnum)
    dnum[num]=num*num
print(sqnum)
print(tupsq)
print(dnum)

for k in dnum.keys():
    print(k)
for v in dnum.values():
    print(v)
for k,v in dnum.items():
    print(f'{k}:{v}')