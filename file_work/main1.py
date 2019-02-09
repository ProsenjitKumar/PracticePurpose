keyword = ['auto', 'double', 'int', 'struct', 'break',
           'else', 'long', 'switch', 'case', 'enum', 'register', 'typedef', 'char',
           'extern', 'return', 'union', 'const', 'float', 'short', 'unsigned', 'continue', 'for',
           'signed', 'void', 'default', 'goto', 'sizeof', 'volatile', 'do', 'if', 'static', 'while']

# f_read = open('input.txt', mode='r')
# f_write =  open('output.txt', 'w')
# for i in f_read.read():
#         f_write.write(i)
# f_write.close()
# f_read.close()


empty = []
key_count = {}
for key in keyword:
    with open('input.txt', mode='r') as read_fp:
        if key in read_fp.read():
            # if key in empty:
            #     empty[key] += 1
            print(empty)
            with open('output.txt', 'w') as write_fp:
                write_fp.write(' \n'.join(empty))
    #         write_fp.close()
    # read_fp.close()
print(empty)

