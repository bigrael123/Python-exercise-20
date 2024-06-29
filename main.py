from statistics import mean

grades = [9, 7, 7, 10, 3, 9, 6, 6, 2]
print(grades.count(7))
grades[len(grades)-1] = 4
print(grades)
print(max(grades))
grades.sort()
print(grades)
sum_of_grades = sum(grades)
print(sum_of_grades)
average = mean(grades)
print(average)