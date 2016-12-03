f = open('combined_adders_flat', 'r')
o = open('combined_adders_flat.bc', 'w')
o.write('BC1.0\n')
for line in f:
    words = line.split()
    gate = words[0]
    for i in range(len(words)):
        words[i] = words[i].replace("#","")
    if (gate == 'nand'):
        if (len(words) == 6):
            # NAND4
            o.write('{4} := NOT(AND({0},{1},{2},{3}));\n'.format(words[1],words[2],words[3],words[4],words[5]))
        elif (len(words) == 5):
            # NAND3
            o.write('{3} := NOT(AND({0},{1},{2}));\n'.format(words[1],words[2],words[3],words[4]))
        elif (len(words) == 4):
            # NAND2
            o.write('{2} := NOT(AND({0},{1}));\n'.format(words[1],words[2],words[3]))
        elif (len(words) == 3):
            # INV
            o.write('{1} := NOT({0});\n'.format(words[1], words[2]))
        else:
            print('Error: NAND ')
            print(words)
    elif (gate == 'and'):
        if (len(words) == 4):
            # AND2
            o.write('{2} := AND({0},{1});\n'.format(words[1],words[2],words[3]))
        elif (len(words) == 3):
            # BUFFER
            o.write('{1} := {0};\n'.format(words[1],words[2]))
        else:
            print('Error: AND ')
            print(words)
    elif (gate == 'nor'):
        if (len(words) == 6):
            # NOR4
            o.write('{4} := NOT(OR({0},{1},{2},{3}));\n'.format(words[1],words[2],words[3],words[4],words[5]))
        elif (len(words) == 4):
            # NOR2
            o.write('{2} := NOT(OR({0},{1}));\n'.format(words[1],words[2],words[3]))
        else:
            print('Error: NOR ')
            print(words)
    elif (gate == 'or'):
        if (len(words) == 4):
            # OR2
            o.write('{2} := OR({0},{1});\n'.format(words[1],words[2],words[3]))
        else:
            print('Error: OR')
            print(words)
    elif (gate == 'mux2'):
        if (len(words) == 5):
            # MUX2
            o.write('{3} := OR((AND({0},{2})),(AND(NOT({0}),{1})));\n'.format(words[1],words[2],words[3],words[4]))
        else:
            print('Error: MUX')
            print(words)
    elif (gate == 'xor'):
        if (len(words) == 4):
            # XOR2
            o.write('{2} := OR((AND({0},NOT({1}))),(AND(NOT({0}),{1})));\n'.format(words[1],words[2],words[3]))
        else:
            print('Error: xor')
            print(words)
    else:
        print('Error: ')
        print(words[0])

# adds new variable checki := csi XOR rsi (where csi and rsi are the ith sum bit of the carry-lookahead and ripple adders respectively)
for i in range(32):
    i = str(i)
    o.write('check{0} := OR((AND(cs{0},NOT(rs{0}))),(AND(NOT(cs{0}),rs{0})));\n'.format(i))

f.close()
o.close()
