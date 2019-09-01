with open("simple_logic/output") as f:
    content = f.readlines()

flagenc = int(content[0].split()[2],16)
# print(hex(flagenc))
content.remove(content[0])

pairs = []

for line in content:
    s = line.split(' ')
    p = int(s[2][6:],16)
    c = int(s[3][4:],16)
    #print(hex(p),hex(c))
    pairs.append((p,c))

ROUNDS = 765

def enc(msg,key,bits):
    enc = msg
    mask = (1<<bits)-1
    for i in range(ROUNDS):
        enc = (enc+key) & mask
        enc = enc^key
    return enc 

def dec(msg,key,bits):
    enc = msg
    mask = (1<<bits)-1
    for i in range(ROUNDS):
        enc = enc^key
        enc = (enc-key) & mask
    return enc 

proList = [0]

for B in range(16):
    bits = (B+1)*8
    newproList = []
    for prokey in proList:
        for i in range(256):
            key = (i<<(B*8)) + prokey
            cal = 0
            for pair in pairs:
                p,c = pair
                mask = (1<<bits)-1
                p = p&mask
                c = c&mask
                if c==enc(p,key,bits):
                    cal+=1
            if cal==6:
                print(B,key)
                newproList.append(key)
    proList = newproList.copy()

for finalkey in proList:
    print('%x' % dec(flagenc,finalkey,128))


