print("Welcome to my python list pratice")

list1 = ["salman", "sindh", "pakistan"]
print(list1[0])
print(list1[1])
print(list1[2])

customer_list = ["Nexskill", 10, 2.5, True]
print(customer_list[0])
print(customer_list[1])
print(customer_list[2])
print(customer_list[3])
customer_list.append("Yahoo")
print(customer_list)
customer_list.insert(1,"jim")
print(customer_list)
print(type(customer_list[1]))
customer_list.remove("jim")
print(customer_list)

customer_list.pop(1)
print(customer_list)
      