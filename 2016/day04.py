from collections import Counter

file = open('input.txt', 'r')
total = 0
for line in file:
    line = line.strip()

    # Get checksum,
    chksum = line[line.find('[') + 1: len(line) - 1]
    pos = line.rfind('-')
    id = int(line[pos + 1 : line.find('[')])
    code = line[:pos]
    counts = Counter(code)

    # Verify checksum
    is_valid = True
    for i in range(len(chksum) - 1):
        c1 = chksum[i]
        c2 = chksum[i+1]
        if counts[c1] < counts[c2] or counts[c1] == 0 or counts[c2] ==0:
            is_valid = False
            break

        if counts[c1] > counts[c2]:
            continue

        if c1 >= c2:
            is_valid = False
            break

    if is_valid:
        total += id
        decrypt = ''
        shift = id % 26
        for c in code:
            if c == '-':
                decrypt += ' '
                continue

            val = chr(ord(c) + shift)
            if val > 'z':
                diff = ord('z') - ord(c)
                val = chr(ord('a') + (shift - diff - 1))
            decrypt += val
        if 'north' in decrypt:
            print(decrypt, id)


print('Total is {}'.format(total))