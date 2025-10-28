from OOP.Employee import Employee

empid=int(input('Enter Employee ID: '))
ename=(input('Enter Employee Name: '))
bp=float(input('Enter Basic Pay: '))

emp1=Employee(empid,ename,bp)


print(f'Emp id:{empid} \n'
       f'Emp name:{ename}\n' 
       f'Gross Pay:{bp}\n'
       f'Net Pay:{bp}')
emp1.calc_grosspay()
emp1.calc_netpay()

