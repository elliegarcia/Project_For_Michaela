import sys
directoryfile = open(sys.argv[1], "r")
directorystring = directoryfile.read()

directorystring = directorystring.replace('\n', ' ')
directorystring = directorystring.replace('..........................', '')
directorystring = directorystring.replace('.........................', '')
directorystring = directorystring.strip()
directorylist = directorystring.split('OCMR')
studentdictionary = {}

for line in directorylist:
    studentlist = line.split(' ')
    print studentlist
    if ('Col' in studentlist):
        col = studentlist.index('Col') - 1
        colkey = ", ".join(studentlist[3:6])
        studentdictionary[colkey] = studentlist[col]

    elif ('Con' in studentlist):
        con = studentlist.index('Con') - 1
        conkey = ", ".join(studentlist[3:6])
        studentdictionary[conkey] = studentlist[con]

    elif ('Dbl' in studentlist):
        dbl = studentlist.index('Dbl') - 1
        dblkey = ", ".join(studentlist[3:6])
        studentdictionary[dblkey] = studentlist[dbl]

studentdictionary.keys()
# medianvaluefile = open(sys.argv[2], "r")
# for x in range(0,14830):
#     line = medianvaluefile.readline()
#     if queryname[0:5] in line:
#         print line[6:]