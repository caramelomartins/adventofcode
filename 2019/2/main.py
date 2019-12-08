def calculate_output(codes):
    i = 0

    while i < len(codes):
        opcode = codes[i]

        if opcode == 1:
            bucket = codes[i+3]
            codes[bucket] = codes[codes[i+1]] + codes[codes[i+2]]
            i += 4
        elif opcode == 2:
            bucket = codes[i+3]
            codes[bucket] = codes[codes[i+1]] * codes[codes[i+2]]
            i += 4
        elif opcode == 99:
            return codes[0]
        else:
            exit("Something went wrong. Opcode: {}.".format(opcode))

with open("input.txt") as file:
    codes = list(map(int, file.readline().split(",")))

    print("\nPosition 0: {}.".format(calculate_output(codes.copy()))) 

    for x in range(0, 100):
        for y in range (0, 100):
            codes[1] = x
            codes[2] = y

            output = calculate_output(codes.copy())

            if output == 19690720:
                print("Noun: {}.".format(x))
                print("Verb: {}.".format(y))
                print("Calculation: {}.".format(100 * x + y))

