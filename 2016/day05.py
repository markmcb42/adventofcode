from collections import Counter
import hashlib

input = 'ugkcyxxp'
count = 0

password = {}
while True:

    count += 1
    test = input + str(count)
    result = (hashlib.md5(test.encode())).hexdigest()

    if '00000' == result[:5]:
        if result[5].isdigit():
            pos = int(result[5])
            if pos > 7:
                continue
            if pos in password:
                continue
            password[pos] = result[6]

    if len(password) == 8:
        break

print(password)




