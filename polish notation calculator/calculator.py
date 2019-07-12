def chooser(arg1: int, arg2: int, operator: str) -> int:
    switch = {("+", "add"): arg1 + arg2,
              ("-", "sub"): arg1 - arg2,
              ("*", "mul"): arg1 * arg2,
              ("/", "div"): arg1 / arg2}
    print(switch)
    for item in switch:
        if operator in item:
            a = switch[item]
    return a

def float_checker(fl_value: str) -> bool:
    if fl_value[0] != "." and fl_value[-1] != "." and fl_value.replace(".","", 1).isdecimal():
        return True

def integer_checker(int_value: str) -> bool:
    if int_value.lstrip("-").isdecimal():
        return True

operators = {"add", "+", "sub", "-", "mul", "*", "div", "/"}

while True:
    inp = input("please pass function /function number number/ " ).split()
    if len(inp) != 3 or inp[0] not in operators:
        print("please pass in 3 values with correct operator")
        continue
    elif integer_checker(inp[1]) and integer_checker(inp[2]):
        first = int(inp[1])
        second = int(inp[2])
        break
    elif float_checker(inp[1]) and float_checker(inp[2]):
        first = float(inp[1])
        second = float(inp[2])
        break
    print("for value 1 and 2 pass in integers")

print(chooser(first, second, inp[0]))
