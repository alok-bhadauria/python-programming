marks = {
    "IoT" : 27,
    "English" : 23,
    "Math" : 21,
    "Web Tech" : 19,
    "Physics" : 17,
    "Python" : None
}

print(list(marks.items()))

for key, val in list(marks.items()):
    if type(val) != int:
        marks.pop(key)

a = 0

for key, val in marks.items():
    if type(val) == int:
        a += val

print("Total Marks : ", a)

values = marks.values()
max_marksValue = max(values)
min_marksValue = min(values)

subject_maxMarks = []
subject_minMarks =[]

for key, val in marks.items():
    if max_marksValue == val:
        subject_maxMarks.append(key)

    if min_marksValue == val:
        subject_minMarks.append(key)

print("Maximum : ", subject_maxMarks, max_marksValue)
print("Minimum : ", subject_minMarks, min_marksValue)