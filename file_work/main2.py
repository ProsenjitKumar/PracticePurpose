keyword = ['auto', 'double', 'int', 'struct', 'break', 'else', 'long',
       'switch', 'case', 'enum', 'register', 'typedef', 'char',
       'extern', 'return', 'union', 'const', 'float', 'short',
       'unsigned', 'continue', 'for','signed', 'void', 'default',
       'goto', 'sizeof', 'volatile','do', 'if', 'static', 'while']


f_read = open('input.txt', mode='r')

data_type_dict = {}

#a = {'float' : 'Prosenjit das', 'nickname' : 'Prosenjit', 'email' : 'prosenjitearnkumar.com', 'int' : '01711223344'}

for in_key in f_read.read().split():
    if in_key not in data_type_dict:
        #data_type_dict[in_key] = 1
        for key in keyword:
            data_type_dict[in_key] = 1
            if key in data_type_dict:
                print(key)

    # else:
    #     for key in keyword:
    #         if key in data_type_dict:
    #             data_type_dict[in_key] += 1

# for key in keyword:
#     if key in a:
#         print(key)


f_read.close()
