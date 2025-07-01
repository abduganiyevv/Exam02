f = open("Input/numbers.txt", "r")
sonlar = []
for qator in f:
    sonlar.append(int(qator.strip()))
f.close()

yigindi = sum(sonlar)

f = open("Output/output08.txt", "w")
f.write("Yig'indi: " + str(yigindi))
f.close()
