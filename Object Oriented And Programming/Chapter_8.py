                 ####                   OBJECT ORIENTED PROGRAMMING SYSTEM                     ####

#   CLASS :

#CLASS CREATING :

# class Student:
#     name="kiran"

#CREATING OBJECT (INSTANCE) :

# s1=Student()
# print(s1.name)    

#EXAMPLE :
# class car:
#     color="blue"
#     brand="Audi"
# car1=car()
# print(car1.color)
# print(car1.brand)

## CONSTRUCTOR :

# __init__ FUNCTION :

# class students:
#     def __init__(self,fullname):
#         self.name=fullname
# s1=students("kiran")
# print(s1.name) 

#EXAMPLE :

# class student:
#     def __init__(self,fullname):
#         self.name=fullname
#         print("adding new student in database...")

# s1=student("kiran")
# print(s1.name)
# s2=student("ram")
# print(s2.name)

# Example :

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("adding new student to database...")
# s1=student("kiran",97)
# print(s1.name,s1.marks)
# s2=student("Ram",100)
# print(s2.name,s2.marks)


# CLASS AND INSTANCE ATTRIBUTES :( The object attributes gets the more priority than class attributes .)

# class student:
#     college_name="kPRIT"
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("adding the new student data to  database ...")
# s1=student("Kiran",99)
# print(s1.name)


## METHODS : methods are functions that belongs to  objects .

# class student:
#     def __init__(self,fullname):
#         self.name=fullname

#     def hello(self):
#         print("hello",self.name)

# s1=student("Ram Kiran")
# s1.hello()

# PRACTICE :
# 1 ) CREATE STUDENT CLASS THAT TAKES NAME AND MARKS OF 3 SUBJECTS AS ARGUMENTS IN A CONSTRUCTOR . THEN CREATE A METHOD TO PRINT THE AVERAGE . 

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("Hi",self.name,sum/3)
# s1=student("Ram Kiran",[99,98,100])
# s1.get_avg()


## STATIC METHOD :

# class student:
#     @staticmethod
#     def college():
#         print("KPRIT college")

### IMPORTANT CONCEPTS :
#  1) ABSTRACTION 
#  2) ENCAPSULATION

# PRACTICE :
 
# CREATE A ACCOUNT CLASS WITH 2 ATTRIBUTES BALANCE AND ACCOUNT NO. CREATE METHOODS FOR DEBIT, CREDIT AND PRINTING THE BALANCE .

# class Account:
#     def __init__(self,Balance,Account_no):
#         self.Balance=Balance
#         self.Account_no=Account_no

#     def debit(self,amount):
#         self.Balance-=amount
#         print("Rs.", amount,"was debited.")
#         print("The Total Balance is = ",self.get_Balance())

#     def credit(self,amount):
#         self.Balance+=amount
#         print("RS.",amount,"was Credited.")
#         print("The Total Balance is = ",self.get_Balance())

#     def get_Balance(self):
#         return self.Balance           
    
# acc1=Account(1000,12345)
# acc1.debit(1000)
# acc1.credit(10000)
# acc1.debit(7500)
# acc1.credit(40000)
# acc1.debit(100)


