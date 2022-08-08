print("hello user")
employee_name = input("what is the employee name? ") 
# could have added in the . title().strip here 
employee_wage = input("what is the employee hourly rate? ")
employee_hours_worked = input("how many hours did the employee work? ")

perfect_example = employee_name.title().strip().lower()

print(perfect_example)

wage = float(employee_wage)
hours = float(employee_hours_worked)

print(f"{perfect_example} made ${wage * hours} this week")

# ${earnings:.2f} how to do rounding 