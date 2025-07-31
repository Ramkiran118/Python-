             ####                    LISTS AND TUPLES :               ####
 


# LISTS :

# marks =[89,99,87,77,59]
# print(marks)
# print(type(marks))

# student=["Kiran",59,"Hyderabad"]
# print(student)
# print(type(student))

# marks =[89,77,59,99,29,39]
# print(marks[:4])
# print(len(marks[:5]))


# METHODS IN LISTS :

# 1) list.append:

# marks=[89,99,59,49,39,29]
# marks.append(48)
# print(marks)

# 2) list.sort():

marks=[89,99,59,49,39,29]
marks.sort()
print(marks)

# 3) list.sort(reverse=True):

# marks=[89,99,59,49,39,29]
# marks.sort(reverse=True)
# print(marks)

# 4) list.reverse():

# marks=[89,99,59,49,39,29]
# marks.reverse()
# print(marks)

# 5) list.insert(index,element):

# marks=[89,99,59,49,39,29]
# marks.insert(5,55)
# print(marks)

# 6) list.remove(number):

# marks=[89,99,59,49,39,29]
# marks.remove(59)
# print(marks)

# 7) list.pop(index):

# marks=[89,99,59,49,39,29]
# marks.pop(2)
# print(marks)




#  TUPLES :

# tup=(2,3,5,8,1)
# print(tup)
# print(type(tup))

#TUPLES METHODS :

# 1) tup.index(element):

# tup=(2,1,4,5,8,3)
# tup.index(1)
# print(tup)

# 2) tup.count(element):

# marks=(2,1,4,5,8,3)
# marks.count(5)
# print(marks.count(5))

# PRACTICE QUESTIONS :

# WAP to ask the user to enter names of their 3 favourate movies and store them in a list:

# movies=[]
# movies.append (input("enter the movie 1 name :"))
# movies.append (input("enter the movie 2 name :"))
# movies.append (input("enter the movie 3 name :"))

# print(movies)


# WAP to check if a list contains a palindrome of elememnts (Hint : use copy() method):

# list2=list(input("Enter the list :"))

# copy_list2=list2.copy()
# copy_list2.reverse()
# if(copy_list2 == list2):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# WAP to count the number of students with the 'A' grade in the following tuple ["C","D","A","A","B","B","A"]and store the above values in a list and store them from "A" to "D":

# grade=["C","D","A","A","B","B","A"]
# grade.sort()
# print(grade)

