import gmpy2
import math
import base64

p = 2530368937
q = 2612592767
e = 65537
n = p * q
lambda_p = p - 1
lambda_q = q - 1
d = gmpy2.invert(e, (p-1)*(q-1))
exponent1 = d % (p-1)
exponent2 = d % (q-1)
coefficient = gmpy2.invert(q, p)

def decimal_to_hex(dec_value):
    hex_value = hex(dec_value)[2:]
    if len(hex_value) % 2 == 0:
        return hex_value
    new_hex_value = '0' + str(hex_value)
    return new_hex_value

def decimal_to_bits(our_bits, chars = 0):
    return "{0:b}".format(our_bits).zfill(chars)

def add_length(hex_value):
   length = str(math.ceil(len(hex_value)/2))
   print(length)
   return '0' + length + hex_value

def add_int_tag(value_to_tag):
    return '02' + value_to_tag

def decimal_to_der(dec_value):
    hex_val = decimal_to_hex(dec_value)
    new_hex_val = hex_val[:2]
    bin_val = bin(int(new_hex_val, 16))[2:].zfill(8)
    #print(new_hex_val)
    #print(bin_val)
    val_length = len(hex_val)
    binary = bin(val_length)[2:].zfill(math.ceil(val_length/2))
    #print(add_length(hex_val))
    #print(binary)

    if bin_val[0] == '1' :
        binary = '00' + hex_val
        return add_int_tag(add_length(binary))

    return add_int_tag(add_length(decimal_to_hex(dec_value)))

def process(hex_value):
    #new_hex = hex_value[:2]
    hex_value = '020100' + hex_value
    counter = int(len(hex_value)/2)
    heeeex = hex(counter)
    print(heeeex)
    print(counter)
    hex_counter = decimal_to_hex(counter)
    fin_val = '30' + hex_counter + hex_value
    return fin_val


print("Decimal:", n, "DER:", decimal_to_der(n))
print("Decimal:", e, "DER:", decimal_to_der(e))
print("Decimal:", d, "DER:", decimal_to_der(d))
print("Decimal:", p, "DER:", decimal_to_der(p))
print("Decimal:", q, "DER:", decimal_to_der(q))
print("Decimal:", exponent1, "DER:", decimal_to_der(exponent1))
print("Decimal:", exponent2, "DER:", decimal_to_der(exponent2))
print("Decimal:", coefficient, "DER:", decimal_to_der(coefficient))

combined = (decimal_to_der(n) + decimal_to_der(e) + decimal_to_der(d) + decimal_to_der(p) + decimal_to_der(q) + 
decimal_to_der(exponent1) + decimal_to_der(exponent2) + decimal_to_der(coefficient))

#print(len(combined))

new = process(combined)

#print(combined)

#print(new)

print(decimal_to_der(161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741))
