import ipaddress
from itertools import combinations

from pcapfile import savefile


q1nazir = "159.237.13.37"
q1mix= "94.147.150.188"
q1m = 2
q1file = "cia.log.1337.pcap"

q2nazir = "161.53.13.37"
q2mix = "11.192.206.171"
q2m = 12
q2file = 'cia.log.1339.pcap'

q3file = 'cia.log.3.pcap'
q3mix = "95.235.155.122"
q3nazir = "61.152.13.37"

testcap = open(q3file, 'rb')

capfile = savefile.load_savefile(testcap, layers=2, verbose=True)

partitions = []


chunks = [capfile.packets[x:x+136] for x in range(0, len(capfile.packets), 136)]


for partition in chunks:
    for pkt in partition:
        ip_src = pkt.packet.payload.src.decode('UTF8')
        if ip_src == q3nazir:
            partitions.append(partition)
all_ips = []
for partition in partitions:
    temp = []
    for pkt in partition:
        if pkt.packet.payload.src.decode('UTF8') == q3mix:
            temp.append(pkt.packet.payload.dst.decode('UTF8'))
    all_ips.append(temp)

print(len(all_ips))

def find_m_exclusive_disjoints(list, m):
    while True:
        exclusive_disjoints = []
        for batch in list:
            union = set().union(*exclusive_disjoints)
            if union & set(batch):
                continue
            else:
                exclusive_disjoints.append(batch)
        if len(exclusive_disjoints) == m:
            return exclusive_disjoints

def intersect(all_ips, m):
    exclusive_disjoints = find_m_exclusive_disjoints(all_ips, m)
    return_addresses = []
    for batch in all_ips:
        for i in range(len(exclusive_disjoints)):
            if set(exclusive_disjoints[i]) & set(batch):
                other_disjoints = [len(set(exclusive_disjoints[j]) & set(batch)) == 0 for j in range(len(exclusive_disjoints)) if j != i]

                # for j in range(len(exclusive_disjoints)):
                #     boollist = []
                #     if j != i:
                #         boollist.append(not set(exclusive_disjoints[j]) & set(batch))
                # if all(boollist):




                if all(other_disjoints):
                    exclusive_disjoints[i] = set(exclusive_disjoints[i]) & set(batch)
                    if len(exclusive_disjoints[i]) == 1 and next(iter(exclusive_disjoints[i])) not in return_addresses:
                        return_addresses.append(next(iter(exclusive_disjoints[i])))
                        break
        if len(return_addresses) == m:
            break
    return return_addresses




    # temp = []
    # for disjoint in exclusive_disjoints:
    #     disjoint = set(disjoint)
    #     print("_______________________________")
    #     for batch in all_ips:
    #         batch = set(batch)
    #         if len(disjoint) == 1:
    #             temp.append(next(iter(disjoint)))
    #             break
    #         if len(batch & disjoint) != 0:
    #              other_disjoint_has_valid = True
    #              for other_disjoint in exclusive_disjoints:
    #                  other_disjoint = set(other_disjoint)
    #                  if other_disjoint & batch:
    #                      b = False
    #                      break
    #              if b:
    #                   disjoint = disjoint & batch
    #                   print(disjoint)
    #return temp

ip_addresses = intersect(all_ips, 8)

def calculate_IPs_as_int(ip_addresses):
    sum = 0
    while len(ip_addresses) > 0:
        sum += int(ipaddress.IPv4Address(ip_addresses.pop()))
    return sum
print(ip_addresses)
print(calculate_IPs_as_int(ip_addresses))
