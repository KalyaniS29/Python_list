my_list= [1,2,3,"banana","apple"]
print(my_list)

#methods

#1. append=to add /end

my_list.append(4)
print(my_list)

#2. extend=combine

lst1=[1,2,3]
lst2=[4,5,6]

lst1.extend(lst2)
print(lst1)

#3 insert()= add anywhere

lst1.insert(3,"fruit")
print(lst1)

# remove()

lst1.remove("fruit")
print(lst1)

#pop()=last/ location

lst1.pop()
print(lst1)

lst1.pop(2)
print(lst1)

#clear()
lst1.clear()
print(lst1)

#index()

my_list=[1,2,"fruit","name","banana"]
a=my_list.index(2)
print(a)
b=my_list.index("banana")
print(b)

#count=frequency
my_list=[1,2,2,3,3,3,4,3,4,7,3,3]
c=my_list.count(3)
print(c)

#sort = arrange in ascending

my_list=[1,7,3,9,2]
my_list.sort()
print(my_list)

my_list=["banana","fruit","apple"]
my_list.sort()
print(my_list)

#reverse=flip
my_list=[6,9,3,8]
my_list.reverse()
print(my_list)

#copy
my_list=[1,2,3,4]
new_list=my_list.copy()
print(new_list)

