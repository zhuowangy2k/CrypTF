import gmpy2,binascii

c=76914867288108301315431196006031214067021632316952127876703442040817997718304320965837302299143144834655173895951465057381425677684365871750350098536277586201498897474802453358559917080942284944063260504783637720787260003538144672914131953688044791360909442596470141688712615745171175353831261668954872494207504356757323832458542594422597212678
n=106004214153119268656713773594444383625903613614257819846990416385081562102381120727274865160959759662419336294429454993757562677729681583954909798169595707974215974537020322568560390173259055145476518790014284998577353513189268141719572431402689057295337814189745267298857850416390904149034732999004207463905800257313948455303325424314906612449
e=65537
# sage : factor(m)
factors = [8774992249 , 8794506433 , 8994041171 , 9497168557 , 9905905769 , 10022017909 , 10810473721 , 10823705279 , 11030634299 , 11609298719 , 11692944779 , 12337175269 , 12505918357 , 12896163937 , 13165589431 , 13811829817 , 14150077289 , 14260678561 , 14517594901 , 14589259151 , 14625695353 , 14710288643 , 14711556661 , 15414482731 , 15459385597 , 15628218607 , 15761805803 , 15831453623 , 15904588423 , 16093350641 , 16404041887 , 16853984981 , 16871685331 , 17024350283]
phin = 1
for i in factors:
    phin = phin*(i-1)
d = gmpy2.invert(e,phin)
m = gmpy2.powmod(c,d,n)
def pflag(m):
    try:
        flag = binascii.unhexlify(hex(m)[2:])
        print(flag)
    except:
        pass
pflag(m)
