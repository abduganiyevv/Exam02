f = open("input/numbers.txt", "r")
sonlar = []
for qator in f:
    sonlar.append(int(qator.strip()))
f.close()

sonlar.sort()
f = open("output/output10.txt", "w")
for son in sonlar:
    f.write(str(son) + "\n")
f.close()
