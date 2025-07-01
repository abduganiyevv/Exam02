students = {'Ali': 5, 'Vali': 4, 'Hasan': 5, 'Husan': 3}
ortacha_baho = sum(students.values()) / len(students)

print(f"O‘rtacha baho: {ortacha_baho}")
print(f"{ortacha_baho} dan yuqori baho olganlar:")

for ism, baho in students.items():
    if baho > ortacha_baho:
        print(ism)
