count = 0
total = 0
minimum = None
maximum = None

while True:

    # enter a number.
    number=input("Enter a number (enter 'done' to quit):")

    # If line startswith # continue
    if number.startswith ("#"):
        continue

    # If enters "done" break.
    if number.lower() == "done":
        break

    # count, total, minimum, and maximum (do not use min() or max()
    try:
        num = float(number)
    except ValueError:
        print("Invalid input, please enter a number.")
        continue

    count += 1
    total += num

    if minimum is None or num < minimum:
        minimum = num
    if maximum is None or num > maximum:
        maximum = num

    # print: Count: <count> Total: <total> Min: <min> Max: <max>

print(f"Count:< {count} >")
print(f"Total:< {total} >")
print(f"Min: < {minimum} >")
print(f"Max: < {maximum} >")



