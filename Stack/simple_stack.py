#Stack using list


my_stack =[]

my_stack.append(10)
my_stack.append(20)
my_stack.append(30)
my_stack.append(40)
my_stack.append(50)
my_stack.append(60)


#Displaying elements in stack
print("=================================================")
print("Printing Elements after Inserting in queue ")
print(my_stack)


#Removing or popping element
element = my_stack.pop()
print("=================================================")
print("Element removed is : {} ".format(element))
print("Printing elements in queue after removal :\n",my_stack)

#Again pushing/appending an element
my_stack.append(70)
print("=================================================")
print("Printing Elements after Inserting in queue ")
print(my_stack)




