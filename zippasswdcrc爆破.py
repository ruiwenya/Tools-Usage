import binascii
import string

def crack_crc():
    print('-------------Start Crack CRC-------------')
    crc_list = [0x14433530, 0xaf251007, 0xd554e7b6, 0xebb3156, 0xbb474d49, 0x2cb8a39b, 0x75fe76f0]
    comment = ''
    chars = string.printable
    for crc_value in crc_list:
        for char1 in chars:
            for char2 in chars:
                for char3 in chars:
                    res_char = char1 + char2 + char3
                    char_crc = binascii.crc32(res_char.encode())
                    calc_crc = char_crc & 0xffffffff
                    if calc_crc == crc_value:
                        print('[+] {}: {}'.format(hex(crc_value),res_char))
                        comment += res_char
    print('-----------CRC Crack Completed-----------')
    print('Result: {}'.format(comment))

if __name__ == '__main__':
    crack_crc()
