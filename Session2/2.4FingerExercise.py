"""
2.4 Finger exercise
Replace the comment in the following code with a while loop.

numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
#concatenate X to toPrint numXs times
print(toPrint)
"""

numXs = int(input('How many times should I print the letter X? '))
iterations = 0
toPrint = ''

while iterations < numXs:
    toPrint = toPrint + 'X'
    iterations += 1

print(toPrint)
