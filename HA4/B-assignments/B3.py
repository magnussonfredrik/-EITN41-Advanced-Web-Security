import hashlib
import math

k = 128

def MGF1 (mgfSeed, maskLen, hashLen = 20):
    if maskLen > 2 ** 32:
        return "mask too long"
    T = ""
    for i in range(int(math.ceil(maskLen / hashLen))):
        C = I20SP(i, 4)
        T += hashlib.sha1(bytearray.fromhex(mgfSeed + C)).hexdigest()
    return T[:2 * maskLen]


def I20SP(x, xLen):
    if x > 256 ** xLen:
        return "integer too large"
    # Remove 0x and fill with zeros in order to
    return hex(x)[2:].zfill(2 * xLen)

#print(MGF1('46dad84c7fa3460344bda67c31e8f948addb0649f13b7509', 24))

def OAEP_encode(message, seed):
    L = ""
    lHash = hashlib.sha1(bytearray.fromhex(L)).hexdigest()
    PS = L.zfill(2 * k - len(message) - (20 * 4) - 4)
    DB = lHash + PS + '01' + message
    dbMask = MGF1(seed, k - 20 - 1)
    maskedDB = int(DB, 16) ^ int(dbMask, 16)
    maskedDB = hex(maskedDB)[2:]
    seedMask = MGF1(maskedDB, 20)
    maskedSeed = int(seed, 16) ^ int(seedMask, 16)
    maskedSeed = hex(maskedSeed)[2:]
    EM = '00' + maskedSeed + maskedDB
    EM = EM.zfill(256)
    return EM[:256]

def OAEP_decode(encoded_message):
    L = ""
    lHash = hashlib.sha1(bytearray.fromhex(L)).hexdigest()
    #separate the encoded message:
    Y = encoded_message[:2]
    maskedSeed = encoded_message[2 : 20 * 2 + 2]
    maskedDB = encoded_message[20 * 2 + 2:]
    seedMask = MGF1(maskedDB, 20)
    seed = hex(int(maskedSeed, 16) ^ int(seedMask, 16))[2:]
    dbMask = MGF1(seed, k - 20 - 1)
    DB = hex(int(maskedDB, 16) ^ int(dbMask, 16))[2:]
    separated_lHash = DB[:20 * 2]
    PSIndex = DB[20 * 2:].find("01")
    if PSIndex == -1:
        return "decryption error"
    PS = DB[2 * 20 : PSIndex]
    M = DB[20*2 + len(PS) + 2:]
    if separated_lHash != lHash or Y != '00':
        return "decryption error"

    return M.lstrip("0")[1:]



#print(OAEP_encode("0b12625e83ce789cbcc60e9f469b76f95fcd76815eb508470892be8a56", "1e652ec152d0bfcd65190ffc604c0933d0423381"))
print(OAEP_decode("00451e66a5e9b51f00abe919cfa277b237008087def9d3778a18b7aa067f90b2178406fa1e1bf77f03f86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabdf472023d44ef55c4a40d1ce16608342d9b31f7fab5270ff56cf8f962258890b9f78184c"))
