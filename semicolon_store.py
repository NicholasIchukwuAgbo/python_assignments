import datetime

customer_name = input("Customer name?: ")

goods_purchase = input("What did the customer buy?: ")

number_of_goods_purchase = int(input("How many pieces?: "))

price_per_unit = int(input("How much per unit?: "))

while True:

    optional = input("Add more items? (Yes/No): ")

    if optional.lower() == "yes":

        goods_purchase2 = input("What did the customer buy: ")

        number_of_goods_purchase2 = int(input("How many pieces?: "))

        price_per_unit2 = int(input("How much per unit?: "))
        
    elif optional.lower() == "no":

        cashier_name = input("Cashier name?: ")

        discount_amount = float(input("How much discount will he get?: "))
        break
        
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")


print("SEMICOLON STORES")

print("MAIN BRANCH")

print("TEL: 04683484560")

print("Date:", datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S"))

print("Cashier: " + cashier_name)

print("Customer's Name: " + customer_name);
	
print("""
========================================================
ITEMS   QTY    PRICE   TOTAL(NGN)
--------------------------------------------------------
""")

total = (price_per_unit * number_of_goods_purchase) + price_per_unit2 * number_of_goods_purchase2

discount = total * 0.075

vat = total * 0.175

total_bill = total + vat - discount

print(f"{goods_purchase}\t{number_of_goods_purchase}\t{price_per_unit}\t{price_per_unit * number_of_goods_purchase}")

print(f"{goods_purchase2}\t{number_of_goods_purchase2}\t{price_per_unit2}\t{price_per_unit2 * number_of_goods_purchase2}")

print("Sub Total: ", total)

print("Discount: ", discount)

print("VAT: ",  vat)

print("Bill Total: ", total_bill)

print("THIS IS NOT AN RECIEPT KINDLY PAY: ", total_bill)

amount_paid = int(input("How much did the customer give you?: "))

print("SEMICOLON STORES")

print("MAIN BRANCH")

print("TEL: 04683484560")

print("Date:", datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S"))

print("Cashier: " + cashier_name)

print("Customer's Name: " + customer_name);
	
print("""
========================================================
ITEMS   QTY    PRICE   TOTAL(NGN)
--------------------------------------------------------
""")

total = (price_per_unit * number_of_goods_purchase) + price_per_unit2 * number_of_goods_purchase2

discount = total * 0.075

vat = total * 0.175

total_bill = total + vat - discount

balance = amount_paid - total_bill

print(f"{goods_purchase}\t{number_of_goods_purchase}\t{price_per_unit}\t{price_per_unit * number_of_goods_purchase}")

print(f"{goods_purchase2}\t{number_of_goods_purchase2}\t{price_per_unit2}\t{price_per_unit2 * number_of_goods_purchase2}")

print("Sub Total: ", total)

print("Discount: ", discount)

print("VAT: ",  vat)

print("Bill Total: ", total_bill)

print("Balance: ", balance)

print("THANKS FOR PATRONAGE")







