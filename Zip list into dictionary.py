subject = ["IoT","English","Maths","Web Tech","Physics","Python"]
marks = [27, 23, 21, 19, 17, None]

# Method 1
print(dict(zip(subject, marks)))

# Method 2
score = {}
for i in range(len(marks)):
    score[subject[i]] = marks[i]

print(score)