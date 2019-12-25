#Bubble Sort

class BubbleSort:
	def __init__(self):
		#self.mylist1 = []
		pass


	def sort(self, list1):
		for i in range( 0,len(list1) ):
			for j in range( i,len(list1) ):
				if list1[i] > list1[j]:
					temp = list1[i]
					list1[i] = list1[j]
					list1[j] = temp
		self.mylist1 = list1

	def display(self):
		print("Sorted array is :\n",self.mylist1)



###########################################

bs1= BubbleSort()

#Taking input from user
print("=================================================")
list1 = [int(x) for x in input("Enter numbers to be sorted separated by space : ").split()]

print("=================================================")
print("You have entered following numbers to  be sorted :\n",list1)
bs1.sort(list1)

print("=================================================")
bs1.display()

