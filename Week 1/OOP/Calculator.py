from selectors import SelectSelector

from ArithCalculations import ArithCalculations

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

calc=ArithCalculations(num1,num2)

print(f'{calc.add()}')
print(f'{calc.sub()}')
print(f'{calc.mul()}')

try:
    if num2==0:
        raise ZeroDivisionError('num2 is 0')
    if age <18:
        raise  AgeNotEnough("You are minor")
except ZeroDivisionError as zde:
    print(f'{zde}')
else:
    try:
        l1 = [1, 5, 7, 3]
        val = l1[1]
        res = calc.div()
    except ZeroDivisionError as zde:
        print(f'{zde}-0 in denominator')
    except IndexError as ie:
        print(f'{ie}-Index not found or too big')
    except:
        print('OOPS!')
    else:
        print(val)
        print(res)
    finally:
        print('Done !')


