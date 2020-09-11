
def xor_calculator(string1, string2):
    result = int(string1, 16) ^ int(string2, 16)
    return ('{:x}'.format(result)).upper()

def get_message(broadcast, DA, DB):
    result1 = xor_calculator(broadcast, DA)
    result2 = xor_calculator(result1, DB)
    return result2

SA = input("Enter SA:")
SB = input("Enter SB:")
DA = input("Enter DA:")
DB = input("Enter DB:")
M = input("Enter message:")
b = int(input("Enter b:"))

if b == 0:
    broadcast = xor_calculator(SA, SB)
    message = get_message(broadcast, DA, DB)
    print(broadcast + message)
elif b == 1:
    broadcast = xor_calculator(SA, SB)
    message = get_message(M, DA, DB)
    print(message)
#print(xor_calculator('aaaa','0879'))
