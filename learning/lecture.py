# mylist = ['rohit', 'om', 'merin', 'ritika', 'omkar','aditya', 'kunal']
# print(mylist[-5])
# print(mylist[1])
# mylist2 = [ 1, 'java' , 2 , 'python']
# print(mylist2[1])

# print(type(mylist))
# print(mylist[1])
# mylist2.pop(1)

# mylist2.remove(0)
# print(mylist2)


# num= [ 1, 2, 3]
# num2= [4 ,5 , 6]
# num3 =num+num2
# print(num3)

# num4= [5]
# num5= [6]
# new =num4+num5
# print(new)


# num = 1
# sum = 0
# while num<11:
#     sum+=num
#     num=num+1

# print("Sum of first 10 number = " , sum)


# fact =1 
# a = int(input("Enter number : "))
# num = a
# while(num>0):
#     fact*=num
#     num=num-1
# print("Factorial of " , a , " is: " , fact)

#Sum of Numbers and Reverse the digits



# num = int(input("Enter Numbers:"))
# sum = 0
# rev = 0
# while(num > 0):
#     rem = num % 10
#     num = num//10
#     sum += rem
#     rev = rev*10+rem
# print("Sum of Digits:",sum)
# print("Reverse of the Numbers:",rev)


# i = 1
# while(i<=5):
#     j = 1
#     while(j<=i):
#         print(i, end=" ")
#         j += 1
#     i += 1
#     print()


# ch = 65  # Initialize ch to 65, which is the ASCII code for 'A'
# i = 1    # Initialize i to 1

# while i <= 5:
#     j = 1
#     while j <= i:
#         print(chr(ch), end=" ")  # Print the character corresponding to ch
#         j += 1
#         ch += 1  # Increment ch by 1 after printing each character
#     i += 1
#     print()



# ch = 65
# i = 1

# while i <= 5:
#     j = 1
#     while j <= i:
#         print(chr(ch), end=" ")
#         j += 1
#     ch += 1  # Increment the character code by 1 after each row
#     i += 1
#     print()


# i = 5
# while i >= 1:
#     j = i
#     while j >= 1:
#         print(j, end=" ")
#         j -= 1
#     i -= 1
#     print()

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()






from datetime import datetime


date = datetime.today()
    

year_string = date.strftime("%M")


print(year_string)

