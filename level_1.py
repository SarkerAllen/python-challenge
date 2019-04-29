s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw " \
    "rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

a = "map"


def change_str(s):
    if s is 'y':
        return 'a'
    if s is 'z':
        return 'b'
    if s.isalpha() and s not in 'yz':
        return chr(ord(s) + 2)
    return s


ns = map(change_str, s)
na = map(change_str, a)

print(''.join(ns))
print(''.join(na))
