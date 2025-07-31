                  ####                   FUNCTIONS AND RECRUSION              ####

###      FUNCTIONS  :

# SYNTAX : 

# def functionName(parameter1 , parameter2,..):  # function definition 
#     #some work 
#     return value
# functionName(arg1,arg2) # function call 

# EXAMPLE :

# def sum(a,b):
#     sum=a+b
#     return sum
# print(sum(2,3))    

# example 2  :

# def calculate_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# calculate_sum(2,3)

# example 3 :

# def cal_sum(a,b):
#     return a+b
# sum=cal_sum(10,20)
# print(sum)

# AVERAGE OF 2 NUMBERS :

# def calc_average(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
#     return avg
# calc_average(1,1,1)

# 1) WAP TO PRINT THE LENGTH OF A LIST (LIST  IS THE PARAMETER ):
 
# cities=["Hyderabad","Chennai","Mumbai", "Delhi","Banguluru"]

# def print_len(list):
#     print(len(list))
# print_len(cities)


# 2) WAP  TO PRINT THE ELEMENTS OF A LIST IN A SINGLE LINE( LIST IS THE PARAMETER ):

# colors=["red","blue","green","yellow","pink","white","black"]
# def print_list(list):
#     for items in list:
#         print(items,end=" ")
# print_list(colors)        

# 3) WRITE A FUNCTION TO FIND THE FACTORIAL OF N (N IS THE PARAMETER ):

# def cal_fact(n):
#     factorial=1
#     for i in range(1,n+1):
#         factorial*=i
#     print("The Factorial is :",factorial)        
# cal_fact(5)    


# 4) WAF TO CONVERT USD TO INR :

# def convert(usd_value):
#     inr_value=usd_value*83
#     print(usd_value,"USD =",inr_value,"INR")
# convert(5)    


# RECURSION :

# exmaple :

# def show(n):  # function 
#     if(n==0):  # base case 
#         return
#     print(n)
#     show(n-1)  # recrusion function 
# show(5)       # function call 

# EXAMPLE : WAP TO CALCULATE THE FACTORIAL OF A NUMBER USING RECRUSION :

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return fact(n-1)*n
# print(fact(5))


# 1) WIRTE A RECURSIVE FUNCTION TO CALCULATE THE SUM OF FIRST N NATURAL NUMBERS :

# def calc_sum(n):
#     if(n==0):
#         return 0
#     return calc_sum(n-1) + n
# print(calc_sum(5))


# 2) WRITE A RECURSIVE FUNCTION TO PRINT ALL ELEMENTS IN A LIST :(HINT : USE LIST AND INDEX AS PARAMETER ):

# colors=["red","blue","green","yellow","pink","white","black"]
# def print_list(list,indx=0):
#     if(indx==len(list)):
#         return
#     print(list[indx])
#     print_list(list,indx+1)
# print_list(colors)    

