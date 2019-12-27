class BinarySearch():

	def __init__(self):
		self.my_list1 = []


	def set_list(self,list1):
		self.list1 = list1

	def sort(self):
		self.list1.sort()

	def search(self,element):
		#initial values
		min = 0
		max = len(list1) -1
		mid = -1
		search_iteartion = 0

		while min <=max :
			search_iteartion +=1			#counting number of itearations
			mid = int( (max + min) /2 ) # as we don't want float value
			print("log: iteration no : {0}, min = {1}, max = {2}, mid = {3}".format(search_iteartion,min,max,mid))
			if element == list1[mid] :
				print("console : Element found at position {}".format(mid) )
				break
			elif element > list1[mid] : #element is greater than mid value
				min = mid +1
			else : 							#else the element would be smaller than mid
				max = mid -1



if __name__ == "__main__": # This block of code will be executed if the file is used directly instead of using it as module # if used as module it will not be executed
	
	list1 = [int(x) for x in input("Enter values to the list separated by space : ").split()]
	element = int( input("Enter value to be searched : ") )

	bs1 = BinarySearch()
	bs1.set_list(list1)
	bs1.sort()
	bs1.search(element)



