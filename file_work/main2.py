keyword = ['auto', 'double', 'int', 'struct', 'break', 'else', 'long',
       'switch', 'case', 'enum', 'register', 'typedef', 'char',
       'extern', 'return', 'union', 'const', 'float', 'short',
       'unsigned', 'continue', 'for','signed', 'void', 'default',
       'goto', 'sizeof', 'volatile','do', 'if', 'static', 'while']


f_read = open('input.txt', mode='r')

data_type_dict = {}

#a = {'float' : 'Prosenjit das', 'nickname' : 'Prosenjit', 'email' : 'prosenjitearnkumar.com', 'int' : '01711223344'}

for in_key in f_read.read().split():
    data_type_dict[in_key] = data_type_dict
for key in keyword:
    if key in data_type_dict:
        print(key)

    # if in_key not in data_type_dict:
    #     #data_type_dict[in_key] = 1
    #     for key in keyword:
    #         data_type_dict[in_key] = 1
    #         if key in data_type_dict:
    #             print(key)

    # else:
    #     for key in keyword:
    #         if key in data_type_dict:
    #             data_type_dict[in_key] += 1

# for key in keyword:
#     if key in a:
#         print(key)

# keyword = ['auto', 'double', 'int', 'struct', 'break', 'else', 'long',
#        'switch', 'case', 'enum', 'register', 'typedef', 'char',
#        'extern', 'return', 'union', 'const', 'float', 'short',
#        'unsigned', 'continue', 'for','signed', 'void', 'default',
#        'goto', 'sizeof', 'volatile','do', 'if', 'static', 'while']
#
# f_read = open('input.txt', mode='r')
# f_write =  open('output.txt', 'a')
# for i in f_read.read():
#     f_write.write(i)
# f_read.close()
# empty = []
# for key in keyword:
#     with open('input.txt', mode='r') as read_fp:
#         if key in read_fp.read():
#             if key in empty:
#                 empty[key] += 1
#             with open('output.txt', 'w') as write_fp:
#                 empty.append(key)
#                 write_fp.write(' \n'.join(empty))
# f_write.close()

