# Finding an approximation to the square-root of a number via exhaustive search.

x = int(raw_input('Enter an integer: '))
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print 'numGuesses =', numGuesses
if abs(ans**2 - x) >= epsilon:
    print 'Failed to find square-root of', x
else:
    print ans, 'is a close enough approximation to the square-root of', x
