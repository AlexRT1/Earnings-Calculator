# print("hello user")
# employee_name = input("what is the employee name? ").title().strip() 
# # could have added in the . title().strip here 
# employee_wage = input("what is the employee hourly rate? ")
# employee_hours_worked = input("how many hours did the employee work? ")

# perfect_example = employee_name.title().strip()

# print(perfect_example)

# wage = float(employee_wage)
# hours = float(employee_hours_worked)

# print(f"{perfect_example} made ${wage * hours} this week")

# # # ${earnings:.2f} how to do rounding 


# # # print(bool("-1")) any non empty str is true botch
# # # Quite often we want to explicitly check that two values are equal. In that case, we can use the == operator.
# # # != not =

# # a = [1, 2, 3]
# # b = a
# # b.append(0)

# # print(a)



# # start of coding while vinny is away oh yeah

# numbers = [1, 2, 3, 4]
# new_numbers = numbers + [5]

# print (numbers == new_numbers)

# numbers = [1, 2, 3, 4]
# numbers.append(5)

# print(id(numbers))
# print(id(new_numbers))

# user_number = input ("what number are you thinking of? " )

# print(int(user_number))
# if int(user_number) > 0 :
#     print( "your number is more than 1 ")

# elif int(user_number) == 0 :
#     print("your number is 0")

# else :
#     print ("your number is less than 1 ")

# # ask vinny why elseif int(user_number) < 1 :
#     # print ("your number is less than 1 ") doesnt work


# # hours_worked = input("how many hours have you worked this week ? ")
# # wage = input(" how much are you paid per hour? ")

# # hours_worked = int(hours_worked)

# # if hours_worked > 40:
# #     regular_pay = 40 * wage
# #     # overtime_pay = (hours_worked - 40) * wage * 1.1
# #     # owed_pay = int(regular_pay + overtime_pay)

# #     # print(f"You are owed ${owed_pay}.")
# # else:
# #     owed_pay = int(hours_worked * wage)
    
# # print(f" you are owed ${owed_pay}.")

# employeer = [
#     ("Rolf Smith", 35, 8.75),
#     ("Anne Pun", 30, 12.50),
#     ("Charlie Lee", 50, 15.50),
#     ("Bob Smith", 20, 7.00)
# ]

# for employee in employeer:
#     total_pay = employee[1] * employee[2]
#     print(f"{employee[0]} has to be paid £{total_pay}")    
# # 1st is finding the hours 2d finding the wage finding name

# for highest_wage in employeer
#     total_pay = employee[1] * employee[2]
    

# fizzbuzzz




for number in range(0, 101) :
    if (number / 3).is_integer() and (number / 5).is_integer() :
        print("Fizz Buzz")
    elif (number % 3 == 0) :
         print("Fizz")
    elif (number % 5 == 0) :
         print("Buzz")
    else :
        print(number)




