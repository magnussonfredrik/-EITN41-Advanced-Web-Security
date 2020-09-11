from hashlib import sha1
file = open('merklepath.txt')


def string_to_hash(tohash):
    return sha1(bytearray.fromhex(tohash)).hexdigest()

lines = []

for line in file.readlines():
    lines.append(line.strip("\n"))

hash = lines[0]

for i in range(1, len(lines)):
    if lines[i].startswith("R"):
        string = lines[i].strip("R")
        hash = hash + string
        hash = string_to_hash(hash)
    if lines[i].startswith("L"):
        string = lines[i].strip("L")
        hash = string + hash
        hash = string_to_hash(hash)

print(hash)
