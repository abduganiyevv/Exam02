def calculate_tax(soliq , foyda):
    return soliq , foyda

 
def calculate_net_salary(soliq , foyda):
    return soliq , foyda

maosh = int(input("Maoshizni kiriting:"))
chegirma = 0.2
soliq = maosh * chegirma
foyda = maosh - soliq
if maosh >= 5000000:
    print(calculate_tax(soliq , foyda))

chegirma = 0.13
soliq = maosh * chegirma
foyda = maosh - soliq
if maosh <= 5000000:
    print(calculate_net_salary(soliq , foyda))