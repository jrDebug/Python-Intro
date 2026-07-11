list = [1 , 2 , 3 , 4 , 5 , 6]
var1 = len(list)
list.append(7)
var2 = len(list)
print(var2 - var1)

list1 = {"zero" : 1 , "one" : 2 , "two" : 3 , "three" : 4 , "four" : 5 , "five" : 6}
print(list1["three"] * list1["five"])
list1["six"] = 7
print(list1)
