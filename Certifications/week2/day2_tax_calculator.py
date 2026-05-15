income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = (0.18 * income) - 556.2

    if tax < 0:
        tax = 0

else:
    surplus = income - 85528
    tax = 14839.2 + (0.32 * surplus)

tax = round(tax, 0)

print("The tax is:", tax, "thalers")