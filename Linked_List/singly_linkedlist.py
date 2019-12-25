#LinkedLists
'''
reference : https://www.geeksforgeeks.org/data-structures/linked-list/
Linear Data Structure
Not contiguous (elements are not store in continuous blocks of memory)



Why Linked List
Can grow or shrink unlike array
Ease of insertion/deletion

Disadvantage :
Random access not allowed need to traverse each  time.
'''

class Node:

	def __init__(self,data=None):
		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):
		self.head=None


	def insert(self,data):
		if self.head == None: 				#if will be executed for first node
			self.head = Node(data)

		else :								#else will be executed  there after
			current =self.head				#for traversing pointing current to first node that is head
			while current.next !=None:  	#traversing till last element will stop at last element
				current = current.next 		#traversing one node at a time
			
			current.next = Node(data)		#inserting or appending ne node to the linked list



	def display_list(self):
		if self.head != None:
			current = self.head
			while current !=None:			#here as we have to also print last element have used current !=None instead of current.next !=None
				print(current.data,end =" ")
				current = current.next
			print("\n")
		else:
			print("Linked List is Empty")



	def find(self,element):
		found_flag =0
		res = self.isempty()
		if res == False: 
			current = self.head
			while current != None:
				if element == current.data:
					print("Element Found")
					found_flag =1
					break
				else:
					current = current.next
			if found_flag != 1:
				print("Element not found")



	def remove(self,element):
		deletion_flag =0
		if not  self.isempty():
			if element == self.head.data:
				self.head = self.head.next
			else:
				prev = self.head
				while prev.next != None:
					if prev.next.data == element:
						current = prev.next
						prev.next = current.next 
						print("Element deleted is ",current.data)
						deletion_flag =1
						#print("Printing Linked List after deletion")
						#self.display_list()
					else:
						prev = prev.next
				if deletion_flag !=1:
					print("Element not found")


	def isempty(self):
		if self.head ==None:
			print("    Linked List is empty")
			return True
		else :
			print("    Linked list is not empty")
			return False



	def insert_multiple(self,list1):
		for element in list1:
			self.insert(element)
######################################################
		
#Creating object of LinkedList class
l1 = LinkedList()

#Inserting elements in linked list
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.insert(40)
l1.insert(50)
l1.insert(60)

#Displaying elements in Linked List
print("=================================================")
print("Printing Elements after Inserting in Linked List")
l1.display_list()

#Finding element in Linked List
element = 20
print("=================================================")
print("Element to be found is : {}".format(element))
l1.find(element)

#Removing Element from Linked List
element = 40
print("=================================================")
print("Element to be removed from Linked List is :  {}".format(element))
l1.remove(element)


print("=================================================")
print("Printing Elements after removing : {}".format(element))
l1.display_list()


list1 = [11,21,31,41,51,61]
l1.insert_multiple(list1)


#Displaying elements in Linked List
print("=================================================")
print("Printing Elements after Inserting multiple elements at once using list in Linked List")
l1.display_list()

