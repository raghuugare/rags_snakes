# Finding an approximation to the square-root of a number via the Newton-Raphson method.
# Can be extended to find the n'th root of a number too!
x = int(raw_input('Approximation of Square-root via the Newton-Raphson method--Enter an integer: '))
epsilon = 0.01
guess = x/2.0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) -k)/(2*guess))
print '(Newton-Raphson method): Square root of', x, 'is about ', guess
