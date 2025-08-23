def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    third_line = []
    result_line = []

    for equation in problems:
        parts = equation.split()
        number1 = parts[0]
        operator = parts[1]
        number2 = parts[2]
        if number1.isdigit()==False or number2.isdigit()==False:
            return 'Error: Numbers must only contain digits.'
        if operator!='+' and operator!= '-':
            return "Error: Operator must be '+' or '-'."
        if len(number1)>4 or len(number2)>4:
            return 'Error: Numbers cannot be more than four digits.'
        maxi = max(len(number1), len(number2)) + 2  # Max width for alignment

        # First line (number1)
        space1 = maxi - len(number1)
        space1_str = ""
        for _ in range(space1):
            space1_str += " "
        first_line.append(space1_str + number1)

        # Second line (operator +  number2)
        space2 = maxi - len(number2) - 2
        space2_str = ""
        for _ in range(space2):
            space2_str += " "
        second_line.append(operator + " " + space2_str + number2)

        # Third line (-----)
        dash_line = ""
        for _ in range(maxi):
            dash_line += "-"
        third_line.append(dash_line)
        if operator == '+':
            number3 = int(number1) + int(number2)
        else:
            number3 = int(number1) - int(number2)

        rspace = maxi - len(str(number3))
        rspace_str = ""
        for _ in range(rspace):
            rspace_str += " "
        result_line.append(rspace_str + str(number3))


        firstspace=""
        if equation!=problems[-1]:
            for  x in range(4):
                firstspace+=' '
            first_line.append(firstspace)
            second_line.append(firstspace)
            third_line.append(firstspace)
            result_line.append(firstspace)
            

    array = ''.join(first_line) + '\n' + ''.join(second_line) + '\n' + ''.join(third_line)

    if show_answers:
        array += '\n' + ''.join(result_line)

    return array

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
