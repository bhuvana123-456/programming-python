principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (Years): "))
si = (principal * rate * time) / 100
amount = principal + si
print("Simple Interest =", si)
print("Total Amount =", amount)
