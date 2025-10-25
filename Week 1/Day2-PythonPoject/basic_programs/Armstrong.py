numstr=input('Enter a number:')
numlen=len(numstr)
num=int(numstr)
sum=0
temp=num
while(num>0):
    rem=num%10
    sum=sum+rem**numlen
    num=num//10
if temp==sum:
    print('Armstrong')
else:
    print('Not Armstrong')

