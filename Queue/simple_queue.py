#queue using list

class MyQueue:

	def __init__(self):
		self.my_queue = []

	def enque(self,data):
		self.my_queue.insert(0,data)

	def deque(self):
		return self.my_queue.pop()

	def isempty(self):
		if len(my_queue) == 0:
			print("Queue is empty")

	def display(self):
		print(self.my_queue)

#########################################



#################################################
mq1 = MyQueue()

mq1.enque(10)
mq1.enque(20)
mq1.enque(30)
mq1.enque(40)
mq1.enque(50)
mq1.enque(60)


#Displaying elements in stack
print("=================================================")
print("Printing Elements after Inserting in queue ")
mq1.display()


#Removing or popping element
element = mq1.deque()
print("=================================================")
print("Element removed is : {} ".format(element))
print("Printing elements in queue after removal :\n")
mq1.display()

#Again enqueing/appending an element
mq1.enque(70)
print("=================================================")
print("Printing Elements after Inserting in queue ")
mq1.display()
