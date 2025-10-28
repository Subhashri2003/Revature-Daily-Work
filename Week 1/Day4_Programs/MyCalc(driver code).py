
from MyPackage.Interest_Calculations import  simple_interest
from MyPackage.Shape_Calculations import area_of_rect,area_of_circle,area_of_square

pri=float(input('Enter principle: '))
ny=float(input('Enter no of years: '))
roi=float(input('Enter roi: '))



print(f'Simple interest is: {simple_interest(pri=pri,ny=ny,roi=roi)[0]} '
      f'Amount: {simple_interest(pri=pri,ny=ny,roi=roi)[1]} ')

print(f'Area of rect is: {area_of_circle(10)} \n '
      f'Area of square is: {area_of_square(10)}\n'
      f'Area of rect is: {area_of_rect(10,5)}')