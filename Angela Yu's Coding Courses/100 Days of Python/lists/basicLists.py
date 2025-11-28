# a = 3
# b = 'hello'

# These are single vars.
# What if we want to store multiple values?

# Lists

# syntax:
# list_name = [item1, item2, item3]

# fruits = ['apple', 'banana', 'cherry', 'mango']
# print(fruits)

# Lists exist in one line!
fiftyStates = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
fiftyStatesInOrderOfUnionJoined = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']
print(fiftyStates)
print(fiftyStatesInOrderOfUnionJoined)

# We can grab specific items from these lists as well.
askedState = input("Enter a number for which state you want (1-50): ")
index = int(askedState) - 1  # converting to int and adjusting for 0-based index
print("The state you selected is:", fiftyStatesInOrderOfUnionJoined[index])

# Wonder why I put the -1 there?
# Lists are zero-indexed. That means the first item is item 0.

# Here, we retrieve the first item by using zero, not one.
# first item: list_name[0]

# The -1 makes it so that the user can enter the state in their way of thinking.
# So if they enter 1, we give them index 0.

# The only issue is if they enter 0 or a number greater than 50.
# We'll get to that later, though.
