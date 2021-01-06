fin = open("hex.txt", 'r')
fout = open("hash160.txt", 'a')
line = fin.readline()
while line:
    line = line.strip('\n')
    if line:
        line = line[2:42]
        fout.write(line + '\n')
        line = fin.readline()
    else:
        break
fin.close()
fout.close()
