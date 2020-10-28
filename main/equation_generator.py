while True:
    print("Enter the values:\n")
    command = input()
    if command == "exit":
        break
    else:
        data = command.split(" ")
        x1 = int(data[0])
        y1 = int(data[1])
        x2 = int(data[2])
        y2 = int(data[3])

        m = (y2 - y1)/(x2 - x1)
        c = y1 - m*x1

        print("\n y = " + str(m) + "x + " + str(c) + "\n")
