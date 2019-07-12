def C_to_F(arg):
    return arg * 9/5 + 32
def C_to_K(arg):
    return arg + 273.15
def F_to_C(arg):
    return arg - 32 * 5/9
def F_to_K(arg):
    return arg - 32 * 5/9 + 273.15
def K_to_C(arg):
    return arg - 273.15
def K_to_F(arg):
    return arg - 273.15 * 9/5 + 32

operations_map = {"C_to_Fahrenheit":"C_to_F", "C_to_F":"C_to_F",
                    "C_to_Kelvin":"C_to_K",   "C_to_K":"C_to_K",
                    "F_to_Celsius":"F_to_C",  "F_to_C":"F_to_C",
                    "F_to_Kelvin":"F_to_K",   "F_to_K":"F_to_K",
                    "K_to_Celsius":"K_to_C",  "K_to_C":"K_to_C",
                    "K_to_Fahrenheit":"K_to_F", "K_to_F":"K_to_F"}

first_format = {"C", "F", "K"}
second_format = {"C", "Celsius", "F", "Fahrenheit", "K", "Kelvin"}
while True:
    inp1 = input("Supported temperature formats are: 36.6 C | 97.88 F | 309.75 K \nPlease pass in convertion temperature: ")
    tempr = inp1.split()
    if len(tempr) != 2:
        print("Supported temperature formats: 36.6 C | 97.88 F | 309.75 K \nInput amount is {}: should be exactly 2".format(len(tempr)))
        continue
    tempr_value = tempr[0]
    tempr_format = tempr[1]
    if tempr_format not in first_format:
        print("{}, is not supported format of conversion".format(tempr_format))
        continue
    if tempr_value.lstrip("-").isdecimal():
        tempr_value = int(tempr_value)
        break
    elif tempr_value[0] != "." and tempr_value[-1] != "." and tempr_value.replace(".","",1).isdecimal():
        tempr_value = float(tempr_value)
        break

while True:
    inp2 = input("Convert to (C(elsius) | K(elvin) | F(ahrenheit)): ")
    conv = inp2.split()
    if len(conv) != 1:
        print("Supported conversion formats: (C(elsius) | K(elvin) | F(ahrenheit)) \nInput amount is {}: should be exactly 1".format(len(conv)))
        continue
    if conv[0] not in second_format:
        print("{} not in supported formats".format(inp2))
        continue
    else:
        break

operation = f"{tempr_format}_to_{inp2}"
print(operations_map[operation])

if tempr_format == inp2:
    print("Conversion result {} °{} = {} °{}".format(tempr_value, tempr_format, tempr_value, inp2))
else:
    print("Conversion resultss {} °{} = {} °{}".format(tempr_value, tempr_format, globals()[operations_map[operation]](tempr_value), inp2))
