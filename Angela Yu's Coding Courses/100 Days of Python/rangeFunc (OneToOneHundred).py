# Range Function Usage:
# In this example is used with the for loop.

for number in range(1, 11):

# Processes each number from 1 to 10, excluding 11.
    print(number)

# By default, it increments by 1. Can specify as shown below:

for number in range(1, 11, 3):
    print(number)

# How could we add up all the numbers from 1 to 100?

total = 0 # To initialize the final sum variable.
for number in range(1, 101):
    total += number
print(total)