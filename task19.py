names = ['Ali', 'Diyor', 'Jasurbek', 'Muhammad']

eng_uzun = ""
for ism in names:
    if len(ism) > len(eng_uzun):
        eng_uzun = ism

print(f"Eng uzun ism: {eng_uzun}")

