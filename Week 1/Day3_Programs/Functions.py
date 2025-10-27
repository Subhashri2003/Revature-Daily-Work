n1 = int(input())
n2 = int(input())
n3 = int(input())

def add(**nums):
    print(type(nums))
    res = nums.get('fn', 0) + nums.get('sn', 0) + nums.get('tn', 0)
    return res

print(add(fn=n1, sn=n2, tn=n3))
print(add(fn=n1, sn=n2))




def calculate(m1,m2,m3):
    total=m1+m2+m3
    avg=total/3
    return total,avg

sname=input('Enter name:')
m1=int(input('Enter first number:'))
m2=int(input('Enter second number:'))
m3=int(input('Enter third number:'))

total,avg=calculate(m1,m2,m3)
print(f'total:{total}, Avg: {avg}')


