keyword = ['auto', 'double', 'int', 'struct', 'break', 'else', 'long',
       'switch', 'case', 'enum', 'register', 'typedef', 'char',
       'extern', 'return', 'union', 'const', 'float', 'short',
       'unsigned', 'continue', 'for','signed', 'void', 'default',
       'goto', 'sizeof', 'volatile','do', 'if', 'static', 'while']

comments = ['//', '/*', '*/', '#']

f_read = open('input.txt', mode='r')
f_write =  open('output.txt', 'a')
content = 5
f_write.write("\n****Input File Code******\n\n")
for i in f_read.read():
    f_write.write(i)
f_read.close()
empty = []
for key in keyword:
    with open('input.txt', mode='r') as read_fp:
        if key in read_fp.read():
            if key in empty:
                empty[key] = 1
            with open('output.txt', 'w') as write_fp:
                empty.append(key)
                write_fp.write('Keyword List\n\n')
                write_fp.write(' \n'.join(empty,))
                write_fp.write('\n\n')

f_write.write("\n\n*******Without comment Code*******\n\n")


def skip_comments(file):
    for line in file:
        if not line.lstrip().startswith('//'):
            line = line.split("//")
            yield line[0]


f = open('input.txt')
for line in skip_comments(f):
    f_write.write(line)




f_write.close()

