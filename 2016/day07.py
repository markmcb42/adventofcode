from collections import Counter
import hashlib


def check_aba(supers):
    aba = []
    for test in supers:
        for i in range(len(test) - 2):
            if test[i] == test[i + 2]:
                if test[i] != test[i + 1]:
                    val = test[i:i + 3]
                    aba.append(val)

    return aba


def is_abba(data):
    isabba = False
    for i in range(1, len(data) - 2):
        if data[i] == data[i + 1]:
            if data[i - 1] == data[i + 2]:
                if data[i - 1] != data[i]:
                    isabba = True
                    break
    return isabba


def test_abba(supers, hypers):
    # If any of the hypernet have abba, return false
    for hyper in hypers:
        if is_abba(hyper):
            return False

    # If any of the supernets have abba, return true
    for test in supers:
        if is_abba(test):
            return True
    return False


tls_count = 0
ssl_count = 0

file = open('input.txt', 'r')
for line in file:
    strs = []
    hypers = []

    line = line.strip()

    i = 0
    while True:
        lpos = line.find('[', i)
        if lpos == -1:
            strs.append(line[i:])
            break
        test = line[i:lpos]
        i += len(test) + 1
        strs.append(test)
        rpos = line.find(']', i)
        hyper = line[lpos + 1:rpos]
        hypers.append(hyper)
        i += len(hyper) + 1

    if test_abba(strs, hypers):
        tls_count += 1

    ssl = False
    abas = check_aba(strs)
    for aba in abas:
        bab = aba[1] + aba[0] + aba[1]
        for hyper in hypers:
            if bab in hyper:
                ssl = True
                break
    if ssl:
        ssl_count += 1

print('TLS Count: {} SSL Count {}'.format(tls_count, ssl_count))
