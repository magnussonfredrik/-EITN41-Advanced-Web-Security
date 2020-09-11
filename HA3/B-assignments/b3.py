import hashlib
from random import randint
import matplotlib.pyplot as plot

m = hashlib.sha1()

all_k = [i for i in range(2**16)]

def commitment_scheme(v, k, x):
    m.update(bytearray(v.to_bytes((v.bit_length()+ 7 ) // 8, 'big')) + bytearray(k.to_bytes((k.bit_length()+7) // 8, 'big')))
    return int.from_bytes(m.digest(), 'big') % 2 ** x

def bind(x):
    c0 = [commitment_scheme(0, k, x) for k in range(2 ** 16)]
    c1 = [commitment_scheme(1, k, x) for k in range(2 ** 16)]
    if set(c0) & set(c1):
        return 1
    return 0


def binding_probability():
    return [bind(x) for x in range(0, 40)]

def conceal(x):
    rand = randint(0, 1)
    commit = commitment_scheme(0, randint(0, 2**16), x)
    collision0 = [commitment_scheme(0, k, x) for k in range(2 ** 16)]
    collision1 = [commitment_scheme(1, k, x) for k in range(2 ** 16)]
    commits = {0: [], 1: []}

    for collision in collision0:
        if commit == collision:
            commits[0].append(commit)
    for collision in collision1:
        if commit == collision:
            commits[1].append(commit)
    return len(commits[0])/(len(commits[0])+len(commits[1]))

    #print(count0/(count0+count1))
    #print(count0, count1)

def concealing_probability():
    return [iterate_conceal(x) for x in range(0, 40)]

def iterate_conceal(x):
    prob = [conceal(x) for y in range (50)]
    print(sum(prob)/len(prob))
    return sum(prob)/len(prob)

plot.plot(range(0, 40), binding_probability(), label="Binding")
plot.plot(range(0, 40), concealing_probability(), label="Conceiling")
plot.ylabel("Probability")
plot.xlabel("Hash length in bits")
plot.show()






#all_k = [int_to_bits(value) for value in list]
