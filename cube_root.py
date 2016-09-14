# Finding the cube-root of a perfect cube (integer)
x = int(raw_input('Enter an integer: '))
ans = 0

while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print x, 'is not a perfect cube!'
else:
    print 'Cube-root of ', x, ' = ', ans
