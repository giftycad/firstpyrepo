# lower_limit = int(input("Enter the lower limit: "))
# upper_limit = int(input("Enter lower limit: "))


# number_range = [x for x in range(lower_limit, upper_limit)]
# even_num = []
# odd_num = []
# for num in number_range:
#     if num % 2 == 0:
#         even_num.append(num)
#     else:
#         odd_num.append(num)


# print(even_num)
# print(odd_num)

# Lower_limit = int(input("Enter the first number for range: "))

# Upper_limit = int(input("Enter the second number for range: "))

# print("Even numbers are ")

# for value in range(Lower_limit, Upper_limit+1):
#     if(value % 2 == 0):

#         print(value)

# print("Odd numbers are ")

# for value in range(Lower_limit, Upper_limit+1):

#     if(value % 2 == 1):

#         print(value)
# low_lim = int(input(" Please enter the lower limit: "))
# up_lim = int(input("Please enter the lower limit: "))
# lower_range = low_lim+1
# output = input("Do you choose an even or odd number (Even/Odd): ")


lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter lower limit: "))
lower_range = lower_limit
choice = input("Even number or Odd number (E/O): ")


number_range = [x for x in range(lower_range, upper_limit)]
even_num = []
odd_num = []
for num in number_range:
    if num % 2 == 0:
        even_num.append(num)
else:
    odd_num.append(num)
if choice == "E":
    print(even_num)
elif choice == "O":
    print(odd_num)
