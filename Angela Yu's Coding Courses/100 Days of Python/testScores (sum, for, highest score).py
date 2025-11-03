import random
# sum() can be used to add together the items in a list
testScores = [78, 65, 89, 91, 45]
totalScore = sum(testScores)
print(f'{totalScore} is the total score.')

# you can do this manually with a for loop
sum = 0 # to set a starting point
for score in testScores:
    sum += score # this adds the next score to the current sum
print(f'{sum} is the total score.')
# output will be the same as using sum() function, 368


### Below is the final code for finding the top score
# 20 scores between 0 and 100
baby_score_to_upgrade = 0
student_scores = [20, 45, 67, 89, 91, 34, 56, 78, 99, 100, 54, 32, 23, 87, 65, 43, 21, 76, 88, 90]
for i in student_scores:
    if i > baby_score_to_upgrade:
        baby_score_to_upgrade = i
    # print(baby_score_to_upgrade) if you want to see how it updates
print(f"The highest score in the class is: {baby_score_to_upgrade}")
