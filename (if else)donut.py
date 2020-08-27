price=int(input("enter the price of a donut:"))
quantity=int(input("enter the quantity of the donut:"))
amount=price*quantity
if amount>1000:
    print("10% of discount is applicable")
    discount=amount*10/100
    amount=amount-discount
else:
   print("5% discount is aplicable")
   discount=amount*5/100
   amount=amount-discount
print("The payble amount is RS:",amount)
