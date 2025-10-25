'''
Date:25/10/2025
Author:Subhashri
Description:Prog to find biggest of 2 nos
'''

num1=int(input('Enter a number: '))
num2=int(input('Enter another number: '))
if num1>num2:
    print(f'{num1} is greater than {num2}')
elif num2>num1:
    print(f'{num2} is greater than {num1}')
else:
    print('Both numbers are equal')

txt = f"{'num1 is greater' if num1 > num2 else 'num2 is greater'}"
print(txt)

num3=45
print(f'num3.2f')