# PRINT THE NUMBERS FROM 1 TO 100

# for i in range(1,101):
#     print(i,end=" ")

# PRINT THE NUMBERS FROM 100 TO 1

# for i in range(100,0,-1):
#     print(i,end=" ")

# WAP PRINT THE MULTIPLICATION TABLE OF A 

# number=int(input("Enter the number :"))
# for i in range(1,11):
#     print(f"{number} X {i}={number*i}")

# for i in range(5):
#     if(i==3):
#         continue
#     print(i)
#     i+=1

# for i in range(5):
#     if(i==3):
#         break
#     print(i)
#     i+=1

# WAP TO FIND THE SUM OF FIRST N NATURAL NUMBERS (USING WHILE LOOP):

# number=int(input("enter the n value:"))
# i=1
# sum=0
# while(i<=number):
#     sum+=i
#     i+=1
# print(f"The sum of First N Natural Numbers is :{sum}")    

# USING FOR LOOP

# number=int(input("Enter the number:"))
# sum=0
# for i in range(number):
#     i+=1
#     sum+=i
# print(sum)

# WAP TO FIND THE FACTORIAL OF FIRST N NATURAL NUMBER

# number=int(input("Enter the number :"))
# factoral=1
# for i in range(number,0,-1):
#     factoral=factoral*i
# print(factoral)

# n=int(input("Enter the number :"))

# factorial=1
# i=1
# while(i<=n):
#     factorial=factorial*i
#     i+=1
# print(factorial)

# LISTS:

# WAP TO ASK THE USER TO ENTER NAMES OF THEIR 3 FAVORATE MOVIES AND STORE THEM IN A LIST

# list=[]
# list.append("jaanu")
# list.append("salaar")
# list.append("ba4ed4rf4rf32ewds32wsxz32wqsaxzahubali")
# print(list)

list=[]
for i in range(1,4):
    user=input(f"Enter fav movie {i}: ")
    list.append(user)
print(list)
