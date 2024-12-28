total_delivery = int(input("Enter number of successful delivery: "))

base_pay = 5000
	
wages = 0
	
if(total_delivery < 50):

	wages = total_delivery * 160 + base_pay

elif (total_delivery < 59):

	wages = total_delivery * 200 + base_pay

elif (total_delivery < 69):

	wages = total_delivery * 250 + base_pay

elif (total_delivery >= 70):

	wages = total_delivery * 500 + base_pay

print(wages)