price=int(input("enter the price of a donut rs: "))
quantity=int(input("enter the number of donuts "))
amount=price*quantity
if amount>1000:
    print("discount of 10% is aplicable")
    discount=amount*10/100
    amount=amount-discount
print("the payble amount is:",amount)

      
    
