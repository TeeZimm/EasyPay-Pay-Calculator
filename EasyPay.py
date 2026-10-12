def main():

    # This section is for user input of their name.
    employee_name = input("Enter Employee Name: ")

    # This section rejects invalid user input for hours worked.
    while True:
        try:
            hours_worked = float(input("Enter Hours Worked: "))
            if hours_worked < 0:
                print("Number cannot be negative.")
            elif hours_worked > 168:
                print("Number cannot be greater than 168.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
                    
    # This section rejects invalid user input for hourly rate.
    while True:
        try:
            hourly_rate = float(input("Enter Hourly Rate: "))
            if hourly_rate < 0:
                print("Number cannot be negative.")
            elif hourly_rate == 0:
                print("Hourly rate cannot be 0.")
            elif hourly_rate > 500:
                print("Number cannot be greater than 500.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
            
    marital_status = input(
            "Enter Marital Status (Single/Married): "
        ).strip().lower()

    # This section rejects invalid user input for marital status.
    while marital_status != "single" and marital_status != "married":
        print("Please choose single or married.")
        marital_status = input(
            "Enter Marital Status (Single/Married): "
        ).strip().lower()
        
    # This section determines overtime hours based on user input.
    if hours_worked > 40:
        regular_hours = 40.0
        overtime_hours = hours_worked - 40.0
    else:
        regular_hours = hours_worked
        overtime_hours = 0.0
            
    # This section determines estimated deduction rate based on
    # marital status.
    if marital_status == "single":
        deduction_rate = 0.15
    else:
        deduction_rate = 0.12

    # This section details the pay calculations.
    regular_pay = round((regular_hours * hourly_rate), 2)
    overtime_rate = hourly_rate * 1.5
    overtime_pay = round(overtime_hours * overtime_rate, 2)
    gross_pay = round((regular_pay + overtime_pay), 2)
    deductions = round((gross_pay * deduction_rate), 2)
    net_pay = round((gross_pay - deductions), 2)

    # This is the formatted output.
    print("")
    print("--------------------------------")
    print("")
    print("Employee Name: ", employee_name)
    print("")
    print(f"Hours Worked: 	{hours_worked:.2f}")
    print(f"Hourly Rate: 	${hourly_rate:,.2f}")
    print(f"Overtime Rate: 	${overtime_rate:,.2f}")
    print("")
    print("--------------------------------")
    print("")
    print(f"Regular Pay: 	${regular_pay:,.2f}")
    print(f"Overtime Pay: 	${overtime_pay:,.2f}")
    print("")
    print("--------------------------------")
    print("")
    print(f"Gross Pay: 	${gross_pay:,.2f}")
    print(f"Deductions: 	${deductions:,.2f}")
    print(f"Net Pay: 	${net_pay:,.2f}")

if __name__ == "__main__":
    main()