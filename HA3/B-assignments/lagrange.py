k, n = 0, 0


def chill():
    while not 3 <= k < n <= 8:
        print("parameters must fulfill 3 <= k < n <= 8")
        k = int(input("Enter the parameter k"))
        n = int(input("Enter parameter n"))


private_pol = [int(x) for x in input("Enter private polynomial, in order, with space between each coeff").split()]
poly_shares = [int(x) for x in input("Enter polynomial shares, in order, with space between each").split()]
master_poly_points = input("Enter all points on master polynomial as [participant_id:participant_value] with spaces between").split()
key_values = [x.split(':') for x in master_poly_points]
### For testing ###
#private_pol = [9, 19, 5]
#poly_shares = [37, 18, 40, 44, 28]
#master_poly_points = ['4:1385', '5:2028']


def interpolate(dictionary):
    sum = 0
    for i in dictionary.keys():
        mul = 1
        for j in dictionary.keys():
            if j != i:
                mul = j / (i - j) * mul
        sum += dictionary[i] * mul
    return sum

# Calculates polynomial
def calc_pol(pol, x):
    sum = pol[0]
    for i in range(1, len(pol)):
        sum += pol[i] * x ** i
    return sum



poly_values = {}
poly_values[1] = calc_pol(private_pol, 1) + sum(poly_shares)
for i in key_values:
    poly_values[int(i[0])] = int(i[1])

print("Deactivation code: ", abs(int(interpolate(poly_values))))
