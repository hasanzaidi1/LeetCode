def findComplement(num):

    binary = bin(num)[2:]
    flipped_bits = []
    for i in range(len(binary)):
        if binary[i] == '1':
            flipped_bits.append('0')
        else:
            flipped_bits.append('1')

    flipped_num_bin = ''
    for i in range(len(flipped_bits)):
        flipped_num_bin += flipped_bits[i]

    flipped_num = int(flipped_num_bin, 2)
    return flipped_num

print(findComplement(5))
print(findComplement(1))

