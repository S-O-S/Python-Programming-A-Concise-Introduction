def problem3_1(txtfilename):
    sum=0
    f = open(txtfilename)
    for line in f.readlines():
        sum+=len(line)
        print(line, end="")
    f.close()
    print("\n\nThere are",sum,"letters in the file.")