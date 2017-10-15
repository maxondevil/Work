target = open('Result_FRESH_base.txt', 'w')
source = open('baza_23-45_Zh_verkhnyaya_chast_goroda.txt', 'r')
debugging = open('Debug.txt', 'w')
base = set()
alert_count = 0
duplicate_count = 0
eight_count = 0
nine_count = 0
for line in source:
    newline = []
    for c in line:
        if c.isdigit():
            newline.append(c)
    if newline == []:
        continue
    if newline[0] == '8':
        debugg = ''.join(newline)
        debugging.write('%s\n' % debugg)
        newline[0] = '7'
        eight_count += 1
    elif newline[0] == '9':
        debugg = ''.join(newline)
        debugging.write('%s\n' % debugg)
        newline.insert(0, '7')
        nine_count += 1
    new_string = ''.join(newline)
    if new_string not in base:
        base.add(new_string)
        if len(newline) != 11 or newline[0] != '7' or newline[1] != '9':
            print new_string
            target.write('%s ALERT!\n' % new_string)
            alert_count += 1
        else:
            target.write('%s\n' % new_string)
    else:
        duplicate_count += 1
print alert_count, duplicate_count
print 'nines: %d  eights: %d' % (nine_count, eight_count)
