def calculation_salary(basic_salary):
    hra = basic_salary * 0.20
    da = basic_salary * 0.10

    gross_salary = basic_salary + hra + da

    tax = gross_salary * 0.05

    net_salary = gross_salary - tax

    return hra, da, tax, net_salary


def main():
    basic_salary = float(input("Enter the salary of emoplyee: "))

    hra, da, tax, net_salary= calculation_salary(basic_salary)

    print("\n===== Salary Slip =====")
    print(f"Basic Salary : ₹{basic_salary:.2f}")
    print(f"HRA (20%)    : ₹{hra:.2f}")
    print(f"DA (10%)     : ₹{da:.2f}")
    print(f"Tax (5%)     : ₹{tax:.2f}")
    print(f"Net Salary   : ₹{net_salary:.2f}")

main()