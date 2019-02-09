# file = open('in.txt', 'r')
# wordcount={}
# for word in file.read().split():
#     if word not in wordcount:
#         wordcount[word] = 1
#     else:
#         wordcount[word] += 1
# print (wordcount)
# file.close()

# word_list = ['Emma', 'Woodhouse', 'father', 'Taylor', 'Miss', 'been', 'she', 'her']
# # i'm using this example text in place of the file you are using
# text = 'This is an example text. It will contain words you are looking for, like Emma, Emma, Emma, Woodhouse, Woodhouse, Father, Father, Taylor,Miss,been,she,her,her,her. I made them repeat to show that the code works.'
# text = text.replace(',', ' ')  # these statements remove irrelevant punctuation
# text = text.replace('.', '')
# text = text.lower()  # this makes all the words lowercase, so that capitalization wont affect the frequency measurement
#
# for repeatedword in word_list:
#     counter = 0  # counter starts at 0
#     for word in text.split():
#         if repeatedword.lower() == word:
#             counter = counter + 1  # add 1 every time there is a match in the list
#     print(repeatedword, ':', counter)

# file=open("in.txt","r+")
# wordcount={}
# for word in file.read().split():
#     if word not in wordcount:
#         wordcount[word] = 1
#     else:
#         wordcount[word] += 1
# for k,v in wordcount.items():
#     # with open('ot.txt', 'w') as fp:
#     #     fp.write(file)
#     print(k, v)

# import sys
# file=open('in.txt',"r")
# wordcount={}
# for word in file.read().split():
#     if word not in wordcount:
#         wordcount[word] = 1
#     else:
#         wordcount[word] += 1
# for key in wordcount.keys():
#   print ("%s %s " %(key , wordcount[key]))
# file.close()


wordCounter = {}

with open('in.txt','r') as fh:
  for line in fh:
    # Replacing punctuation characters. Making the string to lower.
    # The split will spit the line into a list.
    word_list = line.replace(',','').replace('\'','').replace('.','').lower().split()
    for word in word_list:
      # Adding  the word into the wordCounter dictionary.
      if word not in wordCounter:
        wordCounter[word] = 1
      else:
        # if the word is already in the dictionary update its count.
        wordCounter[word] = wordCounter[word] + 1

print('{:15}{:3}'.format('Word','Count'))
print('-' * 18)

# printing the words and its occurrence.
for  (word,occurance)  in wordCounter.items():
  print('{:15}{:3}'.format(word,occurance))