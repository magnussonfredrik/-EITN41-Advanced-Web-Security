import base64
def bits_to_int(our_bits):
    return int(our_bits, 2)

def int_to_hex(our_int):
    return hex(our_int)[2:]

def hex_to_int(our_hex):
    return int(our_hex, 16)

def int_to_bits(our_bits, chars = 0):
    return "{0:b}".format(our_bits).zfill(chars)

def length_Long_Definite_Form(V):
    bytes_in_V_int = int(len(V) / 2)
    bytes_in_V_hex = int_to_hex(bytes_in_V_int)

    L = "---LENGTH-GOES-HERE-LDF---"

    # Do not allow half octets
    if len(bytes_in_V_hex) % 2 != 0:
        bytes_in_V_hex = "0" + bytes_in_V_hex

    if len(bytes_in_V_hex) > 2 or int_to_bits(bytes_in_V_int, 8)[0] == "1":
        bytes_in_L_int = int(len(bytes_in_V_hex) / 2)
        bytes_in_L_bits = int_to_bits(bytes_in_L_int, 7)
        bytes_in_L_bits = "1" + bytes_in_L_bits
        bytes_in_L_hex = int_to_hex(bits_to_int(bytes_in_L_bits))
        L = bytes_in_L_hex + bytes_in_V_hex
    else:
        L = bytes_in_V_hex

    return L

def DER_encode(integer, LDF=True):
    # print()
    T = "02"

    V = ""

    # # Pad V so it becomes even octets
    V = hex(integer)[2:]
    V_bits = "0" + int_to_bits(hex_to_int(V))
    if len(V_bits) % 8 != 0:
        missing_chars = 8 - (len(V_bits) % 8)
        V_bits = "0" * missing_chars + V_bits

    V_length = int(len(V_bits) / 8)
    V = int_to_hex(bits_to_int(V_bits))
    while V_length > len(V)/2:
        V = "0" + V


    L = "---LENGTH-GOES-HERE---"

    # Short definite form
    if V_length <= 127:
        # print("SDF")
        L = hex(V_length)[2:]
        if len(L) % 2 == 1:
            L = "0" + str(L)
        else:
            L = str(L)
    else:
        if LDF:
            # print("LDF")
            L = length_Long_Definite_Form(V)
        else:
            # print("LIF")
            # MUST BE HEX
            L = "10000000"
            V += "0" * 8 * 2

    # print("T: {}".format(T))
    # print("L: {}".format(L))
    # print("V: {}".format(V))
    return T + L + V

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def ass_3(p, q, e=65537):
    VERSION = 0
    n = p * q
    d = modinv(e, (p-1) * (q-1))
    exp1 = d % (p-1)
    exp2 = d % (q-1)
    coefficient = modinv(q, p)

    print("Version: {}".format(VERSION))
    print("n: {}".format(n))
    print("e: {}".format(e))
    print("d: {}".format(d))
    print("p: {}".format(p))
    print("q: {}".format(q))
    print("exponent1: {}".format(exp1))
    print("exponent2: {}".format(exp2))
    print("coefficient: {}".format(coefficient))

    DER_VERSION = DER_encode(VERSION)
    DER_n = DER_encode(n)
    DER_e = DER_encode(e)
    DER_d = DER_encode(d)
    DER_p = DER_encode(p)
    DER_q = DER_encode(q)
    DER_exp1 = DER_encode(exp1)
    DER_exp2 = DER_encode(exp2)
    DER_coefficient = DER_encode(coefficient)

    print()
    print("DER VERSION: {}".format(DER_VERSION))
    print("DER n: {}".format(DER_n))
    print("DER e: {}".format(DER_e))
    print("DER d: {}".format(DER_d))
    print("DER p: {}".format(DER_p))
    print("DER q: {}".format(DER_q))
    print("DER exponent1: {}".format(DER_exp1))
    print("DER exponent2: {}".format(DER_exp2))
    print("DER coefficient: {}".format(DER_coefficient))

    print()
    RSA_V = DER_VERSION + DER_n + DER_e + DER_d + DER_p + DER_q + DER_exp1 + DER_exp2 + DER_coefficient

    RSA_priv_key = DER_encode(hex_to_int(RSA_V))
    RSA_priv_key = "30" + RSA_priv_key[2:]

    print()
    print(RSA_priv_key)
    print()
    print(base64.b64encode(bytearray.fromhex(RSA_priv_key)))

ass_3(
    153654067345173519063152764593898887941847778866643857133324125539081576159222302163504563431415767925517478523801085695515805402234093964106382883616112560699608649630200301476104649443487068763537209861744915023867264470075932905999078280775685899539740289632802762703588979528170419262521108169901585305687, 
    96301784982268189923804491853083184485939466907363961207488354346647468640551402017823499423771418049927310939917755624693369549542757092070242852871459812828100540761920414458518545727049809649579679722065104556549642048862559459838218808059350594404857985785136943579724448705218378893632294170531647115967
)

integer = 101127179857726641365102595166127358082787212907017929383228536335881075913264021804529347558878357252012925513816744021936143657190238760172540927345404806308386790142262040049921117560001576264440361453516365417727897247061324603662711894040386651886534081033854250220869071500788431898363242414808948818423
#integer = 161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741
print(DER_encode(integer))