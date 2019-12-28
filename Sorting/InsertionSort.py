#insertion sort
'''
whole list is divided into 2 sub list
sorted and unsorted
in every iteration 1 element is added from the unsorted list to the sorted list

1st iteration :
as only one element so no comparison and directly added to sorted sub list -list(that is the part on left side we can say)

2nd iteraation :
2nd element compared with 1st element if 2nd element smaller we swap them.

3rd iteration :
3rd element compared with 2nd element if 3rd smaller than 2nd swap.
2nd element compared wit 1st element if smaller swap

after 3rd iteration :
we get 3 elements in sorted sub list

similarly for rest

'''

class InsertionSort:
	def __init__(self):
		self.mylist1 = []

	def list_setter(self,list1):
		self.list1 = list1


	def sort(self):

		for i in range(0,len(self.list1)):
			for j in range(i,0,-1): #for i = 0 inner loop does not executes
				if self.list1[j] < self.list1[j-1] :
					temp = self.list1[j]
					self.list1[j] = self.list1[j-1]
					self.list1[j-1] = temp
				print("log i = {2}, j = {1}: after element swap : {0}".format(self.list1,j,i))
			print("\n")
		print("Sorted list is :",self.list1)


if __name__ == "__main__":

	list1 = [int(x) for x in input("Enter elements in list separated by space").split()]

	is1 = InsertionSort()
	is1.list_setter(list1)
	is1.sort()
