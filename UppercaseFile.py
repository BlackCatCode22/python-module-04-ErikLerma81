fh = open('file.txt')


for lx in fh:
    ly = lx.rstrip()
    print (ly.upper())