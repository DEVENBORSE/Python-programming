def calculate_bill(units):
    if units <= 100:
        bill = units * 1.50

    elif units <= 300:
        bill = (100 * 1.50) + ((units - 100) * 2.50)

    elif units <= 500:
        bill = (100 * 1.50) + (200 * 2.50) + ((units - 300) * 4.00)

    else:
        bill = (
            (100 * 1.50)
            + (200 * 2.50)
            + (200 * 4.00)
            + ((units - 500) * 6.00)
        )

    return bill

def main():
    units = float(input("Enter the units: "))

    if units < 0:
        print("Invalid units entered!")
        return

    total_bill = calculate_bill(units)

    print("\n========== Electricity Bill ==========")
    print(f"Units Consumed : {units}")
    print(f"Total Bill     : ₹{total_bill:.2f}")
    print("=======================================")

main()