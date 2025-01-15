import datetime

items = []

number_of_goods = []

price = []

total = 0

customer_name = input("Customer name?: ")
while (True):
	goods_purchase = input("What did the customer buy?: ")
	items.append(goods_purchase)

	number_of_goods_purchase = int(input("How many pieces?: "))
	while number_of_goods_purchase < 1:
		number_of_goods_purchase = int(input("invalid, try again: "))
	number_of_goods.append(number_of_goods_purchase)
	
	price_per_unit = float(input("How much per unit?: "))
	while price_per_unit < 1:
		price_per_unit = float(input("invalid, try again: "))
	price.append(price_per_unit)

	optional = input("Add more items? (Yes/No): ")

	while optional not in ['yes', 'no']:
		optional = input("wrong input, select (Yes/No): ")

	if optional.lower() == "yes":
		continue
	
	if optional.lower() == "no":
		break

cashier_name = input("Cashier name?: ")

discount_amount = float(input("How much discount will he get?: "))
while discount_amount < 1:
	discount_amount = float(input("invalid, try again: "))	

print("\nSEMICOLON STORES")
print("MAIN BRANCH")
print("LOCATION: Sabo, yaba lagos")
print("TEL: 04683484560")
print("Date:", datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S"))
print("Cashier: " + cashier_name)
print("Customer's Name: " + customer_name)
print("""
===========================================================
 ITEMS		QTY		PRICE		TOTAL(NGN)
===========================================================
""")
for counter in range(len(items)):

	total += number_of_goods[counter] * price[counter]

	print(f"{items[counter]}\t\t{number_of_goods[counter]}\t\t{price[counter]}\t\t{number_of_goods[counter] * price[counter]}")

print("""
==========================================================
""")

discount = total * 0.075

vat = total * 0.175

total_bill = total + vat - discount

print(f"\t\t\t{'Sub Total: '} {total}")
print(f"\t\t\t{'Discount :'} {discount}")
print(f"\t\t\t{'VAT :'} {vat}")
print(f"\t\t\t{'Bill Total :'} {total_bill}")

print("""
==========================================================
""")
print(f"{'THIS IS NOT A RECIEPT KINDLY PAY: '} {total_bill}")
print("""
==========================================================
""")





amount_paid = float(input("How much did the customer give you?: "))
while amount_paid < total_bill:
	amount_paid = float(input("wrong input, pls kindly input the exact amount: "))

balance = amount_paid - total_bill

print("\nSEMICOLON STORES")
print("MAIN BRANCH")
print("LOCATION: Sabo, yaba lagos")
print("TEL: 04683484560")
print("Date:", datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S"))
print("Cashier: " + cashier_name)
print("Customer's Name: " + customer_name)
print("""
===========================================================
 ITEMS		QTY		PRICE		TOTAL(NGN)
===========================================================
""")

for counter in range(len(items)):

	print(f"{items[counter]}\t\t{number_of_goods[counter]}\t\t{price[counter]}\t\t{number_of_goods[counter] * price[counter]}")
print("""
==========================================================
""")
print(f"\t\t\t{'Sub Total: '} {total}")
print(f"\t\t\t{'Discount: '} {discount}")
print(f"\t\t\t{'VAT: '} {vat}")
print(f"\t\t\t{'Bill Total: '} {total_bill}")
print(F"\t\t\t{'Amount paid: '} {amount_paid}")
print(f"\t\t\t{'Balance: '} {balance}")
print("""
==========================================================
  		THANKS FOR PATRONAGE
==========================================================
""")

