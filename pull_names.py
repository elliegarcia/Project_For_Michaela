import sys
directoryfile = open(sys.argv[1], "r")
directorystring = directoryfile.read()
directorystring = directorystring.replace('\xe2\x80\xa8', ' ')
directorystring = directorystring.strip()
directorylist = directorystring.split('\n')
print directorylist
studentdictionary = {}
for line in directorylist:
    studentlist = line.split(' ')
    if ('Col' in studentlist):
        col = studentlist.index('Col') - 1
        colkey = ", ".join(studentlist[:2])
        studentdictionary[colkey] = studentlist[col]
    elif ('Con' in studentlist):
        con = studentlist.index('Con') - 1
        conkey = ", ".join(studentlist[:2])
        studentdictionary[conkey] = studentlist[con]
    elif ('Dbl' in studentlist):
        dbl = studentlist.index('Dbl') - 1
        dblkey = ", ".join(studentlist[:2])
        studentdictionary[dblkey] = studentlist[dbl]

# medianvaluefile = open(sys.argv[2], "r")
# for x in range(0,14830):
#     line = medianvaluefile.readline()
#     if queryname[0:5] in line:
#         print line[6:]