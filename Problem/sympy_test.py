from fractions import Fraction
import sympy

# Define a symbolic variable
x = sympy.symbols('x')

# Create an equation
f = sympy.Eq(x*Fraction('2/5'), 1760)

# Solve the equation
result = sympy.solve(f)

remians = result[0] - 1760

print('남은 돈은 {}원 입니다.'.format(remians))
