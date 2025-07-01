f = open("Input/numbers.txt", "r")
sonlar = []
for qator in f:
    sonlar.append(int(qator.strip()))
f.close()

eng_katta = max(sonlar)

f = open("Output/output09.txt", "w")
f.write("Eng katta son: " + str(eng_katta))
f.close()
