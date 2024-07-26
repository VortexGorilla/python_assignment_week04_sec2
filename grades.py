grades = [55, 70, 65, 40, 90, 85, 50, 77]
passed_with_bonus = [grade * 1.05 for grade in grades if grade >= 60]
print("Grades after filtering and applying bonuses:",passed_with_bonus)
