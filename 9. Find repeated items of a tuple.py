# WAPP to find the repeated items of a tuple

a = input("Enter tuple items : ").split()
a = tuple(map(str, a))
rpt = []
for i in a:
    if (a.count(i)>=2):
        if i not in rpt:
            rpt.append(i)
print("Repeated elements : ",tuple(rpt))