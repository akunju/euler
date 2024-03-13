def euler(x, stop, y, step_size):
    status = ""
    
    steps = int((stop - x) / step_size)
    if (int((stop - x) % step_size) != 0):
        status = "error1"

    if (stop <= x):
        status = "error2"
    
    if status == "":
        while steps > 0:
            slope = (6 * (x ** 3)) - (3 * y * (x ** 2))
            y += step_size * slope
            x += step_size
            steps -= 1
            print(y)
    else:
        print(status)

start = float(input("Starting x-value: "))
stop_value = float(input("Desired x-value: "))
initial = float(input("Starting y-value: "))
step_size = float(input("Step size: "))
print("Differential Function: 6x^3 - 3yx^2 \n")

euler(start, stop_value, initial, step_size)
