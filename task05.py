matn = input("matn kiriting:")
sozlar = matn.split()
lugat = {}

for soz in sozlar:
    if soz in lugat:
        lugat[soz] += 1
    else:
        lugat[soz] = 1
print(lugat)
