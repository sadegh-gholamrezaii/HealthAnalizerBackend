import math


age = 20
height = 170
weight = 60
waist = 70
neck = 30
hip = 60

# result = (age * 4.33) - (height * 3.098) + (weight * 9.924) + 447.593
# result = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
# result = (9.247 * weight) + (3.098 * height) - (4.330 * age) + 447.593
# result = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
# result = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
# BFP = 86.010*math.log10(waist-neck) - 70.041*math.log10(height) + 36.76
# result = round(result, 2)
print(BFP_man)
print(BFP_woman)