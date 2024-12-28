import math

print("""  

	Pizza Type | Number of Slices | Price Per Box
	----------------------------------------------
	1: Sapa size     ->    4     ->         2,500
		       		  
	2: Small money   ->    6     ->         2,900
 		       		                         
	3: Big boys      ->    8     ->         4,000
                                         
	4: Odogwu       ->    12     ->         5,200


     """)

pizza_type = int(input("Enter your choice (1-4): "));

number_of_guests = int(input("Enter number of guests: " ));

slice_per_box = 0

price_per_box = 0

match (pizza_type):

	case 1:
		slice_per_box = 4
		price_per_box = 2500
		

	case 2:
		slice_per_box = 6
		price_per_box = 2900
		

	case 3:
		slice_per_box = 8
		price_per_box = 4000
		

	case 4:
		slice_per_box = 12
		price_per_box = 5200


boxes = math.ceil(number_of_guests / slice_per_box)
leftover_slice = int(boxes * slice_per_box - number_of_guests)
total_price = int(boxes * price_per_box)
print(f"boxes: {boxes}")
print(f"Leftover Slice: {leftover_slice}")
print(f"Total price: {total_price}")
		
