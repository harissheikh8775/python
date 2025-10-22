# highest score
# sum(exam_score)=total sum of marks in the exam_score list
# max(exam_score)=95 --> gives the maximum number in the list

exam_scores = [78, 85, 92, 67, 88, 73, 95, 81, 76, 89]

max_score=0
for score in exam_scores:
    if score > max_score:
        max_score=score

print(f"The max score in the list is {max_score}")