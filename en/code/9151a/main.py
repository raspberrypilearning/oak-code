test_scores = [18,32,40,28,12,4,16,15,25,41,
               42,44,24,11,22,23,6,38,26,9,
               17,43,35,30,19]

highest_score = max(test_scores)
print(f"The highest score was {highest_score}")
lowest_score = min(test_scores)
print(f"The lowest score was {lowest_score}")
total = 0
for score in test_scores:
    total = total + score
average = total/len(test_scores)
print(f"The average score was {average}")

