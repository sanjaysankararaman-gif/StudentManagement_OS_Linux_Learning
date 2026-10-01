def add_student(l):
	name = input("Enter student name: ")
	roll = input("Enter roll number: ")
	dept = input("Enter department: ")
	s = name+" "+roll+" "+dept
	l.append(s)
	print(l)
	
def search_student(l):
	s = input("Enter student name: ")
	for i in l:
		a = i.split()
		if a[0] == s:
			return True
			break
		else:
			continue
	else:
		return False

def display(l):
	s = input("Enter student name: ")
	for i in l:
		a = i.split()
		if a[0] == s:
			print("Student Name:", a[0])
			print("Roll Number:", a[1])
			print("Department:" , a[2])
			


		
		
		
		
