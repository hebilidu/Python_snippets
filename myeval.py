# Program name : myeval
# Description  : emulate the Python "eval()" function
# Created on   : 210709 by: lidu
# Modified on  : 210709 by: lidu

def collect_input():
    string = input("Please enter an arithmetic expression ('q' to stop): ")
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
    print(expr_list)

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
            elif char in ['+','-','*',':']: # marks the end of current operand
                try:
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
        try:
            ops_list.append(float(buffer))
        except ValueError:
            has_invalid_operand = True
            return f"'{buffer}' is not a valid operand.\n"

    return ops_list



    # isinstance(x, (int, float))
    # 
    
    # calculate the expression result
    return expr_list

def main():
    """Main loop"""
    while True:
        input_string = collect_input()
        if input_string == 'QUIT':
            print("Thanks for your visit. Program ended.\n")
            break
        else:
            print(myeval(input_string))

if __name__ == "__main__":
    main()