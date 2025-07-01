students = [
    {'name': 'Ali', 'age': 18},
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Muhammad', 'age': 21}
]

eng_qisqa = min(students, key=lambda student: len(student['name']))
print(f"Eng qisqa ismli o‘quvchi: {eng_qisqa['name']}")
