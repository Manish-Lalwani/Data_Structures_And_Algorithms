class LinearSearch:

	def __init__(self):
		self.list1 = []

	def search(self,list1,element):
		found_flag = 0
		for i in range(0, len(list1) ):
			if element ==list1[i]:
				print("Element found in List at position : ",i+1)
				found_flag = 1
				break
		if found_flag ==0:
			print("Element not found in list")



###################################################
ls1 = LinearSearch()

print("=================================================")
list1 = [int(x) for x in input("Enter element in the list separated by space : ").split()]

print("=================================================")
element = int( input("Enter the element to be searched : ") )

print("=================================================")
ls1.search(list1,element) 


