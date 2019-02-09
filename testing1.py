
f = open("ot.txt", "w+")
fr = open('in.txt', 'r')

for i in fr.read():
        f.write(i)
f.close()