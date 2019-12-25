#Stack using list

class MyQueue:

	def __init__(self):
		self.my_stack =[]


	def push(self,data):
		self.my_stack.append(data)


	def pop(self):
		return self.my_stack.pop()


	def isempty(self):
		if len(my_stack) == 0:
			print("Stack is Empty ")
		else:
			print("Stack is not Empty")


	def display(self):
		print(self.my_stack)	




#################################################
mq1 = MyQueue()

mq1.push(10)
mq1.push(20)
mq1.push(30)
mq1.push(40)
mq1.push(50)
mq1.push(60)


#Displaying elements in stack
print("=================================================")
print("Printing Elements after Inserting in queue ")
mq1.display()


#Removing or popping element
element = mq1.pop()
print("=================================================")
print("Element removed is : {} ".format(element))
print("Printing elements in queue after removal :\n")
mq1.display()

#Again pushing/appending an element
mq1.push(70)
print("=================================================")
print("Printing Elements after Inserting in queue ")
mq1.display()





