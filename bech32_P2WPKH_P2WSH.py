'''
    split the hex_bech.txt into two file: P2WPKH type hex, P2WSH type
'''
fin = open("hex_bech32.txt", 'r')
fout1 = open("hex_bech32_P2WPKH.txt", 'a')
fout2 = open("hex_bech32_P2WSH.txt", 'a')
line = fin.readline()
while True:
    line = line.strip('\n')
    if len(line) == 40:
        fout1.write(line + '\n')
    elif len(line) == 64:
        fout2.write(line + '\n')
    else:
        break
    line = fin.readline()
fin.close()
fout1.close()
fout2.close()
