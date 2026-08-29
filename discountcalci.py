amount = float(input("Enter purchase amount: "))
if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.15
elif amount >= 1000:
    discount = amount * 0.10
else:
    discount = 0
final_amount = amount - discount
print("Discount:", discount)
print("Final amount to be paid:", final_amount)