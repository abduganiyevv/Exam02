f = open("Input/grades.csv", "r")
sanash = 0

for qator in f:
    qator = qator.strip()
    if qator:
        ism, baho = qator.split(",")
        if int(baho) == 5:
            sanash += 1

f.close()

f = open("Output/output16.txt", "w")
f.write("5 baho olganlar soni: " + str(sanash))
f.close()
