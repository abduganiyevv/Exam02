def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("Mablag' yetarli emas")
        return balance
    return balance - amount

def check_balance(balance):
    print(f"Joriy balans: {balance} so'm")
    return balance

balance = 100000
amal = input("Amalni kiriting (deposit / withdraw / check): ").lower()

if amal == "deposit":
    miqdor = int(input("Qo‘yiladigan miqdor: "))
    balance = deposit(balance, miqdor)
    print(f"Yangi balans: {balance} so'm")
elif amal == "withdraw":
    miqdor = int(input("Yechiladigan miqdor: "))
    balance = withdraw(balance, miqdor)
    print(f"Yangi balans: {balance} so'm")
elif amal == "check":
    check_balance(balance)
else:
    print("Salomat no'to'g'ri amal kiritdingiz.")
