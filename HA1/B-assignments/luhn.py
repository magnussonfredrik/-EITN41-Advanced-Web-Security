# Assignment B-1
# Authors: Fredrik Magnusson & Martin Gottlander

file = open('inputdata.txt')

def findX(n):
    for i in range(0, 10):
        temp = n.replace("X", str(i))
        temp = temp.replace("\n", "")
        digits = [int(d) for d in str(temp)]
        odd = digits[-1::-2]
        even = digits[-2::-2]
        checksum = 0
        checksum += sum(odd)
        for digit in even:
            if digit > 4:
                checksum += digit * 2 - 9
            else:
                checksum += digit * 2
        if checksum % 10 == 0:
            return str(i)

answer = ""
for line in file.readlines():
    answer += findX(line)
print(answer)
