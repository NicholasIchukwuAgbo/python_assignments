task_holder = []

def get_task():

	task = input("\n Add a task : ")

	task_holder.append(task)

	print("Task added!\n")


def view_tasks():

	print("\nTasks:")

	for count in range(len(task_holder)):

		print(f"{count + 1}. {task_holder[count]}")

def mark_task(task_holder):

	index = int(input("\nmark task as complete : ")) 

	task_holder[index]["x"]

	print("Task marked as complete.")


def delete_task(task_holder):
	while True:
		try:
			index = int(input("\nEnter the task to delete: "))

			task_holder.pop(index)

			print("Task deleted")
		except ValueError:
			print("invalid, try again")

  
	
def main():

	while True:
		
		print(" 1. Add a tast \n 2. View tasts \n 3. Mark tasks as complete \n 4. Delete a task \n 5. Exit \n")

		user_choice = int(input("Select between 1 - 5: "))

		if user_choice < 1 or user_choice > 5:
			print("invalid, try again") 

		task_place_holder = user_choice 

		if task_place_holder == 1:
			get_task()
		

		elif task_place_holder == 2:
			view_tasks()

		elif task_place_holder== 3:
			mark_task(task_holder)

		elif task_place_holder == 4:
			delete_task(task_holder)

		elif task_place_holder == 5:
			break
			
					

if __name__ == "__main__":
	main()
	

	
	
	