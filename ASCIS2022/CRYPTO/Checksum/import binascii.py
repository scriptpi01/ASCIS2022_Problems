import binascii

FLAG = 'ASCIS{XXXXXXXXXXX}'

def check_key(passwd):
    if len(passwd) < 16:
        return False
    if binascii.crc32(passwd.encode()) != binascii.crc32(FLAG.encode()):
        return False
    return True

password = input('What is the password?: ')
if check_key(password):
    print('Correct! Here is the flag: ' + FLAG)
else:
    print('Sorry! This is the hash we want:' + str(hex(binascii.crc32(FLAG.encode()))))