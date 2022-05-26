"""
2.2 Finger exercise
Write a program that examines three variables—x, y, and z—and
prints the largest odd number among them. If none of them are odd, it should
print a message to that effect.
"""

count = 0
listOfNums = list()
oddListOfNums = list()

while count < 3:
    number = input("Enter a number: ")
    listOfNums.append(int(number))
    count += 1

for num in listOfNums:
    if num % 2 == 1:
        oddListOfNums.append(num)
    else:
        continue

if len(oddListOfNums) > 0:
    print('The biggest odd number is:', max(oddListOfNums))
else:
    print('There are no odd numbers.')

