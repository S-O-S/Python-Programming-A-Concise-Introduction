import sys

file_read = sys.argv[1]
file_write = sys.argv[2]

f1 = open(file_read)
f2 = open(file_write, "w")
for line in f1:
    l = line.strip("\n")
    f2.write(str(len(l)) + "\n")
f2.close()    
f1.close()