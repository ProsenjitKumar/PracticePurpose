# try:
#     fp = open('input.txt')
#     print(fp)
# finally:
#     fp.close()

# filepath = 'input.txt'
# with open(filepath) as fp:
#    line = fp.readline()
#    cnt = 1
#    while line:
#        print("Line {}: {}".format(cnt, line.strip()))
#        line = fp.readline()
#        cnt += 1

# filepath = 'input.txt'
# with open(filepath) as fp:
#    for cnt, line in enumerate(fp):
#        print("Line {}: {}".format(cnt, line))

# import sys
# import os
#
# def main():
#    filepath = sys.argv[1]
#
#    if not os.path.isfile(filepath):
#        print("File path {} does not exist. Exiting...".format(filepath))
#        sys.exit()
#
#    bag_of_words = {}
#    with open(filepath) as fp:
#        cnt = 0
#        for line in fp:
#            print("line {} contents {}".format(cnt, line))
#            record_word_cnt(line.strip().split(' '), bag_of_words)
#            cnt += 1
#    sorted_words = order_bag_of_words(bag_of_words, desc=True)
#    print("Most frequent 10 words {}".format(sorted_words[:10]))
#
# def order_bag_of_words(bag_of_words, desc=False):
#    words = [(word, cnt) for word, cnt in bag_of_words.items()]
#    return sorted(words, key=lambda x: x[1], reverse=desc)
#
# def record_word_cnt(words, bag_of_words):
#    for word in words:
#        if word != '':
#            if word.lower() in bag_of_words:
#                bag_of_words[word.lower()] += 1
#            else:
#                bag_of_words[word.lower()] = 1
#
# if __name__ == '__main__':
#    main()


# x = open("input.txt").read().splitlines()
# print(x)


# with open('input.txt', 'r', encoding='utf-8') as f:
#     content = f.readlines()
# # you may also want to remove whitespace characters like `\n` at the end of each line
# content = [x.strip() for x in content]
# print(content)

# lines = ['     A first string  ',
#          'A Unicode sample: €',
#          'German: äöüß']
#
# # Write text file
# with open('output.txt', 'w') as fp:
#     fp.write('\n'.join(lines))
#
# # Read text file
# with open('input.txt', 'r') as fp:
#     read_lines = fp.readlines()
#     read_lines = [line.rstrip('\n') for line in read_lines]
#
# print(lines == read_lines)


# lines = open('input.txt', 'r')
# filter_line = []
# if 'status' in lines:
#     filter_line.append(lines)
#     with open('output.txt', 'w') as fp:
#         fp.write('\n'.join(filter_line))
# else:
#     print('not found')
#
# name = input("~ Please enter Your name below: ")
# ban_path = 'input.txt' # be sure to replace by the full path
#
# with open(ban_path , mode='r', encoding='utf-8') as f:
#     if name in f.read():
#         print('your name {n} is in the list'.format(n=name))
#         with open('output.txt', 'w') as write_fp:
#             write_fp.write(name)
#     else:
#         print('your name {n}, was not found in the list'.format(n=name))

# def word_count_dict(fname):
#     from os.path import isfile
#     if isfile(fname):
#         d={}
#         with open(fname) as fi:
#             for line in fi:
#                 entries=line.split('~')
#                 for elem in entries[1:]:
#                     d[elem]=d.get(elem,[])+[entries[0]]
#         for k in d:
#             print (k,len(d[k]))
#
# word_count_dict('topics.txt')

# with open('input.txt', 'r') as f:
#     for line in f:
#         print(line[:-1])

# with open('input.txt', 'r') as f:
#     for line in f:
#         if line.endswith('\n'):
#             line = line[:-1]
#         print(line)

# f = open("input.txt", "r")
# print(f.read(10))

# import json
#
# with open('input.txt') as fp:
#     data = json.load(fp)
#
# for user in data:
#     print(user['user']['user_id'])

# with open('input.txt', 'rb') as file_in:
#     with open("output.txt", "wb") as file_out:
#         file_out.writelines(filter(lambda line: b'lines with this text' in line, file_in))
