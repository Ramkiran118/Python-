                     ####                 LOOPS                 ####

#  WHILE LOOP :

# i=1
# while i<=6:
#     print(i,)
#     i+=1

# 1) PRINT NUMBERS FROM 1 TO 100 :

# print("The numbers are :",end=" ")
# i=1
# while i<=100:
#     print(i,end=" ")
#     i+=1


# 2) PRINT NUMBERS FROM 100 TO 1 :

# i=100
# while i>=1:
#     print(i)
#     i-=1


# 3) PRINT THE MULTIPLICATION TABLE OF A NUMBER n :

# n=int(input("enter the number :"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1


# 4) PRINT THE ELEMENTS OF THE FOLLOWING LIST USING A LOOP :
# [1,4,9,16,25,36,64,81,100]

# nums=[1,4,9,16,25,36,64,81,100]
# idx=0
# while idx < len(nums):
#     print(nums[idx])
#     idx+=1

# 5) SEARCH FOR A NUMBER 'x' IN THIS TUPLE USING LOOP :
# (1,4,9,16,25,36,49,64,81,100)

# nums=(1,4,9,16,25,36,49,64,81,100)
# X=36
# i=0
# while i<len(nums):
#     if(nums[i]==X):
#         print("found at idx",i)
#     else:
#         print("not found")
#     i+=1

# BREAK :

# i=1
# while i<=5:
#     print(i)
#     if(i==4):
#         break
#     i+=1
# print("code ended")

# CONTINUE :

# i=1
# while i<=5:
#     if(i==4):
#         i+=1
#         continue
#     print(i)
#     i+=1

#     FOR LOOPS :

# nums=(2,4,6,8,10,12)
# for val in nums:
#     print(val)

# 1) PRINT THE ELEMENTS OF THE FOLLOWING LIST USING FOR LOOP :
#[1,4,9,16,25,36,49,64,81,100]

# nums=[1,4,9,16,25,36,49,64,81,100]
# for element in nums:
#     print(element,end=" " )

# 2) SEARCH FOR A NUMBER "x" IN THIS TUPLE USING FOR LOOP :
#(1,4,9,16,25,36,49,64,81,100)

# nums=(1,4,9,16,25,36,49,64,81,100)
# X=49
# i=0
# for element in nums:
#     if(X==element):
#         print("found at index :", i)
#     i+=1    

# RANGE :

# for val in range(0,11,2,):
#     print(val)

# 1)  PRINT NUMBERS FROM 1 TO 100 USING RANGE :

# for i in range(1,100,1):
#     print(i)

# 2) PRINT NUMBERS FROM 100 TO 1 :
 
# for i in range(100,0,-1):
#     print(i)

#   PRINT THE MULTIPICATION TABLE OF N :

# n=int(input("enter the number "))
# for i in range(1,11):
#     print(i*n)

#  PASS STATEMENT : (PASS):( PASS IN A NULL STATEMENT :)

# for el in range(1,100,5):
#     pass
    
# print("some use ful work is there :")


# 1) WAP TO FIND THE SUM OF FIRST N NUMBERS (USING WHILE LOOP ):

# n=int(input("enter the value :"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i+=1
# print(sum)

#             OR  

# n=int(input("enter the number"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("sum of the n numbers is :",sum)    

# 2) WRITE A PROGRAM TO FIND THE FACTORIAL OF FIRST N NUMBERS (USING FOR  LOOP  :):

# n=int(input("enter the number :"))
# factorial=1
# for i in range(1,n+1):
#     factorial*=i
# print("factorial of a number is : ", factorial)


