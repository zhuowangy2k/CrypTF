import math

BLOCK_SIZE = 16
UMAX = int(math.pow(256, BLOCK_SIZE))

def to_bytes(n):
    s = hex(n)
    s_n = s[2:]
    if 'L' in s_n:
        s_n = s_n.replace('L', '')
    if len(s_n) % 2 != 0:
        s_n = '0' + s_n
    decoded = binascii.unhexlify(s_n)
    return decoded

f = open("AES-ABC/body.enc.ppm",'rb')
content = f.read()
f.close()

header = content[:16]
data = content[16:]

print(len(data)/16)
blocks = [data[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE] for i in range(int(len(data) / BLOCK_SIZE))]

import binascii

for i in range(len(blocks)-1, 0,-1):
    prev_blk = int(binascii.hexlify(blocks[i-1]),16)
    curr_blk = int(binascii.hexlify(blocks[i]),16)
    if curr_blk>=prev_blk:
        blocks[i] = to_bytes(curr_blk-prev_blk)
    else:
        blocks[i] = to_bytes(curr_blk+UMAX-prev_blk)

blocks.remove(blocks[0])
t = b"".join(blocks)

f = open("body_trans_ppm",'wb')
f.write(header)
f.write(t)
f.close()

#picoCTF{d0Nt_r0ll_yoUr_0wN_aES}