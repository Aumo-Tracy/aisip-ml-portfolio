def analyze_scores(scores):
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    return average, highest, lowest

student_scores = [65, 70, 80, 90, 55, 88]

avg, high, low = analyze_scores(student_scores)

print("Average:", avg)
print("Highest:", high)
print("Lowest:", low)