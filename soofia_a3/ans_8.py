# 8. Write the code to compute – Number of items, mean value, maximum value, average
# value of given list
# Grades = [8, 9, 7, 6, 8, 5, 9, 8.2, 5.9, 4.9, 3, 7]

from statistics import mean


Grades = [8, 9, 7, 6, 8, 5, 9, 8.2, 5.9, 4.9, 3, 7]

print("number of items in Grades list: ",len(Grades))

max = max(Grades)
print("max is ",max)

mean1 = mean(Grades)
print("mean is ",mean1)

sum = 0
for i in range(0,len(Grades)):
    sum = sum + Grades[i]

print("average is {:.2f}".format(sum/len(Grades)))