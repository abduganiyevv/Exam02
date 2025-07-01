cart = {
  'non': {'price': 3000, 'quantity': 2},
  'sut': {'price': 8000, 'quantity': 1},
  'olma': {'price': 5000, 'quantity': 5}
}
a = (cart["non"]["price"])
b = (cart["sut"]["price"])
c = (cart["olma"]["price"])
a1 = a * (cart["non"]["quantity"])
b1 = b * (cart["sut"]["quantity"])
c1 = c * (cart["olma"]["quantity"])
d = a1 + b1 + c1
print(f"Umumiy summa:{d}")

