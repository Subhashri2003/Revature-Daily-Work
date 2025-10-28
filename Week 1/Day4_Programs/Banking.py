

from MyPackage.Interest_Calculations import simple_interest,compound_interest

pri=float(input("Enter the principal amount: "))
ny=float(input("Enter the no of years: "))
roi=float(input("Enter the rate of interest: "))

si,amt=simple_interest(pri=pri,ny=ny,roi=roi)
print(f'SI:{si} Amount:{amt}')

amt=compound_interest(pri=pri,ny=ny,roi=roi)
print(f'Amount:{amt}')