a = int(input('the cost of the meal is'))
tip = 0.18 * a
tax = .06 * a
total = a*0.06+tip+a
print('the tax is',tax)
print('the tip is',tip)
print('the total amount is %.3f\n'%total)
