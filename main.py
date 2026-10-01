import student

a = True
print("Each record in the list is a string like so, ['Sanjay 26150975 IT', 'Abishek 26150996 CSE']")
l = eval(input("Enter list of students: "))
while a:
	print("Enter 1 to Display Student details")
	print("Enter 2 to Add Student details")
	print("Enter 3 to Search for a student")
	print("Enter 4 to exit")
	choice = int(input("Enter choice ="))
	
	if choice == 1:
		student.display(l)
	elif choice == 2:
		student.add_student(l)
	elif choice == 3:
		print(student.search_student(l))
	elif choice == 4:
		a = False
	else:
		print("Invalid Input")
		

