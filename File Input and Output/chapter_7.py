                 ####                FILE INPUT / OUTPUT                 ####
# SYNTAX :
# f=open ("file_name","mode")
#data=f.read()
#f.close()
 
###  reading a file ###

# f=open("hello.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()

### writing a file ###

# f=open("world.txt","w")
# f.write("iam ramkiran randhi.")
# f=open("world.txt","r")
# data=f.read()
# print(data)

### Appending a file ###

# f=open("world.txt","a")
# f.write(" from Kommuri prathap reddy college.")
# f=open("world.txt","r")
# data=f.read()
# print(data)

###  deleting a file  ###

# import os
# os.remove("file_name")

#  PRACTICE QUESTION :

#  1) CREATE A NEW FILE "PRACTICE.TXT" USING PYTHON AND ADD THE FOLLOWING DATA IN IT :
#(HELLO  EVERYONE
# WE ARE LEARNING PYTHON
# USING VS CODE )

# with open("practice.txt","w") as f: 
#     f.write("Hello Everyone \n we are learning python \n using VS-code")
# f=open("practice.txt","r")
# data=f.read()
# print(data)

# 2) WAF THAT REPLACES ALL OCCURENCES OF THE "JAVA" WITH "PYTHON" IN ABOVE FILE :

# with open("practice.txt","r") as f:
#     data=f.read()
# new_data=data.replace("python","java")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)

# 3) WAF TO FIND IN WHICH LINE OF THE FILE DOES THE WORD "LEARNING" OCCURES FIRST . PRINT -1 IF WORD NOT FOUND.
# def check_for_line():
#     word="learning"
#     data=True
#     line_no=1
#     with open("practice.txt","r")as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no+=1
#         return-1
# print(check_for_line())  


# 5)  FROM A FILE CONTAINING NUMBERS SEPERATED BY COMMA, PRINT THE COUNT OF EVEN NUMBERS :

# count=0
# with open("practice.txt","r") as f:
#     data=f.read()
#     nums=data.split(",")
#     for val in nums:
#         if(int(val)%2==0):
#             count+=1
# print(count)        

# f=open("write.txt","w")
# f.write("Iam Ramkiran Randhi Pursing in btech in kommuri prathap reddy  college.")

# f=open("write.txt","r")
# data=f.read()
# print(data)

# f=open("write.txt","a")
# f.write(" Iam good at Java , Python, C-language .")

# with open("write.txt","r") as f:
#     data=f.read()
# new_data=data.replace("Python","machine learning") 
# print(new_data)   
# with open("write.txt","w") as f:
#     f.write(new_data)














