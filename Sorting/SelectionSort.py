#selection sort
'''
1st element is selected as the min and it's location is stored.
1st element is compared with all the other element if any smaller element found than it's location is stored as min and other elements are compared with the new min
after first iteration : 1st element is swapped with the element whose location is stored as min. This is the smallest element


similar steps for other elements
in second iteration we get 2nd smallest number

continued till n-1 iteration
after n-1 iteration  numbers are sorted (also this is the worst case scenario)
'''

class SelectionSort:
	
	def __init__(self):
		self.list1 = []


	def list_setter(self,list1):
		self.list1 = list1


	def ascending_sort(self):
		min = -1

		for i in range(0,len(self.list1)):
			min = i
			#print("log : iteration = {}".format(min))
			for j in range(i,len(self.list1)):
				if self.list1[min] > self.list1[j]:
					min = j
			
			#swapping 
			temp = self.list1[i]
			self.list1[i] = self.list1[min]
			self.list1[min] = temp

		print("Sorted list is :",self.list1)



	def descending_sort(self):
		max = -1

		for i in range(0,len(self.list1)):
			max = i
			for j in range(i,len(self.list1)):
				if self.list1[max] < self.list1[j]:
					max = j

			#swapping
			temp = self.list1[i]
			self.list1[i] = self.list1[max]
			self.list1[max] = temp

		print("Sorted List in Descending order is : ",list1)






if __name__ == "__main__" :
	
	list1 = [int(x) for x in input("Enter elements in list separated by space : ").split()]
	choice = int(input("Select one from below\n1. Ascending\n2. Descending\nEnter 1 or 2 : "))

	ss = SelectionSort()

	ss.list_setter(list1)
	
	if choice ==1:
		ss.ascending_sort()
	else:
		ss.descending_sort()




			
