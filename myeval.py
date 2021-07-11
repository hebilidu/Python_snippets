# Program name : myeval
# Description  : emulate the Python "eval()" function for the 4 basic arithmetic operations
# Created on   : 210709 by: lidu
# Modified on  : 210711 by: lidu

def collect_input():
    string = input("Please enter an arithmetic expression with the four basic operators +, -, *, / ('q' to stop): ")
    if string in ("q", "Q"):
        return "QUIT"
    else:
        return string

def myeval(expression):
    """emulate the Python 'eval() function"""
    # check the expression is not empty
    if expression == "":
        return f"Empty expression. Try again.\n"

    result = ""
    expr_list = list(expression)

    # check expression contains only valid characters (incl. spaces)
    valid_chars_only = True
    for char in expr_list:
        if char not in ['+','-','*','/','.',' '] and not char.isdigit():
            valid_chars_only = False
            buffer = ""
            result += f"'{char}' is not a valid character.\n"
    if not valid_chars_only:
        return result + "Try again.\n"

    # build list of operators and operands
    ops_list = []
    buffer = ""
    has_invalid_operand = False    
    for char in expr_list:
        if buffer == "":
            if char in ['+','-'] or char.isdigit():
                buffer += char
            elif char == " ":
                pass
            else:
                has_invalid_operand = True
                result = f"'{char}' is an invalid character to start an operand.\n"
        else:
            if char in [' ','.'] or char.isdigit():
                buffer += char
            elif char in ['+','-','*','/']: # marks the end of current operand
                try: # store operand and operator
                    ops_list.append(float(buffer))
                    ops_list.append(char)
                    buffer = ""
                except ValueError:
                    has_invalid_operand = True
                    result = f"'{buffer}' is not a valid operand.\n"
        if has_invalid_operand:
            return result

    if buffer == "": # empty buffer at this stage means the last operand is missing
        return f"The expression '{expression}' is incomplete"
    else:
        try: # do we have a regular floating number?
            ops_list.append(float(buffer))
        except ValueError: # apparently not
            has_invalid_operand = True
            return f"'{buffer}' is not a valid operand.\n"

    # print(ops_list) # test instruction
    
    # calculate the expression result
    if len(ops_list) == 1: # particular case when expression is just a number
        return f"{expression} = {ops_list[0]}"
    # first pass on ops_list to execute the priority operations (* and /)
    reduced_ops_list =[ops_list[0]]
    for i,j in enumerate(ops_list):
        if j == '*':
            reduced_ops_list.append(reduced_ops_list.pop() * ops_list[i+1])
        elif j == '/':
            try:
                reduced_ops_list.append(reduced_ops_list.pop() / ops_list[i+1])
            except ZeroDivisionError:
                return "Division by zero error!"
        elif j in ['+', '-']:
            reduced_ops_list.extend([ops_list[i-1], ops_list[i], ops_list[i+1]])

    # print(reduced_ops_list) # test instruction

    # second pass to execute the non priority operations (+ and -)
    result = reduced_ops_list[0]
    for i,j in enumerate(reduced_ops_list):
        if j == '+':
            result += reduced_ops_list[i+1]
        elif j == '-':
            result -= reduced_ops_list[i+1]

    return f"{expression} = {result}"

def main():
    """Main loop"""
    while True:
        input_string = collect_input()
        if input_string == 'QUIT':
            print("Thanks for your visit. Program ended.\n")
            break
        else:
            print(myeval(input_string), '\n')

if __name__ == "__main__":
    main()