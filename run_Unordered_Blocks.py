import os
import time
import datetime 
from blockchain_parser.blockchain import Blockchain

# Instantiate the Blockchain by giving the path to the directory 
# containing the .blk files created by bitcoind
def parse_block_with_date(timestamp):
    start = [2018,12] # choose the start date: start[0]: year & start[1]: month
    end = [2021,1] # choose the end date: end[0]: year & end[1]: month
    year_month = timestamp.strip(' ')[0:7]
    # print("year_month: ", year_month)
    mydate = year_month.split('-')
    year = int(mydate[0])
    month = int(mydate[1])
    # print("year: ", year)
    # print("month: ", month)
    if year == 2019 or year == 2020:
        return True
    if year == 2018 and month == 12:
        return True
    if year == 2021 and month == 1:
        return True
    return False
foutput = open("base58.txt", 'a')
fbech32 = open("bech32.txt", 'a')
blockchain = Blockchain(os.path.expanduser('~/.bitcoin/blocks'))
for block in blockchain.get_unordered_blocks():
    timestamp = block.header.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    # print("block time: %s" % (timestamp))
    if not parse_block_with_date(timestamp):
        continue
    for tx in block.transactions:
        for no, output in enumerate(tx.outputs):
            # print("tx=%s outputno=%d type=%s value=%s" % (tx.hash, no, output.type, output.value))
            print("block time: %s" % (timestamp))
            for addr in output.addresses:
                if addr.address.startswith("bc"):
                    fbech32.write(addr.address + '\n')
                else:
                    foutput.write(addr.address+'\n')
                # print(addr)
foutput.close()
fbech32.close()
